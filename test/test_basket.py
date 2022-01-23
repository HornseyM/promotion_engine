from context import basket


def test_basket_initialisable_without_exception():
    """Should be able to initalise a simple (e.g. empty) basket without an exception."""
    assert basket.Basket()
