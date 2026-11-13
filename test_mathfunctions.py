from mathfuncs import add, mean


def test_add():
    assert add(2, 3) == 6


def test_mean():
    assert mean([2, 4, 6]) == 4

