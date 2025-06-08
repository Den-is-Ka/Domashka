def get_mask_card_number(card_number: str) -> str:
    """
    Маскируем номер карты, оставляем последние 4 цифры.
    """
    mask_card_number = card_number[:4] + ' ' + card_number[4:6] + '*******' + card_number[-4:]
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """
    Маскируем номер счета.
    """
    mask_account = '**' + account_number[-4:]
    return mask_account


if __name__ == '__main__':
    print(get_mask_card_number('7000792289606361'))

    print(get_mask_account('73654108430135874305'))
