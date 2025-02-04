from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Маскирует номер карты или счёта в зависимости от типа."""
    if info.startswith("Счет"):
        masked_account = info.replace("Счет", "").strip()
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
        date_part = date_str.split("T")[0]
        year, month, day = date_part.split("-")
        formatted_date = f"{day}.{month}.{year}"
        return formatted_date
    except (IndexError, ValueError):
        return "Некорректный формат даты"
