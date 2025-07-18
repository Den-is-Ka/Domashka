from config import PATH_CSV, PATH_XLSX
from src.decorators import hello
from src.transactions_file import get_transactions_file_csv, get_transactions_file_xlsx
from src.utils import convert_transaction_rub, load_transactions_json
from tests.test_external_api import unittest
import os
import pandas as pd
import json
import csv
from datetime import datetime
from openpyxl import load_workbook
from src.operations import (
    filter_operations_by_description,
    count_operations_by_category
)

ROOT_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(ROOT_DIR, 'data')
PATH_JSON = os.path.join(DATA_DIR, 'operations.json')
PATH_CSV = os.path.join(DATA_DIR, 'transactions.csv')
PATH_XLSX = os.path.join(DATA_DIR, 'transactions_excel.xlsx')

VALID_STATUS = ["EXECUTED", "CANCELED", "PENDING"]

# if __name__ == "__main__":
#     hello()


# if __name__ == '__main__':
#     transactions = load_transactions_json('data/operations.json')
#     print(transactions)
#     print(convert_transaction_rub(transactions[3]))


# if __name__ == '__main__':
#     unittest.main()


# if __name__ == '__main__':
#     csv_transactions = get_transactions_file_csv(PATH_CSV)
#     print(csv_transactions)
#     xlsx_transactions = get_transactions_file_xlsx(PATH_XLSX)
#     print(xlsx_transactions)


def read_from_json(path):
    """
        Читает список операций из JSON-файла и преобразует в плоский формат, пригодный для Excel/CSV.
        Структура полей: id, state, date, amount, currency_name, currency_code, from, to, description.
        """
    with open(path, encoding='utf-8') as f:
        raw = json.load(f)
    # Преобразуем вложенную структуру
    flat = []
    for op in raw:
        amt_info = op.get('operationAmount', {})
        cur_info = amt_info.get('currency', {})
        flat.append({
            'id': op.get('id'),
            'state': op.get('state'),
            'date': op.get('date'),
            'amount': amt_info.get('amount'),
            'currency_name': cur_info.get('name'),
            'currency_code': cur_info.get('code'),
            'from': op.get('from'),
            'to': op.get('to'),
            'description': op.get('description'),
        })
    return flat


def read_from_csv(path):
    with open(path, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        return list(reader)


def read_from_xlsx(path):
    """Читает список операций из XLSX-файла с помощью pandas.read_excel."""
    # try:
    #     import pandas as pd
    # except ImportError:
    #     print("Ошибка: модуль pandas не установлен.")
    #     return []
    try:
        df = pd.read_excel(path, engine='openpyxl')
    except Exception as e:
        print(f"Ошибка при чтении Excel-файла '{path}': {e}")
        return []
    # Преобразуем DataFrame в словари
    return df.to_dict(orient='records')


def parse_date(date_str):
    """Парсим дату и возвращает datetime."""
    try:
        return datetime.fromisoformat(date_str.replace('Z', '+00:00'))
    except ValueError:
        return datetime.strptime(date_str, '%d.%m.%Y')


def main():
    print("Привет! Выберите формат файла: 1-JSON, 2-CSV, 3-XLSX")
    choice = input().strip()

    # Определяем путь к файлу из конфига
    if choice == '1':
        path = PATH_JSON
        ops = read_from_json(path)
        print(f"Выбран JSON-файл: {path}")
    elif choice == '2':
        path = PATH_CSV
        ops = read_from_csv(path)
        print(f"Выбран CSV-файл: {path}")
    elif choice == '3':
        path = PATH_XLSX
        ops = read_from_xlsx(path)
        print(f"Выбран XLSX-файл: {path}")
    else:
        print("Некорректный выбор формата.")
        return

    # Фильтр по статусу
    status = input(f"Введите статус ({', '.join(VALID_STATUS)}): ").upper()
    while status not in VALID_STATUS:
        status = input("Неверный статус. Повторите: ").upper()
    ops = [o for o in ops if str(o.get('state', '')).upper() == status]

    # Сортируем по дате
    if input("Сортировать по дате? Да(1)/Нет: ").lower().startswith('1'):
        asc = input("По возрастанию? Да(1)/Нет: ").lower().startswith('1')
        ops.sort(key=lambda o: parse_date(o.get('date', '')), reverse=not asc)

    # Фильтр по рублям
    if input("Только рублевые? Да(1)/Нет: ").lower().startswith('1'):
        ops = [o for o in ops if o.get('currency') == 'RUB']

    # Фильтр по описанию
    if input("Фильтровать по слову в описании? Да(1)/Нет: ").lower().startswith('1'):
        term = input("Введите слово: ")
        ops = filter_operations_by_description(ops, term)

    # Вывод итогов
    print(f"Найдено {len(ops)} операций")
    for o in ops:
        d = parse_date(o.get('date', '')).strftime('%d.%m.%Y')
        print(f"{d} {o.get('description')} - {o.get('amount')} {o.get('currency_name')} {o.get('currency_code')} {o.get('from')} {o.get('to')}")


if __name__ == '__main__':
    main()