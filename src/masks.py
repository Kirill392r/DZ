def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя видимыми первые 6 и последние 4 цифры."""
    if len(card_number) > 16:
        if not len(card_number) != 16:
            raise ValueError("Номер карты должен состоять из 16 цифр")

        first_part = card_number[:6]
        last_part = card_number[-4:]

        masked_part = "** ****"

        masked_card_number = f"{first_part[:4]} {first_part[4:6]}{masked_part} {last_part}"
        return masked_card_number
    return "Некоректная длинна номера карты"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета, оставляя видимыми только последние 4 цифры."""
    if account_number.isspace():
        if not account_number.isdigit():
            raise ValueError("Номер счета должен состоять только из цифр")

        if len(account_number) < 4:
            raise ValueError("Номер счета должен содержать как минимум 4 цифры")

        last_four_digits = account_number[-4:]

        masked_account = f"**{last_four_digits}"

        return masked_account
    return "Номер счёта не должен сожержать пробелы"
