import re


def filter_operations_by_description(operations, search_str):
    """
    Возвращает список операций, в описании которых встречается search_str (без учета регистра).
    operations: список словарей с ключом 'description'.
    search_str: строка для поиска.
    """
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    return [op for op in operations if pattern.search(op.get('description', ''))]


def count_operations_by_category(operations, categories):
    """
    Подсчитывает, сколько операций относится к каждой категории.
    operations: список словарей с ключом 'description'.
    categories: список строк (названия категорий).
    Возвращает словарь {category: count}.
    """
    counts = {cat: 0 for cat in categories}
    for op in operations:
        desc = op.get('description', '')
        for cat in categories:
            if re.search(re.escape(cat), desc, re.IGNORECASE):
                counts[cat] += 1
    return counts
