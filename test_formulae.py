from formulae import highest_common_factor as hcf


def test_highest_common_factor():
    assert hcf(20, 50) == 10
    assert hcf(50, 20) == 10

    assert hcf(57, 57) == 57

    assert hcf(93, 13) == 1
