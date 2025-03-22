import re


def regular_expression_data_search(data: list[dict], key_transaction: str) -> list[dict]:
    try:
        if not data:
            return []
        pattern = re.compile(r":", key_transaction)
        findal = pattern.search(data)
        return findal
    except Exception:
        return []


print(regular_expression_data_search([
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }], )