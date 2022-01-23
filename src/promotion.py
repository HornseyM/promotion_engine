from abc import ABC, abstractmethod

from .basket import Basket
from .item import Item
from src import basket

"""Module to store the curent promotions (for now)."""

class Promotion(ABC):

    @abstractmethod
    def apply(self, bas: Basket) -> Basket:
        """Abstract class for applying a promotion to a basket that all
        promotion classes should imlement.
        
        :param bas: The basket to apply the promotion to.
        """

    @staticmethod
    def _apply_n_items(bas: Basket, name: str, num: int,
                       replace: Item) -> Basket:
        """Takes in a basket and applies the promotion that replaces a number 
        of items of the same type with a lower price.
        
        :param bas: The basket to apply teh promotion to.
        :param name: The name if the item to replace.
        :param num: The number of items the promotion should apply to.
        :param replace: The item to replace them with.

        :returns: The basket with the promotion applied.
        """
        ret = bas
        # First get all the items
        a_items = [item for item in bas.items if item.name == name]
        # Check we have enough for a promotion
        if len(a_items) >= num:
            rest_items = [item for item in bas.items if item.name != name]
            # If we have any extra, remove excess, putting them back with the
            # others
            if len(a_items) > num:
                rest_items = rest_items + a_items[num:]
            # Finally add the promotion that is replacing the items and 
            # update the basket
            rest_items = rest_items + [replace]
            ret = basket.Basket(rest_items)
        return ret


class ProAs(Promotion):
    """The promotion on A is buy 3 for 130. This class will find them in a
    basket and apply the promotion.
        
    :param bas: The basket to apply the promotion to.
    """

    def apply(self, bas: Basket) -> Basket:
        """Takes in a basket and applies the promotion on A to the basket if
        there are enough As, otherwise leaves it unchanged.
        
        :param bas: The basket to apply the promotion to.

        :returns: The basket with the promotion applied.
        """
        return self._apply_n_items(bas, 'A', 3, Item("3 As for 130", 130))


class ProBs(Promotion):    
    """The promotion on B is buy 2 for 45. This class will find them in a
    basket and apply the promotion.
        
    :param bas: The basket to apply the promotion to.
    """

    def apply(self, bas: Basket) -> Basket:
        """Takes in a basket and applies the promotion on B to the basket if
        there are enough Bs, otherwise leaves it unchanged.
        
        :param bas: The basket to apply the promotion to.
        
        :returns: The basket with the promotion applied.
        """
        return self._apply_n_items(bas, 'B', 2, Item("2 bs for 450", 45))
