from collections.abc import Iterable, Iterator
from typing import Dict, Any


def filter_by_currency(
    transactions: Iterable[Dict[str, Any]],
    currency: str,
) -> Iterator[Dict[str, Any]]:
    """
    Генератор, по очереди выдающий транзакции с указанной валютой.

    :param transactions: Iterable словарей транзакций, ожидается ключ 'currency'.
    :param currency: Код валюты, например 'USD'.
    :return: Итератор (generator) по транзакциям с указанной валютой.
    """
    for tx in transactions:
        if tx.get("currency") == currency:
            yield tx
