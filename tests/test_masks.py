from src.masks import get_mask_account, get_mask_card_number


def test_valid_card_number(correct_card_number):
    """Тест с корректным номером карты"""
    assert get_mask_card_number("7000792289606361")


def test_invalid_length(invalid_length):
    """Тест с некорректной длинной карты"""
    assert get_mask_card_number("700079228960636")


def test_non_digit_characters(the_card_number_must_consist_of_sixteen_digits):
    """Тест с нечисловыми символами в номере карты"""
    assert get_mask_card_number("7000abc289606361")


def test_empty_string(the_card_number_must_consist_of_sixteen_digits):
    """Теск с пустой строкой"""
    assert get_mask_card_number("")


def test_whitespace_characters(the_card_number_must_consist_of_sixteen_digits):
    """Тест с пробелами в номере карты"""
    assert get_mask_card_number("7000 7922 8960 6361")


def test_correct_card_number_account(correct_card_number_account):
    """Тест с корректным номером счёта"""
    assert get_mask_account("73654108430135874305")


def test_invalid_length_account(invalid_length_account):
    """Тест с некорректной длинной счёта"""
    assert get_mask_account("736")


def test_non_digit_characters_account(non_digit_characters_account):
    """Тест с нечисловыми символами в номере счёта"""
    assert get_mask_account("7365abc8430135874305")


def test_whitespace_characters_account(whitespace_characters_account):
    """Тест с пробелами в номере счёта"""
    assert get_mask_account("7365 4108 4301 3587 4305")
