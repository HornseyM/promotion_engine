import pytest

from src import promotion, basket, item


@pytest.fixture()
def builder():
    return item.ItemBuilder()


def test_promotion_a_initialiseable():
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
    """An a basket with three A will should be changed by applying the As promotion."""
    bas = basket.Basket([builder.get_a(), builder.get_a(), builder.get_a()])
    promo = promotion.ProAs()
    bas = promo.apply(bas)
    assert bas.total == 130


def test_with_four_as_basket_is_changed_after_apply(builder):
    """An a basket with 4 A will should be changed by applying the As promotion."""
    bas = basket.Basket([builder.get_a(), builder.get_a(), builder.get_a(), 
                        builder.get_a()])
    promo = promotion.ProAs()
    bas = promo.apply(bas)
    assert bas.total == 180


def test_with_four_as_basket_is_changed_once_only(builder):
    """An a basket with 4 A will should only be changed once by applying the
    As promotion."""
    bas = basket.Basket([builder.get_a(), builder.get_a(), builder.get_a(), 
                        builder.get_a()])
    promo = promotion.ProAs()
    bas = promo.apply(bas)
    bas = promo.apply(bas)
    assert bas.total == 180


def test_with_six_as_basket_is_changed_once_only(builder):
    """An a basket with 6 A will should be changed by applying the
    As promotion."""
    bas = basket.Basket([builder.get_a(), builder.get_a(), builder.get_a(), 
                        builder.get_a(), builder.get_a(), builder.get_a()])
    promo = promotion.ProAs()
    bas = promo.apply(bas)
    bas = promo.apply(bas)
    assert bas.total == 260
    
###




def test_promotion_b_initialiseable():
    """Test the promotion on B can be initialised without exception."""
    assert promotion.ProBs()


def test_empty_basket_is_unchanged_after_apply_b():
    """An empty basket shouldn't be changed by applying the Bs promotion."""
    bas = basket.Basket()
    promo = promotion.ProBs()
    bas = promo.apply(bas)
    assert bas.total == 0


def test_with_no_bs_basket_is_unchanged_after_apply_b(builder):
    """An a basket with no Bs will shouldn't be changed by applying the Bs promotion."""
    bas = basket.Basket([builder.get_a(), builder.get_c(), builder.get_d()])
    promo = promotion.ProBs()
    bas = promo.apply(bas)
    assert bas.total == 85


def test_with_one_b_basket_is_unchanged_after_apply(builder):
    """An a basket with one B will shouldn't be changed by applying the Bs promotion."""
    bas = basket.Basket([builder.get_b(), builder.get_c(), builder.get_d()])
    promo = promotion.ProBs()
    bas = promo.apply(bas)
    assert bas.total == 65


def test_with_two_bs_basket_is_changed_after_apply(builder):
    """An a basket with two B will should be changed by applying the Bs promotion."""
    bas = basket.Basket([builder.get_b(), builder.get_b(), builder.get_d()])
    promo = promotion.ProBs()
    bas = promo.apply(bas)
    assert bas.total == 60
