from src.decorators import hello

from src.utils import load_transactions_json, convert_transaction_rub
if __name__ == "__main__":
    hello()


if __name__ == '__main__':

    transactions = load_transactions_json('data/operations.json')
    print(transactions)

    print (convert_transaction_rub(transactions[3]))
