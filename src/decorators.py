from functools import wraps

from config import ROOT_DIR


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwarks):
            # Логируем старт
            message = ""
            try:
                func(*args, **kwarks) # вызов исходника
                message = f"Стартуем функцию {func.__name__} завершилась."
            except Exception as e:
                message = f"{func.__name__} тип ошибки {type(e)} с аргументами {args}, {kwarks}"
            finally:
                if filename:
                    with open(f"{ROOT_DIR}/logs/{filename}", "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)

        return wrapper
    return decorator


def hello():
    return None
