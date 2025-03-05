from typing import Iterator


def filter_by_currency(transactions: list[dict], unit: str) -> Iterator[dict]:
    """Генераторная функция, фильтрует транзакции по заданной валюте и возвращает итератор."""
    if not isinstance(transactions, list):
        raise ValueError("transactions должен быть списком")
    if not isinstance(unit, str):
        raise ValueError("unit должен быть строкой")

    for key in transactions:
        if not isinstance(key, dict):
            continue
        try:
            if key["operationAmount"]["currency"]["code"] == unit:
                yield key
        except (KeyError, TypeError):
            continue


def transaction_descriptions(info_about_description: list[dict]) -> Iterator[str]:
    """Генераторная функция, возвращает описание каждой транзакции по очереди."""
    for description in info_about_description:
        if isinstance(description, dict) and "description" in description:
            yield description["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генераторная функция, выдает номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for num in range(start, stop + 1):
        card_number = f"{num:016d}"
        yield " ".join([card_number[i : i + 4] for i in range(0, 16, 4)])
