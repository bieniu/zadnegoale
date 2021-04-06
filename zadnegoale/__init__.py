"""
Python wrapper for getting allergen data from Żadnego Ale API.
"""
import logging
from datetime import date
from typing import Optional, Union

from aiohttp import ClientSession

from .const import ATTR_ALERTS, ATTR_DUSTS, ENDPOINT, HTTP_OK, URLS

_LOGGER = logging.getLogger(__name__)


class DictToObj(dict):
    """Dictionary to object class."""

    def __getattr__(self, name):
        if name in self:
            return self[name]
        raise AttributeError("No such attribute: " + name)


class ZadnegoAle:
    """Main class to perform Zadnego Ale API requests"""

    def __init__(
        self, session: ClientSession, region: Union[int] = None, debug: bool = False
    ):
        """Initialize."""
        self._session = session
        if not isinstance(region, int) or not 0 < region < 10:
            raise InvalidRegionError("'region' should be an integer from 1 to 9")
        self._region = region
        self._region_name: Optional[str] = None
        self._debug = debug

    @staticmethod
    def _construct_url(arg: str, **kwargs) -> str:
        """Construct Zadnego Ale API URL."""
        url = ENDPOINT + URLS[arg].format(**kwargs)
        return url

    @staticmethod
    def _parse_dusts(data: list) -> dict:
        """Parse and clean dusts API response."""
        parsed = DictToObj(
            {
                item["allergen"]["name"].lower(): {
                    "value": item["value"],
                    "trend": item["trend"].lower(),
                    "level": item["level"].lower(),
                }
                for item in data
            }
        )

        return {"sensors": parsed}

    @staticmethod
    def _parse_alerts(data: list) -> dict:
        """Parse and clean alerts API response."""
        return {"alerts": {"value": data[0]["text"]}}

    async def _async_get_data(self, url: str) -> list:
        """Retreive data from Zadnego Ale API."""
        async with self._session.get(url) as resp:
            if resp.status != HTTP_OK:
                raise ApiError(f"Invalid response from Zadnego Ale API: {resp.status}")
            _LOGGER.debug("Data retrieved from %s, status: %s", url, resp.status)
            data = await resp.json()
            if data == "null":
                raise ApiError(f"Invalid response from Zadnego Ale API: {data}")
        return data

    async def async_update(self, alerts=False) -> DictToObj:
        """Retreive data from Zadnego Ale."""
        date_str = date.today().strftime("%Y%m%d")
        url = self._construct_url(ATTR_DUSTS, date=date_str, region=self._region)
        dusts = await self._async_get_data(url)

        if self._debug:
            _LOGGER.debug(dusts)

        if not self._region_name:
            self._region_name = dusts[0]["region"]["name"]

        if alerts:
            url = self._construct_url(ATTR_ALERTS, date=date_str, region=self._region)
            alerts = await self._async_get_data(url)

            if self._debug:
                _LOGGER.debug(alerts)

            return DictToObj({**self._parse_dusts(dusts), **self._parse_alerts(alerts)})

        return DictToObj(self._parse_dusts(dusts))

    @property
    def region_name(self) -> Optional[str]:
        """Return location name."""
        return self._region_name


class ApiError(Exception):
    """Raised when Zadnego Ale API request ended in error."""

    def __init__(self, status: str):
        """Initialize."""
        super().__init__(status)
        self.status = status


class InvalidRegionError(Exception):
    """Raised when region is invalid."""

    def __init__(self, status: str):
        """Initialize."""
        super().__init__(status)
        self.status = status
