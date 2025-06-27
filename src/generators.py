from typing import Any, Generator, Iterator, Literal

# from src.transaction_data import transactions


def filter_by_currency(transactions_list: list[dict], currency: Literal["USD", "RUB"]) -> Iterator[dict[Any, Any]]:
    """
    Возвращаем итератор.
    """
    for i in transactions_list:
        if i["operationAmount"]["currency"]["code"] == currency:
            yield i


def transaction_descriptions(transactions_list: list[dict], descriptions_code=None) -> Iterator[dict[Any, Any]]:
    # пример реализации генератора
    for i in transactions_list:
        yield i["description"]


def card_number_generator(start: int, end: int) -> Generator[str]:

    """
    Генератор номеров банковских карт в диапазоне от start до end включительно.
    Номера формата XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        # Форматируем число с ведущими нулями до 16 цифр
        card_number = f"{number:016d}"
        # Разбиваем на группы по 4 цифры
        formatted_number = " ".join([card_number[i: i + 4] for i in range(0, 16, 4)])
        yield formatted_number


# # Пример использования:
# for card_number in card_number_generator(1, 5):
#     print(card_number)
