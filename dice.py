import random


def roll_die():
    return random.randint(1, 6)


def test_roll_die():
    assert random.randint(1, 6)
