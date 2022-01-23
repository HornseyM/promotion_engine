"""Module to contain the item class."""


class Item:
    """An item, suitable for adding to a basket.
    
    :param name: The name of the item.
    :param price: The price of the item.
    """

    def __init__(self, name: str, price: int) -> None:
        self._name: str = name
        self._price: int = price

    @property
    def name(self) -> str:
        """Return the name variable."""
        return self._name
    
    @property
    def price(self) -> int:
        """Return the price variable."""
        return self._price

class ItemBuilder():
    """Class to build and return items consistently and correctly."""

    @staticmethod
    def get_a() -> Item:
        """Return an 'A' item which costs 50."""
        return Item('A', 50)

    @staticmethod
    def get_b() -> Item:
        """Return an 'B' item which costs 30."""
        return Item('B', 30)

    @staticmethod
    def get_c() -> Item:
        """Return an 'C' item which costs 20."""
        return Item('C', 20)

    @staticmethod
    def get_d() -> Item:
        """Return an 'D' item which costs 15."""
        return Item('D', 15)
