import pytest
from src.generators import filter_by_currency, card_number_generator, transaction_descriptions


def test_filter_by_currency(transactions):
    currency = "USD"
    result = list(filter_by_currency(transactions, currency))
    assert len(result) == 1
    assert result[0]["description"] == "Payment 1"


def test_card_number_generator():
    result = list(card_number_generator(1, 5))
    assert len(result) == 5
    assert result[4] == "0000 0000 0000 0005"


def test_transaction_descriptions(transactions):
    result = list(transaction_descriptions(transactions))
    assert result == ["Payment 1", "Payment 2"]


def test_filter_by_currency_empty():
    transactions = []
    result = list(filter_by_currency(transactions, "USD"))
    assert result == []


def test_transaction_descriptions_empty():
    transactions = []
    result = list(transaction_descriptions(transactions))
    assert result == []


def test_filter_by_currency_stop_iteration():
    gen = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(gen)


