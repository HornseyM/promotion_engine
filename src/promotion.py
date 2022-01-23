from .basket import Basket
from .item import Item
from src import basket

"""Module to store the curent promotions (for now)."""


class ProAs:
    """The promotion on A is buy 3 for 130. This class will find them in a
    basket and apply the promotion."""

    @staticmethod
    def apply(bas: Basket) -> Basket:
        """Takes in a basket and applies the promotion on A to the basket if
        there are about As, otherwise leaves it unchanged."""
        ret = bas
        # First get all the As
        a_items = [item for item in bas.items if item.name == "A"]
        # Check we have enough for a promotion
        if len(a_items) >= 3:
            rest_items = [item for item in bas.items if item.name != "A"]
            # If we have any extra, remove excess, putting them back with the
            # others
            if len(a_items) > 3:
                rest_items = rest_items + a_items[3:]
            rest_items = rest_items + [Item("3 As for 130", 130)]
            ret = basket.Basket(rest_items)
        return ret
