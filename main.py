# import pandas as pd
import json

# from tests.test_external_api import unittest
import os
from typing import Any, Dict, List

from config import PATH_CSV, PATH_JSON, PATH_XLSX
from src.decorators import hello
from src.operations import filter_operations_by_description
from src.processing import filter_by_state, sort_by_date
from src.transactions_file import get_transactions_file_csv, get_transactions_file_xlsx
from src.utils import convert_transaction_rub, load_transactions_json
from src.widget import get_date, mask_account_card

ROOT_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(ROOT_DIR, 'data')

VALID_STATUS = ["EXECUTED", "CANCELED", "PENDING"]

if __name__ == "__main__":
    hello()


if __name__ == '__main__':
    transactions = load_transactions_json('data/operations.json')
    print(transactions)
    print(convert_transaction_rub(transactions[3]))


# if __name__ == '__main__':
#     unittest.main()


if __name__ == '__main__':
    csv_transactions = get_transactions_file_csv(PATH_CSV)
    print(csv_transactions)
    xlsx_transactions = get_transactions_file_xlsx(PATH_XLSX)
    print(xlsx_transactions)


#

def get_transactions_file_json(full_path):
    """ Загружаем данные из JSON-файла и преобразуем
    в формат для Exel/CSV. """

    # Загрузка данных из JSON-файла
    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # Преобразование
    file_conversion = []
    for operation in data:
        file_conversion.append({
            'id': operation.get('id'),
            'state': operation.get('state'),
            'date': operation.get('date'),
            'amount': operation.get('operationAmount', {}).get('amount', ''),
            'currency_name': operation.get('operationAmount', {}).get('currency', {}).get('name', ''),
            'currency_code': operation.get('operationAmount', {}).get('currency', {}).get('code', ''),
            'from': operation.get('from', ''),
            'to': operation.get('to', ''),
            'description': operation.get('description')
        })
        # if not operation:  # Пропуск пустых операций
        #     continue
    return file_conversion


def get_user_choice(prompt: str, valid_choices: List[str]) -> str:
    """Получаем выбор пользователя """
    while True:
        user_input = input(f"{prompt}\nПользователь: ").strip().lower()
        for choice in valid_choices:
            if user_input == choice.lower():
                return choice
        print(f"Некорректный ввод. Пожалуйста, выберите один из вариантов: {', '.join(valid_choices)}")


def filter_rub_transactions(transactions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Фильтруем только рублевые транзакции."""
    return [t for t in transactions if t.get("currency_code") == "RUB"]


def print_transaction(transaction: Dict[str, Any]) -> None:
    """Печатаем информацию о транзакции в нужном формате."""
    date = get_date(transaction["date"])
    description = transaction["description"]

    # Обработка from и to
    from_account = mask_account_card(transaction["from"]) if "from" in transaction and isinstance(transaction["from"], str) else "Не указано"
    to_account = mask_account_card(transaction["to"]) if "to" in transaction and isinstance(transaction["to"], str) else "Не указано"

    # Получаем сумму и валюту
    amount = transaction["amount"]
    currency = transaction["currency_name"]

    # Формируем строку перевода
    transfer_line = ""
    if from_account != "Не указано" and to_account != "Не указано":
        transfer_line = f"{from_account} -> {to_account}"
    elif to_account != "Не указано":
        transfer_line = f"{to_account}"

    # Печатаем информацию о транзакции
    print(f"{date} {description}")
    if transfer_line:
        print(transfer_line)
    print(f"Сумма: {amount} {currency}\n")


def main():
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print('Выберите необходимый пункт меню:\n'
          '1. Получить информацию о транзакциях из JSON-файла \n'
          '2. Получить информацию о транзакциях из CSV-файла \n'
          '3. Получить информацию о транзакциях из XLSX-файла \n')

    # Получаем выбор пользователя
    file_choice = input("Пользователь: ").strip()

    # Определяем путь к файлу
    transactions = []
    if file_choice == "1":
        print("\nПрограмма: Для обработки выбран JSON-файл.\n")
        transactions = get_transactions_file_json(PATH_JSON)
    elif file_choice == "2":
        print("\nПрограмма: Для обработки выбран CSV-файл.\n")
        transactions = get_transactions_file_csv(PATH_CSV)
    elif file_choice == "3":
        print("\nПрограмма: Для обработки выбран XLSX-файл.\n")
        transactions = get_transactions_file_xlsx(PATH_XLSX)
    else:
        print("Неверный выбор. Завершение программы.")
        return

    if not transactions:
        print("Не удалось загрузить транзакции. Файл пуст или имеет неверный формат.")
        return

    # Фильтруем по статусу
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("Программа: Введите статус, по которому необходимо выполнить фильтрацию. \n"
              f"Доступные для фильтровки статусы: {', '.join(valid_statuses)} \n")
        status = input("Пользователь: ").strip().upper()

        if status in valid_statuses:
            print(f'\nПрограмма: Операции отфильтрованы по статусу "{status}" \n')
            filtered_transactions = filter_by_state(transactions, status)
            break
        else:
            print(f'\nПрограмма: Статус операции "{status}" недоступен. \n')

    if not filtered_transactions:
        print("Не найдено ни одной транзакции с указанным статусом.")
        return

    # Сортируем по дате
    sort_choice = get_user_choice("Программа: Отсортировать операции по дате? (Да/Нет) \n", ["Да", "Нет"])
    if sort_choice == "Да":
        order_choice = get_user_choice(
            "\nПрограмма: Отсортировать по возрастанию или по убыванию? (по возрастанию/по убыванию): \n",
            ["по возрастанию", "по убыванию"])
        reverse_sort = order_choice == "по убыванию"
        filtered_transactions = sort_by_date(filtered_transactions, reverse_sort)

    # Фильтруем по валюте
    currency_choice = get_user_choice("\nВыводить только рублевые транзакции? (Да/Нет) \n", ["Да", "Нет"])
    if currency_choice == "Да":
        filtered_transactions = filter_rub_transactions(filtered_transactions)

    # Фильтруем по ключевому слову
    search_choice = get_user_choice("\nОтфильтровать список транзакций по определенному слову в описании? (Да/Нет) \n",
                                    ["Да", "Нет"])
    if search_choice == "Да":
        search_word = input("\nВведите слово для поиска в описании: ").strip()
        filtered_transactions = filter_operations_by_description(filtered_transactions, search_word)

    # Выводим результат
    print("\nРаспечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}\n")

    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        for transaction in filtered_transactions:
            print_transaction(transaction)


if __name__ == '__main__':
    main()
