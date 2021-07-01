"""Type definitions for ZadnegoAle."""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Allergen:
    """Data class for allergen."""

    value: int = 0
    trend: Optional[str] = None
    level: str = "lack"


@dataclass
class Allergens:  # pylint: disable=too-many-instance-attributes
    """Data class for allergens."""

    alder: Optional[Allergen]
    alternaria: Optional[Allergen]
    ash: Optional[Allergen]
    beech: Optional[Allergen]
    birch: Optional[Allergen]
    cladosporium: Optional[Allergen]
    elm: Optional[Allergen]
    grass: Optional[Allergen]
    hazel: Optional[Allergen]
    hornbeam: Optional[Allergen]
    maple: Optional[Allergen]
    mugwort: Optional[Allergen]
    nettle: Optional[Allergen]
    oak: Optional[Allergen]
    pigweed: Optional[Allergen]
    pine: Optional[Allergen]
    plane_tree: Optional[Allergen]
    plantain: Optional[Allergen]
    poplar: Optional[Allergen]
    ragweed: Optional[Allergen]
    sorrel: Optional[Allergen]
    willow: Optional[Allergen]
    yew: Optional[Allergen]
