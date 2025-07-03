import os

from src.decorators import log

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_DIR = os.path.join(ROOT_DIR, "..", "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

''''
Путь к лог файлу
'''
TEST_LOG_FILE = "Сюда пиши да.txt"
'''
Для очистки лог-файла расскоментировать блок, или очистить файл ручками.
'''
# @pytest.fixture(autouse=True)
# def prepare_logs():
#     log_path = os.path.join(LOGS_DIR, TEST_LOG_FILE)
#     with open(log_path, 'w', encoding='utf-8') as f:
#         pass


def test_logging_to_file():
    """
    Проверяет, что декоратор записывает логи в файл
    """
    @log(filename=TEST_LOG_FILE)
    def test_func():
        return "ok"

    test_func()  # Вызов функции

    log_path = os.path.join(LOGS_DIR, TEST_LOG_FILE)
    with open(log_path, 'r', encoding='utf-8') as f:
        content = f.read()
    assert "завершилась" in content


def test_logging_to_console(capsys):
    """
    Проверка, вывода лога в консоль
    """
    @log()
    def test_func():
        return "ok"

    test_func()

    вывод = capsys.readouterr()
    assert "завершилась" in вывод.out


def test_exception_handling():
    """
    Проверяем, что декоратор ловит и записывает ошибки в лог
    """
    @log(filename=TEST_LOG_FILE)
    def func_with_error():
        raise ValueError("ошибка")

    func_with_error()

    # Проверка лога
    log_path = os.path.join(LOGS_DIR, TEST_LOG_FILE)
    with open(log_path, 'r', encoding='utf-8') as f:
        content = f.read()

    assert "тип ошибки" in content or "ValueError" in content


def test_decorator_without_file():
    """
    Проверяеv работу декоратора без указания файла для логов
    """
    @log()
    def hello():
        return "привет"

    hello()
    # Проверяем лог на наличие сообщения
    log_path = os.path.join(LOGS_DIR, TEST_LOG_FILE)
    with open(log_path, 'r', encoding='utf-8') as f:
        content = f.read()
    assert "завершилась" in content or "привет" not in content
