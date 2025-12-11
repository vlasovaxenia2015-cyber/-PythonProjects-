from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date

print(get_mask_account(11112222333344445555))
print(get_mask_card_number(1111222233334444))
print(mask_account_card('Visa Platinum 7000792289606361'))
print(mask_account_card('Cчет  35383033474447895560'))
print(get_date("1981-11-17T00:00:01.136347"))
transaction = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
print(filter_by_state(transaction))
print(sort_by_date(transaction))
