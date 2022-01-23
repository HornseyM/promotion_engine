from typing import List, Optional

from .item import Item

"""Module to contain the Basket class and any helpers."""


class Basket:
    """A basket to hold and output items of a shop.
    
    :param items: The items to store in the basket.
    """

    def __init__(self, items: Optional[List[Item]] = None) -> None:
        self._items: List[Item] = items or []

    @property
    def items(self) -> List[Item]:
        """Return the items in the basket."""
        return self._items

    @property
    def total(self) -> int:
        """The total of the items in the basket."""
        return sum([item.price for item in self.items])
