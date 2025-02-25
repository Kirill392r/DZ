def filter_by_currency(transactions: list[dict] , unit: str) -> dict:
    """Генераторная функция, фильтрует транзакции по заданной валюте и возвращает итератор."""
    for key in transactions:
        if key["operationAmount"]["currency"]["code"] == unit:
            yield key


def transaction_descriptions(transactions: list[dict]) -> str:
    """Генераторная функция, возвращает описание каждой транзакции по очереди."""
    for description in transactions:
        yield description["description"]


def card_number_generator(start: int, stop: int) -> str:
    """Генераторная функция, выдает номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for num in range(start, stop + 1):
        card_number = f"{num:016d}"
        yield " ".join([card_number[i:i+4] for i in range(0, 16, 4)])
