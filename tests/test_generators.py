import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.mark.parametrize(
    "list_input_usd, expected",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {
                        "amount": "9824.07",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {
                        "amount": "79114.93",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {"name": "USD", "code": "USD"},
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
        ),
    ],
)
def test_filter_by_currency_usd(list_input_usd, expected):
    usd_transactions = filter_by_currency(list_input_usd, "USD")
    assert next(usd_transactions) == expected


@pytest.mark.parametrize(
    "list_input, expected",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {
                        "amount": "9824.07",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {
                        "amount": "79114.93",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            [{}],
        ),
    ],
)
def test_filter_by_currency_empty_cur(list_input, expected):
    with pytest.raises(ValueError, match="enter currency like USD"):
        list(filter_by_currency(list_input, ""))


@pytest.mark.parametrize(
    "list_input, expected",
    [
        (
            [{}],
            [{}],
        ),
    ],
)
def test_filter_by_currency_empty_trans(list_input, expected):
    with pytest.raises(ValueError, match="enter transaction and currency"):
        list(filter_by_currency([{}], ""))


@pytest.mark.parametrize(
    "list_input, expected",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {
                        "amount": "9824.07",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {
                        "amount": "79114.93",
                        "currency": {"name": "EUR", "code": "EUR"},
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {"name": "EUR", "code": "EUR"},
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            },
        ),
    ],
)
def test_filter_by_currency_eur(list_input, expected):
    usd_transactions = filter_by_currency(list_input, "EUR")
    assert next(usd_transactions) == expected


def test_transaction_descriptions():
    transactions_test = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]
    descriptions = transaction_descriptions(transactions_test)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"


def test_card_number_generator():
    card_num = card_number_generator(5, 11)
    assert next(card_num) == "0000 0000 0000 0005"
    assert next(card_num) == "0000 0000 0000 0006"
    assert next(card_num) == "0000 0000 0000 0007"
    assert next(card_num) == "0000 0000 0000 0008"
    assert next(card_num) == "0000 0000 0000 0009"


def test_card_number_generator_lim():
    card_num_lim = card_number_generator(9999999999999998, 9999999999999999)
    assert next(card_num_lim) == "9999 9999 9999 9998"
    assert next(card_num_lim) == "9999 9999 9999 9999"


def test_card_number_generator_more_less():
    with pytest.raises(ValueError, match="start must be less than stop"):
        list(card_number_generator(6, 5))
