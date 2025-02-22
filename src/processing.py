from datetime import datetime


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

    def validate_date(date_str: str) -> bool:
        """Проверяет, что строка соответствует формату ISO 8601."""
        try:
            datetime.fromisoformat(date_str)
            return True
        except ValueError:
            return False

    # Проверяем корректность всех дат перед сортировкой
    for item in data:
        if not validate_date(item["date"]):
            raise ValueError("Некорректный формат даты")
    return sorted(data, key=lambda x: x["date"], reverse=reverse)
