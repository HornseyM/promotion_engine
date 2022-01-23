import pytest

from context import item, basket, promotion

"""Aceptence test from customer are as follows:

Unit price for SKU IDs A	50
B	30
C	20
D	15

Active Promotions
3 of A's for 130
2 of B's for 45 
C & D for 30

Scenario A
1 * A -> 50
1 * B -> 30
1 * C -> 20

Total  = 100

Scenario B
5 * A -> 130 + 2*50
5 * B -> 45 + 45 + 30
1 * C -> 20 (orriginal was 28, assumed typo)

Total  = 370

Scenario C
3 * A -> 130
5 * B -> 45 + 45 + 1 * 30
1 * C -
1 * D -> 30

Total  = 280
"""


@pytest.fixture
def builder():
    return item.ItemBuilder()


def test_scenario_a(builder):
    """Scenario A is defined as follows:
    
    Scenario A
    (1 * A) + (1 * B) + (1 * C) = 100
    """
    # Make the basket of items
    items = [builder.get_a(), builder.get_b(), builder.get_c()]
    bas = basket.Basket(items)
    # Check the total is calculated correctly
    assert bas.total == 100


def test_scenario_b(builder):
    """Scenario B is defined as follows:
    
    Scenario B
    (5 * A) + (5 * B) + (1 * C) = 370
    """
    # Get the promotions
    pro_a = promotion.ProAs()
    pro_b = promotion.ProBs()
    # Get the items and make the basket
    all_a = [builder.get_a() for ii in range(5)]
    all_b = [builder.get_b() for ii in range(5)]
    items = all_a + all_b + [builder.get_c()]
    bas = basket.Basket(items)
    # Apply promotion A once
    bas = pro_a.apply(bas)
    # Apply promotion B once
    bas = pro_b.apply(pro_b.apply(bas))
    # Check the total is calculated with promotions applied
    assert bas.total == 370


def test_scenario_c():
    """Scenario C is defined as follows:
    
    Scenario C
    (3 * A) + (5 * B) + (1 * C) + (1 * D) = 280
    """
    assert False  # ToDo Complete when code exists
