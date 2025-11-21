from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

print(get_mask_account(11112222333344445555))
print(get_mask_card_number(1111222233334444))
print(mask_account_card('Visa Platinum 7000792289606361'))
print(mask_account_card('Cчет  35383033474447895560'))
print(get_date("1981-11-17T00:00:01.136347"))
