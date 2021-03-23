"""Constants for Zadnego Ale library."""
ATTR_DUSTS = "dusts"
ATTR_ALERTS = "alerts"

ENDPOINT = "http://api.zadnegoale.pl/"

HTTP_OK = 200

URLS = {
    ATTR_DUSTS: "dusts/public/date/{year}/region/{region}",
    ATTR_ALERTS: "alerts/public/date/{year}/region/{region}",
}
