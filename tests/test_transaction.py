from unittest.mock import mock_open, patch

from src.transaction import read_transaction_csv


def test_read_transaction_csv():
    """Проверяет, что функция корректно читает CSV-файл."""
    mock_data = """id;state;date;amount;currency_name;currency_code;from;to;description
5380041;CANCELED;2021-02-01T11:54:58Z;23789;Peso;UYU;;Счет 23294994494356835683;Открытие вклада
"""

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_transaction_csv("../data/transactions.csv")

    expected = [
        {
            "id": "5380041",
            "state": "CANCELED",
            "date": "2021-02-01T11:54:58Z",
            "amount": "23789",
            "currency_name": "Peso",
            "currency_code": "UYU",
            "from": "",
            "to": "Счет 23294994494356835683",
            "description": "Открытие вклада",
        }
    ]

    assert result == expected


def test_read_transaction_csv_empty_file():
    """Проверяет, что функция возвращает пустой список, если файл пустой."""
    mock_data = ""

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_transaction_csv("../data/transactions.csv")

    assert result == []


def test_read_transaction_csv_file_not_found():
    """Проверяет, что функция возвращает пустой список, если файл не найден."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_transaction_csv("../data/nonexistent.csv")

    assert result == []


def test_read_transaction_csv_invalid_file():
    """Проверяет, что функция возвращает пустой список, если файл некорректен."""
    mock_data = "invalid;data;here"

    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_transaction_csv("../data/invalid.csv")

    assert result == []
