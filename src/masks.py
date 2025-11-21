def get_mask_card_number(card_number: int | str) -> str:
    str_number = str(card_number)
    str_number = str_number.zfill(16)
    return f"{str_number[:4]} {str_number[4:6]}** **** {str_number[12:]}"


def get_mask_account(account_number: int | str) -> str:
    str_number = str(account_number)
    str_number = str_number.zfill(4)
    return f"**{str_number[-4:]}"
