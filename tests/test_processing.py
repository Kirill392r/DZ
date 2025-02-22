import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3, 5]),
        ("PENDING", [2]),
        ("CANCELED", [4]),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state(filter_by_state_fixture: list[dict], state: str, expected_ids: list) -> None:
    """Проверяет, что функция корректно фильтрует список словарей по статусу."""
    assert [item["id"] for item in filter_by_state(filter_by_state_fixture, state)] == expected_ids


def test_filter_by_state_empty_list() -> None:
    """Проверяет, что функция корректно обрабатывает пустой список."""
    assert filter_by_state([], "EXECUTED") == []


def test_filter_by_state_default(filter_by_state_fixture: list[dict]) -> None:
    """Проверяет, что функция использует значение по умолчанию для статуса."""
    assert [item["id"] for item in filter_by_state(filter_by_state_fixture)] == [1, 3, 5]


@pytest.mark.parametrize(
    "reverse, expected_ids",
    [
        (True, [3, 1, 4, 2]),
        (False, [2, 1, 4, 3]),
    ],
)
def test_sort_by_date(sort_by_date_fixture: list[dict], reverse: bool, expected_ids: list) -> None:
    """Проверяет, что функция корректно сортирует список словарей по дате."""
    result = sort_by_date(sort_by_date_fixture, reverse=reverse)
    assert [item["id"] for item in result] == expected_ids


def test_sort_by_date_same_dates(sort_by_date_fixture: list[dict]) -> None:
    """Проверяет, что функция корректно обрабатывает одинаковые даты."""
    result = sort_by_date(sort_by_date_fixture, reverse=True)
    assert result[1]["id"] == 1
    assert result[2]["id"] == 4


def test_sort_by_date_empty_list() -> None:
    """Проверяет, что функция корректно обрабатывает пустой список."""
    assert sort_by_date([], reverse=True) == []


def test_sort_by_date_invalid_format(sort_by_date_invalid: list[dict]) -> None:
    """Проверяет, что функция корректно обрабатывает некорректные форматы дат."""
    with pytest.raises(ValueError):
        sort_by_date(sort_by_date_invalid, reverse=True)
