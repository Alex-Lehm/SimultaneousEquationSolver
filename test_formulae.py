from formulae import highest_common_factor as hcf
from formulae import lowest_common_multiple as lcm


def test_highest_common_factor():
    assert hcf(20, 50) == 10
    assert hcf(50, 20) == 10

    assert hcf(57, 57) == 57

    assert hcf(93, 13) == 1


def test_lowest_common_multiple():
    assert lcm(2, 3) == 6
    assert lcm(3, 2) == 6

    assert lcm(12, 15) == 60

    assert lcm(4, 5) == 20
