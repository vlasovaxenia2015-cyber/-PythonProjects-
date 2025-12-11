from src.masks import get_mask_account, get_mask_card_number


def test_card_masks(card_number):
    assert get_mask_card_number(card_number) == "1234 56** **** 3456"


def test_acc_masks(acc_number):
    assert get_mask_account(acc_number) == "**2345"
