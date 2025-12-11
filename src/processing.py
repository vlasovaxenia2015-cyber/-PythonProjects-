def filter_by_state(transactions: list, state: str = 'EXECUTED') -> list:
    """Функция для фильтрации списка транзакций по статусу"""
    new_transactions = []
    for transaction in transactions:
        if transaction.get("state") == state:
            new_transactions.append(transaction)
    return new_transactions


def sort_by_date(transactions: list, reverse: bool = False) -> list:
    """Функция для сортировки списка транзакций по дате"""
    new_transactions = sorted(transactions, key=lambda x: x.get("date"), reverse=reverse)
    return new_transactions

