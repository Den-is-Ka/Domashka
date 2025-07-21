import os

ROOT_DIR = os.path.dirname(__file__)  # корневой
DATA_DIR = os.path.join(ROOT_DIR, "data")
LOGS_DIR = os.path.join(ROOT_DIR, "logs")

PATH_JSON = os.path.join(DATA_DIR, "operations.json")  # путь к json
PATH_CSV = os.path.join(DATA_DIR, "transactions.csv")  # путь к csv
PATH_XLSX = os.path.join(DATA_DIR, "transactions_excel.xlsx")  # путь к xlsx
