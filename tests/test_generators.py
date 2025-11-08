from src.generators import card_number_generator

# import pytest


def test_card_number_generator():
    card_num = card_number_generator(5, 11)
    assert next(card_num) == "0000 0000 0000 0005"
    assert next(card_num) == "0000 0000 0000 0006"
    assert next(card_num) == "0000 0000 0000 0007"
    assert next(card_num) == "0000 0000 0000 0008"
    assert next(card_num) == "0000 0000 0000 0009"


def test_card_number_generator_lim():
    card_num_lim = card_number_generator(5, 6)
    assert next(card_num_lim) == "0000 0000 0000 0005"
    assert next(card_num_lim) == "0000 0000 0000 0006"


def test_card_number_generator_more_less():
    try:
        card_number_generator(6, 5)
    except StopIteration as e:
        assert e.StopIteration == "start must be less then stop"
