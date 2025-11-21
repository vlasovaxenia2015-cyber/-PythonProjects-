from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """  Обрабатывает информацию о картах и счетах, и выводит маскировку. """
    if "счет" in account_card.lower():
        number_card = account_card[-10:]
        masked_card = get_mask_account(number_card)
        return f"Счет {masked_card}"
    else:
        name_card = account_card[-16:]
        masked = get_mask_card_number(name_card)
        bank_name = account_card[:-16]
    return f"{bank_name} {masked}"


def get_date(data_number: str) -> str:
    """   Вывести дату в формате "ДД.ММ.ГГГГ"  """
    correct = data_number[8:10] + "." + data_number[5:7] + "." + data_number[:4]
    return correct
