def filter_by_state(transactions: list, state: str = 'EXECUTED') -> list:
    new_transactions = []
    for transaction in transactions:
        if transaction.get("state") == state:
            new_transactions.append(transaction)
    return new_transactions


def sort_by_date(transactions: list, reverse: bool = False) -> list:
    new_transactions = sorted(transactions, key=lambda x: x.get("date"), reverse=reverse)
    return new_transactions
