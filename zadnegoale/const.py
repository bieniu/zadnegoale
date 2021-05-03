"""Constants for Zadnego Ale library."""
from typing import Dict, Final
ATTR_DUSTS: Final = "dusts"
ATTR_ALERTS: Final = "alerts"

ENDPOINT: Final = "http://api.zadnegoale.pl/"

HTTP_OK: Final = 200

URLS: Final[Dict[str, str]] = {
    ATTR_DUSTS: "dusts/public/date/{date}/region/{region}",
    ATTR_ALERTS: "alerts/public/date/{date}/region/{region}",
}
