from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(info: str) -> str:
    """Маскирует номер карты или счета в зависимости от типа."""
    if not info:
        raise ValueError("Входные данные не могут быть пустыми")
    if info.startswith("Счет"):
        masked_account = info.replace("Счет", "").strip()
        if not masked_account.isdigit():
            raise ValueError("Номер счета должен состоять только из цифр")
        if len(masked_account) < 4:
            raise ValueError("Номер счета должен содержать как минимум 4 цифры")
        masked_number = get_mask_account(masked_account)
        return f"Счет {masked_number}"
    else:
        parts = info.split()
        masked_card_number = parts[-1]
        masked_number = get_mask_card_number(masked_card_number)
        return " ".join(parts[:-1]) + " " + masked_number


def get_date(date_str: str) -> str:
    """Преобразует строку с датой в формате "2024-03-11T02:26:18.671407"
    в строку с датой в формате "ДД.ММ.ГГГГ"."""
    try:
        if "T" not in date_str:
            return "Некорректный формат даты"
        date_part, time_part = date_str.split("T")
        if len(date_part.split("-")) != 3:
            return "Некорректный формат даты"
        year, month, day = date_part.split("-")
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            return "Некорректный формат даты"
        if not all(part.isdigit() for part in time_part.replace(":", "").replace(".", "")):
            return "Некорректный формат даты"
        formatted_date = f"{day}.{month}.{year}"
        return formatted_date
    except (IndexError, ValueError):
        return "Некорректный формат даты"
