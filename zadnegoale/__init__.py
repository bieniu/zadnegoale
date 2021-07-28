"""
Python wrapper for getting allergen data from Żadnego Ale API.
"""
import logging
from datetime import date
from typing import Any, List, Optional

from aiohttp import ClientSession
from dacite import from_dict

from .const import (
    ATTR_ALERTS,
    ATTR_DUSTS,
    ATTR_LEVEL,
    ATTR_TREND,
    ATTR_VALUE,
    ENDPOINT,
    HTTP_OK,
    TRANSLATE_ALLERGENS_MAP,
    TRANSLATE_STATES_MAP,
    URL,
)
from .model import Allergens

_LOGGER = logging.getLogger(__name__)


class ZadnegoAle:
    """Main class to perform Zadnego Ale API requests"""

    def __init__(
        self, session: ClientSession, region: Optional[int] = None, debug: bool = False
    ) -> None:
        """Initialize."""
        self._session = session
        if not isinstance(region, int) or not 0 < region < 10:
            raise InvalidRegionError("'region' should be an integer from 1 to 9")
        self._region = region
        self._region_name: Optional[str] = None
        self._debug = debug

    @staticmethod
    def _construct_url(data_type: str, region: int) -> str:
        """Construct Zadnego Ale API URL."""
        date_str = date.today().strftime("%Y%m%d")
        url = ENDPOINT + URL.format(data_type, date_str, region)
        return url

    @staticmethod
    def _parse_dusts(data: list) -> Allergens:
        """Parse and clean dusts API response."""
        parsed = {
            item["allergen"]["name"].lower(): {
                ATTR_VALUE: item[ATTR_VALUE],
                ATTR_TREND: TRANSLATE_STATES_MAP[item[ATTR_TREND]],
                ATTR_LEVEL: TRANSLATE_STATES_MAP[item[ATTR_LEVEL]],
            }
            for item in data
        }
        for pol_name, eng_name in TRANSLATE_ALLERGENS_MAP:
            if pol_name in parsed:
                parsed[eng_name] = parsed.pop(pol_name)
            else:
                parsed[eng_name] = {}
        return from_dict(data_class=Allergens, data=parsed)

    @staticmethod
    def _parse_alerts(data: Any) -> List[str]:
        """Parse and clean alerts API response."""
        return [data[index]["text"] for index in range(len(data))]

    async def _async_get_data(self, url: str) -> Any:
        """Retreive data from Zadnego Ale API."""
        async with self._session.get(url) as resp:
            if resp.status != HTTP_OK:
                raise ApiError(f"Invalid response from Zadnego Ale API: {resp.status}")
            _LOGGER.debug("Data retrieved from %s, status: %s", url, resp.status)
            data = await resp.json()
            if data == "null":
                raise ApiError(f"Invalid response from Zadnego Ale API: {data}")
        return data

    async def async_get_dusts(self) -> Allergens:
        """Retreive dusts data from Zadnego Ale."""
        url = self._construct_url(ATTR_DUSTS, self._region)
        dusts = await self._async_get_data(url)

        if self._debug:
            _LOGGER.debug(dusts)

        if not self._region_name:
            self._region_name = dusts[0]["region"]["name"]

        return self._parse_dusts(dusts)

    async def async_get_alerts(self) -> List[str]:
        """Retreive dusts data from Zadnego Ale."""
        url = self._construct_url(ATTR_ALERTS, self._region)
        alerts = await self._async_get_data(url)

        if self._debug:
            _LOGGER.debug(alerts)

        return self._parse_alerts(alerts)

    @property
    def region_name(self) -> Optional[str]:
        """Return location name."""
        return self._region_name


class ApiError(Exception):
    """Raised when Zadnego Ale API request ended in error."""

    def __init__(self, status: str) -> None:
        """Initialize."""
        super().__init__(status)
        self.status = status


class InvalidRegionError(Exception):
    """Raised when region is invalid."""

    def __init__(self, status: str) -> None:
        """Initialize."""
        super().__init__(status)
        self.status = status
