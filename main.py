from config import PATH_CSV, PATH_XLSX
from src.decorators import hello
from src.transactions_file import get_transactions_file_csv, get_transactions_file_xlsx
from src.utils import convert_transaction_rub, load_transactions_json
from tests.test_external_api import unittest

if __name__ == "__main__":
    hello()


if __name__ == '__main__':
    transactions = load_transactions_json('data/operations.json')
    print(transactions)
    print(convert_transaction_rub(transactions[3]))


if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    csv_transactions = get_transactions_file_csv(PATH_CSV)
    print(csv_transactions)
    xlsx_transactions = get_transactions_file_xlsx(PATH_XLSX)
    print(xlsx_transactions)
