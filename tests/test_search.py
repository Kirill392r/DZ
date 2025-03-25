import pytest

from src.search import filter_operations, count_operations_by_category


@pytest.mark.parametrize("search_string,expected_ids", [
    ("Перевод", [1, 2]),
    ("перевод", []),
    ("Visa", [2]),
    ("Счет", [1, 3]),

    ("руб.", [1, 3]),
    ("USD", [2]),
    ("10000", [1]),
    ("9876543210987654", [1, 2]),


    ("", [1, 2, 3]),
    ("несуществующийтекст", []),
])
def test_filter_operations_basic(sample_operations, search_string, expected_ids):
    """Тестирование базовой функциональности фильтрации"""
    result = filter_operations(sample_operations, search_string)
    assert [op["id"] for op in result] == expected_ids


def test_filter_operations_with_empty_input():
    """Тестирование с пустым списком операций"""
    assert filter_operations([], "Перевод") == []


def test_filter_operations_with_special_chars():
    """Тестирование поиска строк со специальными символами"""
    operations = [{"id": 1, "desc": "Payment (invoice #123)"}]
    assert filter_operations(operations, "(invoice #123)")[0]["id"] == 1


def test_filter_operations_with_nested_lists():
    """Тестирование поиска по вложенным спискам"""
    operations = [
        {
            "id": 1,
            "items": [
                {"name": "item1", "value": "A"},
                {"name": "item2", "value": "B"}
            ]
        },
        {
            "id": 2,
            "items": [
                {"name": "item3", "value": "C"}
            ]
        }
    ]
    result = filter_operations(operations, "B")
    assert len(result) == 1
    assert result[0]["id"] == 1


def test_filter_operations_with_non_string_values():
    """Тестирование обработки нестроковых значений"""
    operations = [
        {"id": 1, "number": 12345, "flag": True},
        {"id": 2, "number": 67890, "flag": False}
    ]

    assert filter_operations(operations, "123") == []
    assert filter_operations(operations, "True") == []


@pytest.mark.parametrize("categories,expected", [
    # Точные совпадения (регистронезависимые)
    (["Перевод организации"], {"Перевод организации": 3}),
    (["перевод организации"], {"перевод организации": 3}),  # проверка регистронезависимости
    (["Перевод с карты на карту"], {"Перевод с карты на карту": 2}),

    # Частичные совпадения (по подстроке)
    (["Перевод"], {"Перевод": 6}),  # 6 операций содержат "Перевод" в описании
    (["организации"], {"организации": 3}),  # 3 операции с "организации"
    (["карты"], {"карты": 2}),  # 2 операции с "карты"

    # Несуществующие категории
    (["Кредит"], {"Кредит": 0}),
    ([""], {"": 0}),  # пустая строка
])
def test_category_counts(sample_operations_count, categories, expected):
    """Тестирование подсчёта операций (регистронезависимый поиск по подстроке)"""
    result = count_operations_by_category(sample_operations_count, categories)
    assert result == expected


def test_empty_inputs():
    """Тесты для пустых входных данных"""
    assert count_operations_by_category([], ["Любая категория"]) == {"Любая категория": 0}
    assert count_operations_by_category([], []) == {}
    assert count_operations_by_category([{"description": "Операция"}], []) == {}


def test_multiple_categories(sample_operations_count):
    """Тестирование нескольких категорий одновременно"""
    result = count_operations_by_category(
        sample_operations_count,
        ["Перевод", "вклада", "магазине"]
    )
    assert result == {
        "Перевод": 6,  # все переводы
        "вклада": 1,  # только "Открытие вклада"
        "магазине": 1  # только "Покупка в магазине"
    }


def test_special_characters():
    """Тестирование специальных символов в описании"""
    operations = [
        {"description": "Платеж (invoice #123)"},
        {"description": "Возврат #456"},
    ]
    result = count_operations_by_category(operations, ["#123", "#456"])
    assert result == {"#123": 1, "#456": 1}