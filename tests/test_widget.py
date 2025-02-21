import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 1234554321123456", "MasterCard 1234 55** **** 3456"),
        ("Мир 1923774638281749", "Мир 1923 77** **** 1749"),
    ],
)
def test_mask_account_card_valid(input_data: str, expected: str) -> None:
    """Тест с корректным номером счета и карты"""
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize(
    "input_data, error_message",
    [
        ("", "Входные данные не могут быть пустыми"),
        ("Счет 7365abc8430135874305", "Номер счета должен состоять только из цифр"),
        ("Счет 756", "Номер счета должен содержать как минимум 4 цифры"),
        ("Visa Platinum 700079228960636", "Номер карты должен состоять из 16 цифр"),
        ("Мир 7000abc289606361", "Номер карты должен состоять из 16 цифр"),
    ],
)
def test_mask_account_card_invalid(input_data: str, error_message: str) -> None:
    """Тест для некорректных входных данных"""
    with pytest.raises(ValueError, match=error_message):
        mask_account_card(input_data)


@pytest.mark.parametrize(
    "data, output",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("0001-01-01T00:00:00.000000", "01.01.0001"),
        ("9999-12-31T23:59:59.999999", "31.12.9999"),
        ("2025-02-19", "Некорректный формат даты"),
    ],
)
def test_get_date_valid(data: str, output: str) -> None:
    """Тест с корректными датами"""
    assert get_date(data) == output


@pytest.mark.parametrize(
    "input_data",
    [
        "",
        "2025-02-19",
        "-03-11T02:26:18.671407",
        "2024--11T02:26:18.671407",
        "2024-03-T02:26:18.671407",
        "2024-03-11Tabc:26:18.671407",
        "2024/03/11T02:26:18.671407",
        "2024-03-11T02:26:18.abc",
    ],
)
def test_get_data_invalid(input_data: str) -> None:
    """Тест на некорректные входные данные"""
    assert get_date(input_data) == "Некорректный формат даты"
