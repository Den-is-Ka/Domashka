import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, mask_card_number", [
    # карта (длина не менее 10 символов)
    ("4111111111111111", "4111 11*******1111"),
    ("1234567890", "1234 56*******7890"),
    # Очень короткая строка
    ("12345", "1234 5*******2345"),  # В этом случае тоже возможна некорректность
])
def test_get_mask_card_number(card_number: str, mask_card_number: str) -> None:
    result = get_mask_card_number(card_number)
    assert result == mask_card_number


@pytest.mark.parametrize("account_number, mask_account", [
    # карта (длина не менее 10 символов)
    ("7000792289606361", "**6361"),
])
def test_get_mask_account(account_number: str, mask_account: str) -> str:
    result = get_mask_account(account_number)
    assert result == mask_account
