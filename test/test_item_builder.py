from context import item


def test_item_builder_initialise_without_exception():
    """Test that an item builder can be initialise without throwing an exception."""
    assert item.ItemBuilder()
