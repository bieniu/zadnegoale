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

TRANSLATE_STATES_MAP: Dict[str, str] = {
    "Bardzo niskie": "very low",
    "Bardzo wysokie": "very high",
    "Bez zmian": "steady",
    "Brak": "lack",
    "Niskie": "low",
    "Silny spadek": "strong falling",
    "Silny wzrost": "strong rising",
    "Spadek": "falling",
    "Wysokie": "high",
    "Wzrost": "rising",
    "Średnie": "medium",
}

TRANSLATE_ALLERGENS_MAP: List[Tuple[str, str]] = [
    ("ambrozja", "ragweed"),
    ("babka", "plantain"),
    ("brzoza", "birch_tree"),
    ("buk", "beech"),
    ("bylica", "mugwort"),
    ("cis", "yew"),
    ("dąb", "oak"),
    ("grab", "hornbeam"),
    ("jesion", "ash_tree"),
    ("klon", "maple"),
    ("komosa", "pigweed"),
    ("leszczyna", "hazel"),
    ("nawłoć", "goldenrod"),
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
