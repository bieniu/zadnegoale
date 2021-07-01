"""Constants for Zadnego Ale library."""
from typing import Dict, List, Tuple

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

TRANSLATE_STATES_MAP: Dict[str, str] = {
    "Bardzo niskie": "Very low",
    "Bardzo wysokie": "Very high",
    "Brak": "Lack",
    "Niskie": "Low",
    "Wysokie": "High",
    "Średnie": "Medium",
    "Bez zmian": "No change",
    "Wzrost": "Increase",
    "Spadek": "Decrease",
}

TRANSLATE_ALLERGENS_MAP: List[Tuple[str, str]] = [
    ("ambrozja", "ragweed"),
    ("babka", "plantain"),
    ("brzoza", "birch"),
    ("buk", "beech"),
    ("bylica", "mugwort"),
    ("cis", "yew"),
    ("dąb", "oak"),
    ("grab", "hornbeam"),
    ("jesion", "ash"),
    ("klon", "maple"),
    ("komosa", "pigweed"),
    ("leszczyna", "hazel"),
    ("olsza", "alder"),
    ("platan", "plane_tree"),
    ("pokrzywa", "nettle"),
    ("sosna", "pine"),
    ("szczaw", "sorrel"),
    ("topola", "poplar"),
    ("trawy", "grass"),
    ("wierzba", "willow"),
    ("wiąz", "elm"),
]
