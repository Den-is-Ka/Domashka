from src.decorators import hello
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
