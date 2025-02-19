import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_valid_card_number(correct_card_number: str) -> None:
    """Тест с корректным номером карты"""
    assert get_mask_card_number(correct_card_number) == "7000 79** **** 6361"


def test_invalid_length(invalid_length: str) -> None:
    """Тест с некорректной длинной карты"""
    with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр"):
        get_mask_card_number(invalid_length)


def test_non_digit_characters(non_digit_characters: str) -> None:
    """Тест с нечисловыми символами в номере карты"""
    with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр"):
        get_mask_card_number(non_digit_characters)


def test_empty_string(empty_string: str) -> None:
    """Теск с пустой строкой"""
    with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр"):
        get_mask_card_number(empty_string)


def test_whitespace_characters(whitespace_characters: str) -> None:
    """Тест с пробелами в номере карты"""
    with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр"):
        get_mask_card_number(whitespace_characters)


def test_valid_account_number(valid_account_number: str) -> None:
    """Тест с корректным номером счёта"""
    assert get_mask_account(valid_account_number) == "**4305"


def test_account_number_with_four_digits(account_number_with_four_digits: str) -> None:
    """Тест с номером счета из 4 цифр"""
    assert get_mask_account(account_number_with_four_digits) == "**1234"


def test_invalid_length_account(invalid_length_account: str) -> None:
    """Тест с некорректной длинной счёта"""
    with pytest.raises(ValueError, match="Номер счета должен содержать как минимум 4 цифры"):
        get_mask_account(invalid_length_account)


def test_empty_account_string(empty_account_string: str) -> None:
    """Тест с пустой строкой"""
    with pytest.raises(ValueError, match="Номер счета должен содержать как минимум 4 цифры"):
        get_mask_account(empty_account_string)


def test_non_digit_characters_account(non_digit_characters_account: str) -> None:
    """Тест с нечисловыми символами в номере счёта"""
    with pytest.raises(ValueError, match="Номер счета должен состоять только из цифр"):
        get_mask_account(non_digit_characters_account)
