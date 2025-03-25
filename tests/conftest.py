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


@pytest.fixture
def sample_transactions() -> list[dict]:
    """Фикстура для корректных тестов к функции filter_by_currency"""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]


@pytest.fixture
def filter_by_currency_invalid_transaction() -> list[dict]:
    """Фикстура для некорректных тестов к функции filter_by_currency"""
    return [
        {"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "USD"}}},
        {"id": 2, "operationAmount": {"amount": "200"}},
        {"id": 3, "operationAmount": {}},
        {"id": 4},
    ]



@pytest.fixture
def sample_operations() -> list[dict]:
    return [
    {
        "id": 1,
        "description": "Перевод организации",
        "from": "Счет 1234567890123456",
        "to": "Счет 9876543210987654",
        "operationAmount": {
            "amount": "10000",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        }
    },
    {
        "id": 2,
        "description": "Перевод с карты на карту",
        "from": "Visa Platinum 1234567890123456",
        "to": "Maestro 9876543210987654",
        "operationAmount": {
            "amount": "500",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        }
    },
    {
        "id": 3,
        "description": "Открытие вклада",
        "to": "Счет 5678123409876543",
        "operationAmount": {
            "amount": "150000",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        }
    }
]


@pytest.fixture
def sample_operations_count() -> list[dict]:
    return [
    {"description": "Перевод организации", "amount": 100},
    {"description": "Перевод с карты на карту", "amount": 50},
    {"description": "Открытие вклада", "amount": 200},
    {"description": "Перевод со счета на счет", "amount": 150},
    {"description": "Перевод организации", "amount": 300},
    {"description": "Покупка в магазине", "amount": 20},
    {"description": "Перевод организации", "amount": 400},
    {"description": "Перевод с карты на карту", "amount": 75},
]