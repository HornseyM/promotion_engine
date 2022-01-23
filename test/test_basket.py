from context import basket


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
