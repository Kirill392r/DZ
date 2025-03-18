import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("..\\logs\\masks.log", "w", encoding="utf8")
file_formater = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты, оставляя видимыми первые 6 и последние 4 цифры."""

    if not card_number.isdigit() or len(card_number) != 16:
        logger.error("Номер карты должен состоять из 16 цифр")
        raise ValueError("Номер карты должен состоять из 16 цифр")

    first_part = card_number[:6]
    last_part = card_number[-4:]

    masked_part = "** ****"

    masked_card_number = f"{first_part[:4]} {first_part[4:6]}{masked_part} {last_part}"
    logger.info("Номер карты успешно замаскирован")
    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета, оставляя видимыми только последние 4 цифры."""

    if len(account_number) < 4:
        logger.error("Номер счета должен содержать как минимум 4 цифры")
        raise ValueError("Номер счета должен содержать как минимум 4 цифры")

    if not account_number.isdigit():
        logger.error("Номер счета должен состоять только из цифр")
        raise ValueError("Номер счета должен состоять только из цифр")

    last_four_digits = account_number[-4:]

    masked_account = f"**{last_four_digits}"
    logger.info("Номер счёта успешно замаскирован")
    return masked_account
