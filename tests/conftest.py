import pytest


@pytest.fixture
def correct_card_number() -> str:
    """Фикстура для теста с корректным номером карты"""
    return "7000792289606361"


@pytest.fixture
def invalid_length() -> str:
    """Фикстура для теста с с некорректной длинной карты"""
    return "700079228960636"


@pytest.fixture
def non_digit_characters() -> str:
    """Фикстура для теста с нечисловыми символами в номере карты"""
    return "7000abc289606361"


@pytest.fixture
def empty_string() -> str:
    """Фикстура для теста с пустой строкой"""
    return ""


@pytest.fixture
def whitespace_characters() -> str:
    """Фикстура для теста с пробелами в номере карты"""
    return "7000 7922 8960 6361"


@pytest.fixture
def valid_account_number() -> str:
    """Фикстура для теста с корректным номером счета"""
    return "73654108430135874305"


@pytest.fixture
def account_number_with_four_digits() -> str:
    """Фикстура для теста с номером счета из 4 цифр"""
    return "1234"


@pytest.fixture
def invalid_length_account() -> str:
    """Фикстура для теста с некорректной длинной счета"""
    return "736"


@pytest.fixture
def empty_account_string() -> str:
    """Фикстура для теста с пустой строкой"""
    return ""


@pytest.fixture
def non_digit_characters_account() -> str:
    """Фикстура для теста с нечисловыми символами в номере счета"""
    return "7365abc8430135874305"


@pytest.fixture
def filter_by_state_fixture() -> list[dict]:
    """Список словарей для проверки теста на корректность работы функции"""
    return [
        {"id": 1, "state": "EXECUTED", "amount": "100.00"},
        {"id": 2, "state": "PENDING", "amount": "200.00"},
        {"id": 3, "state": "EXECUTED", "amount": "300.00"},
        {"id": 4, "state": "CANCELED", "amount": "400.00"},
        {"id": 5, "state": "EXECUTED", "amount": "500.00"},
    ]


@pytest.fixture
def sort_by_date_fixture() -> list[dict]:
    """Список словарей для проверки теста на корректность работы функции"""
    return [
        {"id": 1, "date": "2025-03-20T02:26:18.671407"},
        {"id": 2, "date": "2025-03-19T12:34:56.123456"},
        {"id": 3, "date": "2025-03-21T08:15:42.987654"},
        {"id": 4, "date": "2025-03-20T02:26:18.671407"},
    ]


@pytest.fixture
def sort_by_date_invalid() -> list[dict]:
    return [
        {"id": 1, "date": "2024-03-11"},
        {"id": 2, "date": "2024/03/11T02:26:18.671407"},
        {"id": 3, "date": "abc"},
    ]
