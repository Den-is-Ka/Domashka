from pathlib import Path
from typing import Any, Dict, List, Union
import pandas as pd
from config import PATH_CSV, PATH_XLSX


def get_transactions_file_csv(file_csv: Union[str, Path]) -> List[Dict[str, Any]]:
    """Функция для считывания финансовых операций из CSV.
    Возвращает список словарей с транзакцией."""

    try:
        with open(file_csv, encoding="utf-8") as file:
            excel_transaction = pd.read_csv(file, delimiter=";")
            return excel_transaction.to_dict("records")
    except FileNotFoundError:
        print(f"Ошибка: файл {file_csv} не найден! ")
        return []
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
        return []


def get_transactions_file_xlsx(file_xlsx: Union[str, Path]) -> List[Dict[str, Any]]:
    """Функция для считывания финансовых операций из Excel.
    Возвращает список словарей с транзакцией."""

    try:
        with open(file_xlsx, encoding="utf-8"):
            excel_transaction = pd.read_excel(file_xlsx)
            return excel_transaction.to_dict("records")
    except FileNotFoundError:
        print(f"Ошибка: файл {file_xlsx} не найден! ")
        return []
    except Exception as e:
        print(f"Ошибка при чтении XLSX: {e}")
        return []


if __name__ == '__main__':
    csv_transactions = get_transactions_file_csv(PATH_CSV)
    print(csv_transactions)
    xlsx_transactions = get_transactions_file_xlsx(PATH_XLSX)
    print(xlsx_transactions)
