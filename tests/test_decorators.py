from src.decorators import log


@log(filename="")
def get_mask_card_number(x: str) -> str:
    """Вызов функции для тестов"""
    return x


def test_log_get_mask_card_number(capsys) -> None:
    """Тест для вывода данных типа str в консоль"""
    get_mask_card_number("7000792289606361")
    captured = capsys.readouterr()
    assert "get_mask_card_number ok" in captured.out


@log(filename="")
def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    return data, reverse


def test_log_sort_by_date(capsys) -> None:
    """Тест для вывода данных типа list[dict] и bool в консоль"""
    sort_by_date(True, [3, 1, 4, 2])
    captured = capsys.readouterr()
    assert "sort_by_date ok" in captured.out


@log(filename="")
def card_number_generator(start: int, stop: int):
    return start, stop


def test_log_card_number_generator(capsys) -> None:
    """Тест для вывода данных типа int в консоль"""
    card_number_generator(1, 3)
    captured = capsys.readouterr()
    assert "card_number_generator ok" in captured.out


@log()
def exepition(a, b) -> None:
    """Тесты на ошибки"""
    return a / b


def test_zero_by_division(capsys):
    """Тест на ошибку с делением на 0"""
    try:
        exepition(2, 0)
    except ZeroDivisionError:
        pass
    assert "division by zero error: тип ошибки. Inputs: (2, 0), " "{}" "\n\n"
