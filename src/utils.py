import json
import os
from src.external_api import get_exchange_rate

def load_transactions_json(file_path):

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)


    except (json.JSONDecodeError, FileNotFoundError):
        return []


def convert_transaction_rub(transaction):
    amount = transaction.get('operationAmount').get('amount')
    currency = transaction.get('operationAmount').get('currency').get("code")

    if currency == 'RUB':
        return amount
    elif currency in ['USD', 'EUR']:
        result = get_exchange_rate(currency, amount)
        return result
    else:
        raise ValueError(f"Неизвестная валюта: {currency}")

if __name__ == '__main__':

    transactions = load_transactions_json('../data/operations.json')
    print(transactions)

    print (convert_transaction_rub(transactions[3]))
