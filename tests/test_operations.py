import unittest
from src.operations import filter_operations_by_description, count_operations_by_category


class TestOperationsUtils(unittest.TestCase):
    # Пример операций для тестов
    OPERATIONS = [
        {'description': 'Перевод организации'},
        {'description': 'Перевод с карты на карту'},
        {'description': 'Открытие вклада'},
        {'description': 'REFUND PROCESS'},
    ]

    def test_filter_basic(self):
        # Фильтрация по слову 'перевод'
        result = filter_operations_by_description(
            TestOperationsUtils.OPERATIONS, 'перевод'
        )
        # Должно вернуть только два перевода
        descriptions = [o['description'] for o in result]
        self.assertCountEqual(
            descriptions,
            ['Перевод организации', 'Перевод с карты на карту']
        )

    def test_count_basic(self):
        # Подсчет категорий: перевод, вклад и refund
        counts = count_operations_by_category(
            TestOperationsUtils.OPERATIONS,
            ['перевод', 'вклад', 'refund']
        )
        # Ожидаемые результаты
        expected = {'перевод': 2, 'вклад': 1, 'refund': 1}
        self.assertEqual(counts, expected)


if __name__ == '__main__':
    unittest.main()
