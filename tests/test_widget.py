from src.widget import mask_account_card, get_date
import pytest

@pytest.mark.parametrize('bank_name, name_card, expected_mask',[
    ('Visa Platinum', '7000792289606361', 'Visa Platinum 7000 79*******6361'),
    ('Maestro', '1596837868705199', 'Maestro 1596 83*******5199'),
    ('MasterCard', '7158300734726758', 'MasterCard 7158 30*******6758'),
    ('Visa Classic', '6831982476737658', 'Visa Classic 6831 98*******7658'),
    ('Visa Platinum', '8990922113665229', 'Visa Platinum 8990 92*******5229'),
    ('Visa Gold', '5999414228426353', 'Visa Gold 5999 41*******6353'),
])




def test_mask_account_card(bank_name: str, name_card: str, expected_mask: str):
    combined_argument = bank_name + ' ' + name_card
    result = mask_account_card(combined_argument)
    assert result == expected_mask


def test_get_date():
    pass


