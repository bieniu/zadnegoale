"""Constants for Zadnego Ale library."""
from __future__ import annotations

from typing import Final

ATTR_DUSTS: Final[str] = "dusts"
ATTR_ALERTS: Final[str] = "alerts"

ENDPOINT: Final[str] = "http://api.zadnegoale.pl/"

URL: Final[str] = "{}/public/date/{}/region/{}"

ATTR_LEVEL: Final[str] = "level"
ATTR_TREND: Final[str] = "trend"
ATTR_VALUE: Final[str] = "value"

TRANSLATE_STATES_MAP: Final[dict[str, str]] = {
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

TRANSLATE_ALLERGENS_MAP: Final[list[tuple[str, str]]] = [
    ("alternaria", "alternaria"),
    ("ambrozja", "ragweed"),
    ("babka", "plantain"),
    ("brzoza", "birch_tree"),
    ("buk", "beech"),
    ("bylica", "mugwort"),
    ("cis", "yew"),
    ("cladosporium", "cladosporium"),
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
