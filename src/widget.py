from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(account_card: str) -> str:
    """
    Обрабатывает информацию о картах и счетах, и выводит маскировку.
    """
    parts = account_card.split()
    type_account_card = " ".join(parts[:-1])
    number = parts[-1]
    return account_card

    if "счет" in account_card.lower():
        number_card = account_card[-10:]
        masked_card = get_mask_account(number_card)
        return f"Счет {masked_card}"
    else:
        name_card = account_card[-6:]
        masked = get_mask_card_number(name_card)
        bank_name = account_card[:-6]
        return f"{bank_name} {masked}"


def get_date(data_number: str) -> str:
    '''
    Вывести дату в формате "ДД.ММ.ГГГГ"
    '''
    correct = data_number[8:10] + "." + data_number[5:7] + "." + data_number[:4]
    return correct


if __name__ == '__main__':
    print(get_mask_card_number('Visa Platinum 7000792289606361'))

    print(get_mask_account('Cчет 73654108430135874305'))

    print(get_date("1981-11-17T00:00:01.136347"))
