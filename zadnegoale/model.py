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

    alder: Allergen
    alternaria: Allergen
    ash_tree: Allergen
    beech: Allergen
    birch_tree: Allergen
    cladosporium: Allergen
    elm: Allergen
    goldenrod: Allergen
    grass: Allergen
    hazel: Allergen
    hornbeam: Allergen
    maple: Allergen
    mugwort: Allergen
    nettle: Allergen
    oak: Allergen
    pigweed: Allergen
    pine: Allergen
    plane_tree: Allergen
    plantain: Allergen
    poplar: Allergen
    ragweed: Allergen
    sorrel: Allergen
    willow: Allergen
    yew: Allergen
