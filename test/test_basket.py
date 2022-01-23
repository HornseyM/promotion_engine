import pytest

from context import basket, item


@pytest.fixture()
def builder():
    return item.ItemBuilder()


def test_basket_initialisable_without_exception():
    """Should be able to initalise a simple (e.g. empty) basket without an exception."""
    assert basket.Basket()


def test_initialising_basket_with_no_items():
    """Should be able to provide no items to a basket and it still initialises."""
    assert basket.Basket([])


def test_empty_basket_should_return_no_items():
    """If a basket is empty and the items are request it should return no items."""
    bas = basket.Basket()
    assert not bas.items


def test_empty_basket_should_have_zero_total():
    """If a basket is empty then it's total should be 0."""
    bas = basket.Basket()
    assert bas.total == 0


def test_basket_with_single_item_in_initialises(builder):
    """Initialise a basket with a single item in without exception."""
    assert basket.Basket([builder.get_a()])


def test_basket_with_multiple_items_in_initialises(builder):
    """Initialise a basket with a multiple items in without exception."""
    assert basket.Basket([builder.get_a(), builder.get_b(), builder.get_c()])


def test_basket_with_single_item_returns_item(builder):
    """A basket with a single item in should be able to return it."""
    items = [builder.get_a()]
    bas = basket.Basket(items)
    assert bas.items == items


def test_basket_with_multiple_items_returns_the_items(builder):
    """A basket with multiple items in should return them all."""
    items = [builder.get_a(), builder.get_b(), builder.get_c()]
    bas = basket.Basket(items)
    assert bas.items == items


def test_basket_with_single_item_calculates_total(builder):
    """A basket with a single item in should calculate the correct total."""
    items = [builder.get_a()]
    bas = basket.Basket(items)
    assert bas.total == 50


def test_basket_with_multiple_items_returns_the_items(builder):
    """A basket with multiple items in should calculate the correct total."""
    items = [builder.get_a(), builder.get_b(), builder.get_c()]
    bas = basket.Basket(items)
    assert bas.total == 100
