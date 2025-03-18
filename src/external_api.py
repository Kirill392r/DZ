import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_transaction_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.
    Если валюта уже в рублях, возвращает amount.
    Если валюта в USD или EUR, конвертирует в рубли.
    Если валюта не поддерживается, выбрасывает ValueError.
    """
    operation_amount = transaction.get("operationAmount", {})
    currency_code = operation_amount.get("currency", {}).get("code", "RUB").upper()
    amount = float(operation_amount.get("amount", 0.0))

    if currency_code == "RUB":
        return amount
    elif currency_code in ["USD", "EUR"]:

        headers = {"apikey": API_KEY}
        response = requests.get(f"{BASE_URL}?base={currency_code}&symbols=RUB", headers=headers)
        if response.status_code == 200:
            rate = response.json()["rates"].get("RUB")
            return amount * rate
        else:
            raise Exception(f"Failed to fetch exchange rate: {response.status_code} {response.text}")
    else:
        return 0.0
