"""Type definitions for ZadnegoAle."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Allergen:
    """Data class for allergen."""

    value: int
    trend: str
    level: str


@dataclass
class Allergens:  # pylint: disable=too-many-instance-attributes
    """Data class for allergens."""

    alternaria: Optional[Allergen]
    ambrozja: Optional[Allergen]
    babka: Optional[Allergen]
    brzoza: Optional[Allergen]
    buk: Optional[Allergen]
    bylica: Optional[Allergen]
    cis: Optional[Allergen]
    cladosporium: Optional[Allergen]
    dąb: Optional[Allergen]
    grab: Optional[Allergen]
    jesion: Optional[Allergen]
    klon: Optional[Allergen]
    komosa: Optional[Allergen]
    leszczyna: Optional[Allergen]
    olsza: Optional[Allergen]
    platan: Optional[Allergen]
    pokrzywa: Optional[Allergen]
    sosna: Optional[Allergen]
    szczaw: Optional[Allergen]
    topola: Optional[Allergen]
    trawy: Optional[Allergen]
    wierzba: Optional[Allergen]
    wiąz: Optional[Allergen]
