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


def card_number_generator(
        start: int,
        end: int
) -> Iterator[str]:

    """
    Генератор номеров банковских карт от start до end в формате XXXX XXXX XXXX XXXX.
    """
    for num in range(start, end + 1):
        # Преобразуем номер карты в строку из 16 цифр
        card_number = f"{num:016d}"
        # Разбиваем на блоки по 4 цифры для правильного отображения
        new_card_number = " ".join([card_number[i:i + 4] for i in range(0, 16, 4)])
        yield new_card_number


def transaction_descriptions(
        transactions: Iterable[Dict[str, Any]],
) -> Iterator[Dict[str, Any]]:
    for tx in transactions:
        yield tx.get('description')
