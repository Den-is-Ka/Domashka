from typing import Generator, Iterator


def filter_by_currency(transactions_list: list[dict], currency_code: str) -> Iterator:
    """
    Фильтрует список транзакций по валюте.
    """
    return (
        filter(
            lambda x: x.get("operationAmount", {}).get("currency", {}).get("code") == currency_code, transactions_list
        )
    )


def transaction_descriptions(transactions_list: list[dict]) -> Iterator:
    # пример реализации генератора
    for t in transactions_list:
        yield t["description"]


def card_number_generator(start: int, end: int) -> Generator:
    """
    Генератор номеров банковских карт в диапазоне от start до end включительно.
    Номера формата XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        # Форматируем число с ведущими нулями до 16 цифр
        card_number = f"{number:016d}"
        # Разбиваем на группы по 4 цифры
        formatted_number = " ".join([card_number[i : i + 4] for i in range(0, 16, 4)])
        yield formatted_number

# # Пример использования:
# for card_number in card_number_generator(1, 5):
#     print(card_number)


# if __name__ == '__main__':
#     # фильтруем по валюте USD
#     usd_transactions = filter_by_currency(transactions, 'USD')
#
#     # выводим результат
#     print("Транзакции в USD:")
#     for x in usd_transactions:
#         print(x)
#
# if __name__ == '__main__':
#     descriptions = transaction_descriptions(transactions, None)
#     # Простая проверка: вызываем next() несколько раз
#     try:
#         print(next(descriptions))
#         print(next(descriptions))
#         print(next(descriptions))
#         print(next(descriptions))
#         print(next(descriptions))
#         # если больше, то добавляем вызовы
#     except StopIteration:
#         print("Генератор завершился раньше времени")
#
# if __name__ == '__main__':
#     # Здесь указываем диапазон
#     start_value = 1
#     end_value = 5
#
#     # Запускаем генератор и выводим результаты
#     for card_number in card_number_generator(start_value, end_value):
#         print(card_number)
