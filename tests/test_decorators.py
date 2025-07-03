import os
from src.decorators import log, hello

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_DIR = os.path.join(ROOT_DIR, "..", "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

''''
Путь к лог файлу
'''
TEST_LOG_FILE = "Сюда пиши да.txt"
'''Для очистки лог-файла раскоментировать блок, или очистить файл ручками.
'''
# @pytest.fixture(autouse=True)
# def подготовить_логи():
#     log_path = os.path.join(LOGS_DIR, TEST_LOG_FILE)
#     with open(log_path, 'w', encoding='utf-8') as f:
#         pass

def test_логирование_в_файл():
    @log(filename=TEST_LOG_FILE)
    def test_func():
        return "ok"

    test_func()  # Вызов функции

    log_path = os.path.join(LOGS_DIR, TEST_LOG_FILE)
    with open(log_path, 'r', encoding='utf-8') as f:
        content = f.read()

    assert "завершилась" in content

def test_логирование_в_консоль(capsys):
    @log()
    def test_func():
        return "ok"

    test_func()

    вывод = capsys.readouterr()
    assert "завершилась" in вывод.out


def test_обработка_исключения():
    @log(filename=TEST_LOG_FILE)
    def func_with_error():
        raise ValueError("ошибка")

    func_with_error()

    # Проверка лога
    log_path = os.path.join(LOGS_DIR, TEST_LOG_FILE)
    with open(log_path, 'r', encoding='utf-8') as f:
        content = f.read()

    assert "тип ошибки" in content or "ValueError" in content

def test_декоратор_без_файла():
    @log()
    def hello():
        return "привет"

    # Вызов функции (результат не проверяем)
    hello()

    # Проверяем лог на наличие сообщения
    log_path = os.path.join(LOGS_DIR, TEST_LOG_FILE)
    with open(log_path, 'r', encoding='utf-8') as f:
        content = f.read()

    assert "завершилась" in content or "привет" not in content

# def test_x() -> None:
#     """Документация"""





# def log(filename=None):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwarks):
#             # Логируем старт
#             message = ""
#             try:
#                 func(*args, **kwarks) # вызов исходника
#                 message = f"Стартуем функцию {func.__name__} завершилась."
#             except Exception as e:
#                 message = f"{func.__name__} тип ошибки {type(e)} с аргументами {args}, {kwarks}"
#             finally:
#                 if filename:
#                     with open(f"{ROOT_DIR}/logs/{filename}", "a", encoding="utf-8") as f:
#                         f.write(message + "\n")
#                 else:
#                     print(message)
#
#         return wrapper
#     return decorator
#
# @log(filename="Сюда пиши да.txt")
# @log()
# def hello():
#     print("Hi!")