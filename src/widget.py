from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Обрабатывает информацию о картах и счетах, и выводит маскировку.
    """
    if "счет" in account_card.lower():
        number_card = account_card[-20:]
        mask_account = get_mask_account(number_card)
        return f"Счет {mask_account}"

    else:
        name_card = account_card[-16:]
        mask_account = get_mask_card_number(name_card)
        bank_name = account_card[:-16]
    return f"{bank_name}{mask_account}"


def get_date(data_num: str) -> str:
    """
    Вывести дату в формате "ДД.ММ.ГГГГ"
    """
    correct = data_num[8:10] + "." + data_num[5:7] + "." + data_num[:4]
    return correct
