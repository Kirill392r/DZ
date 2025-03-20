from unittest.mock import patch

import pandas as pd

from src.transactions_excel import read_transaction_exel


def test_read_transaction_exel_success():
    """Проверяет, что функция корректно читает Excel-файл и возвращает список словарей."""
    mock_data = pd.DataFrame({"id": [1, 2], "amount": [100.0, 200.0], "currency": ["RUB", "USD"]})

    with patch("pandas.read_excel", return_value=mock_data):
        result = read_transaction_exel("dummy_file.xlsx")
        expected = [{"id": 1, "amount": 100.0, "currency": "RUB"}, {"id": 2, "amount": 200.0, "currency": "USD"}]
        assert result == expected


def test_read_transaction_exel_file_not_found():
    """Проверяет, что функция возвращает пустой список, если файл не найден."""
    with patch("pathlib.Path.exists", return_value=False):
        result = read_transaction_exel("non_existent_file.xlsx")
        assert result == []


def test_read_transaction_exel_invalid_file():
    """Проверяет, что функция возвращает пустой список, если файл некорректен."""
    with patch("pandas.read_excel", side_effect=Exception("Invalid file")):
        result = read_transaction_exel("invalid_file.xlsx")
        assert result == []


def test_read_transaction_exel_empty_file():
    """Проверяет, что функция возвращает пустой список, если файл пуст."""
    mock_data = pd.DataFrame()
    with patch("pandas.read_excel", return_value=mock_data):
        result = read_transaction_exel("empty_file.xlsx")
        assert result == []
