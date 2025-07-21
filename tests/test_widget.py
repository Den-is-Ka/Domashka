import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "bank_name, name_card, expected_mask",
    [
        ("Visa Platinum", "7000792289606361", "Visa Platinum 7000 79*******6361"),
        ("Счет", "73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(bank_name: str, name_card: str, expected_mask: str) -> None:
    combined_argument = bank_name + " " + name_card
    result = mask_account_card(combined_argument)
    assert result == expected_mask


@pytest.mark.parametrize("data_num, expected", [("1981-11-17T00:00:01.136347", "17.11.1981")])
def test_get_date(data_num: str, expected: str) -> None:
    assert get_date(data_num) == expected
