def filter_by_state(list_dikt: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция которая возвращает новый список словарей, содержащий только те словари,
    у которых ключ соответствует указанному значению."""
    new_list_dikt = []
    for i in list_dikt:
        if i.get("state") == state:
            new_list_dikt.append(i)
    return new_list_dikt


def sort_by_date(data: list[dict], reverse: bool = True) -> list:
    """Функция которая возвращает новый список, отсортированный по дате"""

    return sorted(data, key=lambda x: x["date"], reverse=reverse)
