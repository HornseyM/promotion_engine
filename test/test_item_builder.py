from context import item


def test_item_builder_initialise_without_exception():
    """Test that an item builder can be initialise without throwing an exception."""
    assert item.ItemBuilder()


def test_build_item_a_with_name():
    """Item Builder should be able to build item A with correct name."""
    builder = item.ItemBuilder
    sku = builder.get_a()
    assert sku.name == 'A'


def test_build_item_a_with_price():
    """Item Builder should be able to build item A with correct price."""
    builder = item.ItemBuilder
    sku = builder.get_a()
    assert sku.price == 50


def test_build_item_b_with_name():
    """Item Builder should be able to build item B with correct name."""
    builder = item.ItemBuilder
    sku = builder.get_b()
    assert sku.name == 'B'


def test_build_item_b_with_price():
    """Item Builder should be able to build item B with correct price."""
    builder = item.ItemBuilder
    sku = builder.get_b()
    assert sku.price == 30


def test_build_item_c_with_name():
    """Item Builder should be able to build item C with correct name."""
    builder = item.ItemBuilder
    sku = builder.get_c()
    assert sku.name == 'C'


def test_build_item_c_with_price():
    """Item Builder should be able to build item C with correct price."""
    builder = item.ItemBuilder
    sku = builder.get_c()
    assert sku.price == 20


def test_build_item_d_with_name():
    """Item Builder should be able to build item D with correct name."""
    builder = item.ItemBuilder
    sku = builder.get_d()
    assert sku.name == 'D'


def test_build_item_d_with_price():
    """Item Builder should be able to build item D with correct price."""
    builder = item.ItemBuilder
    sku = builder.get_d()
    assert sku.price == 15
