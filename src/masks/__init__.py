def get_mask_card_number(card_number: str) -> str:
    """
    Маскируем номер банковской карты, показываем последние 4 цифры.

    Args:
        card_number (str): Номер карты (должен состоять только из цифр).

    Returns:
        str: Примерный вид карты '**** **** **** 1234'.
    """
    # Удаляем лишние символы
    digits = "".join(filter(str.isdigit, card_number))

    if len(digits) < 4:
        return "*" * len(digits)

    masked_part = "*" * (len(digits) - 4)
    last_four = digits[-4:]

    masked_number = f"{masked_part}{last_four}"

    # Ставим пробел каждые 4 символа для удобства чтения.
    formatted = " ".join([
        masked_number[i: i + 4] for i in range(0, len(masked_number), 4)
    ])
    return formatted


def get_mask_account(account_number: str) -> str:
    """
    Маскируем номер банковского счета, показываем последние 4 цифры.

    Args:
        account_number (str): Номер счета.

    Returns:
        str: Примерный вид счета '**** **** **** 1234'.
    """
    # Аналогично маскировке номера карты
    digits = "".join(filter(str.isdigit, account_number))

    if len(digits) < 4:
        return "*" * len(digits)

    masked_part = "*" * (len(digits) - 4)
    last_four = digits[-4:]

    masked_number = f"{masked_part}{last_four}"

    # Форматируем для читаемости
    formatted = " ".join([
        masked_number[i: i + 4] for i in range(0, len(masked_number), 4)
    ])

    return formatted
