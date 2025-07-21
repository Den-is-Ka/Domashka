from logger import logger


def get_mask_card_number(card_number: str) -> str:

    logger.info(f"Маскируем номер карты: {card_number}")
    """
    Маскируем номер карты, оставляем последние 4 цифры.
    """
    mask_card_number = card_number[:4] + " " + card_number[4:6] + "*******" + card_number[-4:]
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    logger.info(f"Маскируем номер счета: {account_number}")
    """
    Маскируем номер счета.
    """
    mask_account = "**" + account_number[-4:]
    return mask_account
