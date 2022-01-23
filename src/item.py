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