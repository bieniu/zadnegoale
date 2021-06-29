
"""Type definitions for ZadnegoAle."""
from dataclasses import dataclass

from typing import Optional

@dataclass
class AllergenData:
    """Data class for allergen."""

    value: int
    trend: str
    level: str


@dataclass
class Allergens:
    """Data class for allergens."""

    alternaria: Optional[AllergenData]
    ambrozja: Optional[AllergenData]
    babka: Optional[AllergenData]
    brzoza: Optional[AllergenData]
    buk: Optional[AllergenData]
    bylica: Optional[AllergenData]
    cis: Optional[AllergenData]
    cladosporium: Optional[AllergenData]
    dąb: Optional[AllergenData]
    grab: Optional[AllergenData]
    jesion: Optional[AllergenData]
    klon: Optional[AllergenData]
    komosa: Optional[AllergenData]
    leszczyna: Optional[AllergenData]
    olsza: Optional[AllergenData]
    platan: Optional[AllergenData]
    pokrzywa: Optional[AllergenData]
    sosna: Optional[AllergenData]
    szczaw: Optional[AllergenData]
    topola: Optional[AllergenData]
    trawy: Optional[AllergenData]
    wierzba: Optional[AllergenData]
    wiąz: Optional[AllergenData]
