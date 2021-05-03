"""Constants for Zadnego Ale library."""
from typing import Dict

ATTR_DUSTS: str = "dusts"
ATTR_ALERTS: str = "alerts"

ENDPOINT: str = "http://api.zadnegoale.pl/"

HTTP_OK: int = 200

URLS: Dict[str, str] = {
    ATTR_DUSTS: "dusts/public/date/{date}/region/{region}",
    ATTR_ALERTS: "alerts/public/date/{date}/region/{region}",
}
