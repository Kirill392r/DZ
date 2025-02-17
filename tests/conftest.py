import pytest


@pytest.fixture
def correct_card_number():
    return "7000 79** **** 6361"


@pytest.fixture
def invalid_length():
    return "Некоректная длинна номера карты"


@pytest.fixture
def the_card_number_must_consist_of_sixteen_digits():
    return "Номер карты должен состоять из 16 цифр"


@pytest.fixture
def correct_card_number_account():
    return "**4305"


@pytest.fixture
def invalid_length_account():
    return "Номер счета должен содержать как минимум 4 цифры"


@pytest.fixture
def non_digit_characters_account():
    return "Номер счета должен состоять только из цифр"


@pytest.fixture
def whitespace_characters_account():
    return "Номер счёта не должен сожержать пробелы"
