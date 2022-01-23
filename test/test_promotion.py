import pytest

from src import promotion, basket, item


@pytest.fixture()
def builder():
    return item.ItemBuilder()


def test_promotion_a_initialiseabl():
    """Test the promotion on A can be initialised without exception."""
    assert promotion.ProAs()


def test_empty_basket_is_unchanged_after_apply():
    """An empty basket shouldn't be changed by applying the As promotion."""
    bas = basket.Basket()
    promo = promotion.ProAs()
    bas = promo.apply(bas)
    assert bas.total == 0


def test_with_no_as_basket_is_unchanged_after_apply(builder):
    """An a basket with no As will shouldn't be changed by applying the As promotion."""
    bas = basket.Basket([builder.get_b(), builder.get_c(), builder.get_d()])
    promo = promotion.ProAs()
    bas = promo.apply(bas)
    assert bas.total == 65


def test_with_one_a_basket_is_unchanged_after_apply(builder):
    """An a basket with one A will shouldn't be changed by applying the As promotion."""
    bas = basket.Basket([builder.get_a(), builder.get_c(), builder.get_d()])
    promo = promotion.ProAs()
    bas = promo.apply(bas)
    assert bas.total == 85


def test_with_two_as_basket_is_unchanged_after_apply(builder):
    """An a basket with two A will shouldn't be changed by applying the As promotion."""
    bas = basket.Basket([builder.get_a(), builder.get_a(), builder.get_d()])
    promo = promotion.ProAs()
    bas = promo.apply(bas)
    assert bas.total == 115


def test_with_three_as_basket_is_changed_after_apply(builder):
    """An a basket with two A will shouldn't be changed by applying the As promotion."""
    bas = basket.Basket([builder.get_a(), builder.get_a(), builder.get_a()])
    promo = promotion.ProAs()
    bas = promo.apply(bas)
    assert bas.total == 130
