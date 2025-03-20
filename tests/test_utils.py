from unittest.mock import mock_open, patch

from src.utils import read_transactions


def test_read_transactions_valid_file():
    """Проверяет, что функция корректно читает JSON-файл."""
    mock_data = '[{"id": 1, "operationAmount": {"amount": "100.0", "currency": {"code": "RUB"}}}]'

    with patch("pathlib.Path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data=mock_data)):
            result = read_transactions("../data/operations.json")
            assert result == [{"id": 1, "operationAmount": {"amount": "100.0", "currency": {"code": "RUB"}}}]


def test_read_transactions_empty_file():
    """Проверяет, что функция возвращает пустой список, если файл пустой."""
    with patch("builtins.open", mock_open(read_data="")):
        result = read_transactions("../data/operations.json")
        assert result == []


def test_read_transactions_invalid_json():
    """Проверяет, что функция возвращает пустой список, если файл содержит невалидный JSON."""
    with patch("builtins.open", mock_open(read_data="invalid json")):
        result = read_transactions("../data/operations.json")
        assert result == []


def test_read_transactions_file_not_found():
    """Проверяет, что функция возвращает пустой список, если файл не найден."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_transactions("../data/operations.json")
        assert result == []
