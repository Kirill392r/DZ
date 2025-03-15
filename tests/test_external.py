from unittest.mock import Mock, patch

import pytest

from data.external_api import convert_transaction_to_rub


def test_convert_rub_to_rub():
    """Проверяет, что функция возвращает сумму в рублях."""
    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "RUB"}}}
    with patch("requests.get") as mock_get:
        result = convert_transaction_to_rub(transaction)
        assert result == 100.0
        mock_get.assert_not_called()


def test_convert_usd_to_rub():
    """Проверяет, что функция корректно конвертирует USD в RUB."""
    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "USD"}}}
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 75.0}}

    with patch("requests.get", return_value=mock_response):
        result = convert_transaction_to_rub(transaction)
        assert result == 7500.0


def test_convert_eur_to_rub():
    """Проверяет, что функция корректно конвертирует EUR в RUB."""
    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "EUR"}}}
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 85.0}}

    with patch("requests.get", return_value=mock_response):
        result = convert_transaction_to_rub(transaction)
        assert result == 8500.0


def test_unsupported_currency():
    """Проверяет, что функция выбрасывает исключение, если валюта не поддерживается."""
    transaction = {"operationAmount": {"amount": "100.0", "currency": {"code": "GBP"}}}
    with pytest.raises(ValueError, match="Unsupported currency: GBP"):
        convert_transaction_to_rub(transaction)
