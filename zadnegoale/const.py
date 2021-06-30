"""Constants for Zadnego Ale library."""
from typing import Dict, List, Optional, Union

ATTR_DUSTS: str = "dusts"
ATTR_ALERTS: str = "alerts"

ENDPOINT: str = "http://api.zadnegoale.pl/"

HTTP_OK: int = 200

URL: str = "{}/public/date/{}/region/{}"

ATTR_LEVEL: str = "level"
ATTR_TREND: str = "trend"
ATTR_VALUE: str = "value"

ALLERGENS: List[str] = [
    "alternaria",
    "ambrozja",
    "babka",
    "brzoza",
    "buk",
    "bylica",
    "cis",
    "cladosporium",
    "dąb",
    "grab",
    "jesion",
    "klon",
    "komosa",
    "leszczyna",
    "olsza",
    "platan",
    "pokrzywa",
    "sosna",
    "szczaw",
    "topola",
    "trawy",
    "wierzba",
    "wiąz",
]

ALLERGEN: Dict[str, Optional[Union[int, str]]] = {
    ATTR_VALUE: 0,
    ATTR_TREND: None,
    ATTR_LEVEL: "brak",
}

# RENAME_KEY_MAP = [
#     ("ambrozja", "ragweed"),
#     ("babka", "plantain"),
#     ("brzoza", "birch"),
#     ("buk", "beech"),
#     ("bylica", "mugwort"),
#     ("cis", "yew"),
#     ("dąb", "oak"),
#     ("", ""),
#     ("", ""),
#     ("", ""),
#     ("", ""),
#     ("", ""),
#     ("", ""),
#     ("", ""),
#     ("", ""),
#     ("", ""),
#     ("", ""),
#     ("", ""),
#     ("", ""),

# ]
