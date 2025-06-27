def filter_by_state(list_dictionary: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий
     только те словари, у которых ключ state соответствует указанному значению.
    """
    new_list = [list for list in list_dictionary if list.get("state") == state]
    return new_list  # Возвращаем список словарей соответствующий значению.


def sort_by_date(list_1: list, descending: bool = True) -> list:
    """Функция sort_by_date, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать
    новый список, отсортированный по дате (date).
    """
    return sorted(list_1, key=lambda list_1: list_1.get("date", ""), reverse=descending)


# if __name__ == '__main__':
#     print(filter_by_state([
#         {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
#     ]))
#
# if __name__ == '__main__':
#     print(sort_by_date([
#         {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
#     ]))
