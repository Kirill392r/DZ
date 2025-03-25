import re


def filter_operations(operations: list[dict], search_string: str) -> list[dict]:
    """Фильтрует операции, оставляя те, где хотя бы одно поле (включая вложенные)содержит искомую строку. Поиск регистрозависимый."""
    pattern = re.compile(re.escape(search_string))
    result = []

    for op in operations:
        stack = [op]
        found = False

        while stack and not found:
            data = stack.pop()
            if isinstance(data, dict):
                for value in data.values():
                    if isinstance(value, (dict, list)):
                        stack.append(value)
                    elif isinstance(value, str) and pattern.search(value):
                        found = True
                        break
            elif isinstance(data, list):
                for item in data:
                    stack.append(item)

        if found:
            result.append(op)

    return result


def count_operations_by_category(operations: list[dict], categories: str) -> dict:
    """Подсчитывает количество операций по заданным категориям."""
    category_counts = {category: 0 for category in categories}

    for operation in operations:
        description = operation.get('description', '').lower()
        for category in categories:
            if not category:
                continue
            if category.lower() in description:
                category_counts[category] += 1

    return category_counts
