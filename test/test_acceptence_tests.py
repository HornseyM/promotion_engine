
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


def test_scenario_a():
    """Scenario A is defined as follows:
    
    Scenario A
    (1 * A) + (1 * B) + (1 * C) = 100
    """
    assert False  # ToDo Complete when code exists


def test_scenario_b():
    """Scenario B is defined as follows:
    
    Scenario B
    (5 * A) + (5 * B) + (1 * C) = 370
    """
    assert False  # ToDo Complete when code exists


def test_scenario_c():
    """Scenario C is defined as follows:
    
    Scenario C
    (3 * A) + (5 * B) + (1 * C) + (1 * D) = 280
    """
    assert False  # ToDo Complete when code exists
