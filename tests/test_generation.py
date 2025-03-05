import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(sample_transactions: list[dict]) -> None:
    """Тест с корректными данными транзакций по валюте USD."""
    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
    # Проверяем, что возвращены только транзакции с валютой USD
    assert len(usd_transactions) == 2
    assert all(tx["operationAmount"]["currency"]["code"] == "USD" for tx in usd_transactions)


def test_filter_by_currency_rub(sample_transactions: list[dict]) -> None:
    """Тест с корректными данными транзакций по валюте RUB."""
    rub_transactions = list(filter_by_currency(sample_transactions, "RUB"))
    # Проверяем, что возвращена только одна транзакция с валютой RUB
    assert len(rub_transactions) == 1
    assert all(tx["operationAmount"]["currency"]["code"] == "RUB" for tx in rub_transactions)


def test_filter_by_currency_eur(sample_transactions: list[dict]) -> None:
    """Тест с корректными данными транзакций по валюте EUR (которой нет в данных)."""
    eur_transactions = list(filter_by_currency(sample_transactions, "EUR"))
    # Проверяем, что возвращен пустой список
    assert len(eur_transactions) == 0


def test_filter_by_currency_empty_list() -> None:
    """Тест с пустым списком."""
    empty_transactions: list = []
    result = list(filter_by_currency(empty_transactions, "USD"))
    assert len(result) == 0


def test_filter_by_currency_invalid_transaction(filter_by_currency_invalid_transaction: list[dict]) -> None:
    """Тест для списка с некорректными данными."""
    result = list(filter_by_currency(filter_by_currency_invalid_transaction, "USD"))
    assert len(result) == 1
    assert result[0]["id"] == 1


def test_filter_by_currency_invalid_unit_type(sample_transactions: list[dict]) -> None:
    """Тест на проверку корректной работы программы если unit не строка."""
    with pytest.raises(ValueError, match="unit должен быть строкой"):
        list(filter_by_currency(sample_transactions, 123))


def test_filter_by_currency_invalid_transactions_type() -> None:
    """Тест на проверку корректной работы программы если transactions не список."""
    with pytest.raises(ValueError, match="transactions должен быть списком"):
        list(filter_by_currency({"invalid": "data"}, "USD"))


@pytest.mark.parametrize(
    "transactions, expected_descriptions",
    [
        # Корректные данные
        (
            [
                {"description": "Перевод организации"},
                {"description": "Перевод со счета на счет"},
                {"description": "Перевод с карты на карту"},
            ],
            ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"],
        ),
        # Пустой список
        ([], []),
        # Некорректные данные (отсутствие ключа "description")
        (
            [{"id": 1, "state": "EXECUTED"}, {"description": "Перевод организации"}, {"id": 2, "state": "EXECUTED"}],
            ["Перевод организации"],
        ),
        # Некорректные данные (описание не строка)
        (
            [{"description": "Перевод организации"}, {"description": 12345}, {"description": None}],
            ["Перевод организации", 12345, None],
        ),
    ],
    ids=["корректные данные", "пустой список", "отсутствие ключа 'description'", "описание не строка"],
)
def test_transaction_descriptions(transactions: list[dict], expected_descriptions: list) -> None:
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions == expected_descriptions


def test_transaction_descriptions_with_fixture(sample_transactions: list[dict]) -> None:
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]


@pytest.mark.parametrize(
    "start, stop, expected_output",
    [
        # Корректный диапазон
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        # Крайние значения диапазона
        (
            9999999999999995,
            9999999999999999,
            [
                "9999 9999 9999 9995",
                "9999 9999 9999 9996",
                "9999 9999 9999 9997",
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
        # Диапазон из одного элемента
        (1234567890123456, 1234567890123456, ["1234 5678 9012 3456"]),
        # Нулевые значения
        (0, 0, ["0000 0000 0000 0000"]),
    ],
    ids=["корректный диапазон", "крайние значения диапазона", "диапазон из одного элемента", "нулевые значения"],
)
def test_card_number_generator(start: int, stop: int, expected_output: str) -> None:
    """Проверка генерации номеров карт в заданном диапазоне."""
    result = list(card_number_generator(start, stop))
    assert result == expected_output


def test_card_number_formatting() -> None:
    """Проверка корректности форматирования номеров карт."""
    generator = card_number_generator(1, 1)
    card_number = next(generator)
    assert card_number == "0000 0000 0000 0001"
    assert len(card_number) == 19  # Проверка длины строки с пробелами
    assert card_number.count(" ") == 3


def test_generator_stops_correctly() -> None:
    """Проверка, что генератор корректно завершает работу."""
    generator = card_number_generator(1, 1)
    next(generator)  # Первый вызов
    with pytest.raises(StopIteration):
        next(generator)
