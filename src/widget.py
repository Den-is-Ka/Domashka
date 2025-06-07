from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """обрабатывает информацию о картах и счетах, выводит замаскированный номер"""
    parts = account_card.split()
    type_account_card = " ".join(parts[:-1])
    number = parts[-1]
    return account_card

    if "счет" in account_card.lower():
        number_card = account_card[-20:]

        masked_card = get_mask_account(number_card)
        return f"Счет {masked_card}"

    else:
        name_card = account_card[-16:]
        masked = get_mask_card_number(name_card)
        name_bank = account_card[:-16]
        return f"{name_bank} {masked}"

def get_date():
    pass


if __name__ == '__main__':
    print(get_mask_card_number('Visa Platinum 7000792289606361'))

    print(get_mask_account('Cчет 73654108430135874305'))