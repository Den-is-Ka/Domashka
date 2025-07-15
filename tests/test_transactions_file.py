from typing import Any, Dict, List
from unittest.mock import patch

from config import PATH_CSV, PATH_XLSX
from src.transactions_file import get_transactions_file_csv, get_transactions_file_xlsx


# Тест чтения формата.cvs
def test_get_transactions_file_csv() -> None:
    with patch("pandas.read_csv") as mock_read:
        mock_read.return_value.to_dict.return_value = [
            {
                "id": 650703.0,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210.0,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
        result: List[Dict[str, Any]] = get_transactions_file_csv(PATH_CSV)
        assert result == [
            {
                "id": 650703.0,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210.0,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]


# Тест, если файл .csv не найден
def test_get_transactions_file_csv_missing() -> None:
    with patch("builtins.open", side_effect=FileNotFoundError):
        result: list = get_transactions_file_csv("")
        assert result == []  # Проверим, что вернулся пустой список


# Тест, при ошибке чтения файла .csv
@patch("src.transactions_file.pd.read_csv", side_effect=Exception("Ошибка при чтении CSV:"))
def test_csv_error(mock_read_csv: Any) -> None:
    """
    Проверяет реакцию функции на ошибку чтения CSV-файла.
    """
    result: list = get_transactions_file_csv(PATH_CSV)
    assert result == []  # 'Ожидался пустой список, получил {result}'


# Тест чтения .xlsx
def test_get_transactions_file_xlsx() -> None:
    with patch("pandas.read_excel") as mock_read:
        mock_read.return_value.to_dict.return_value = [
            {
                "id": 650703.0,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210.0,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
        result: List[Dict[str, Any]] = get_transactions_file_xlsx(PATH_XLSX)
        assert result == [
            {
                "id": 650703.0,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210.0,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]


# Тест, если файл .xlsx не найден
def test_get_transactions_file_xlsx_missing() -> None:
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        result: list = get_transactions_file_xlsx("no_file.xlsx")
        assert result == []  # Проверил, что вернулся пустой список


@patch("src.transactions_file.pd.read_excel", side_effect=Exception("Ошибка при чтении XLSX:"))
def test_xlsx_error(mock_read_xlsx: Any) -> None:
    """
    Проверяет реакцию функции на ошибку чтения XLSX-файла.
    """
    result: list = get_transactions_file_xlsx(PATH_XLSX)
    assert result == []  # 'Ожидали пустой список, получил {result}'
