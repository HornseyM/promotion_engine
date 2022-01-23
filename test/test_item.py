from context import item



def test_item_initialisable():
    """Test that an item can be initialise without exception."""
    assert item.Item("A", 50)


def test_that_item_initialise_with_correct_name():
    """When items are initialised they are given a name; this name should 
    be correctly stored and returned."""
    sku = item.Item("A", 50)
    assert sku.name == "A"


def test_item_initialise_with_correct_name():
    """When items are initialised they are given a price; this price should 
    be correctly stored and returned."""
    sku = item.Item("A", 50)
    assert sku.price == 50
