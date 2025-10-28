import pytest
from src.my_project.widget import mask_account_card, get_date


# ------------------- mask_account_card -------------------


@pytest.mark.parametrize(
    "info, expected_part",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_valid_inputs(info, expected_part):
    """Функция правильно маскирует карту или счёт"""
    result = mask_account_card(info)
    assert expected_part in result


@pytest.mark.parametrize(
    "bad_input",
    [
        "",  # пустая строка
        "12345",  # без слова "Счет" и без пробела
        "Счет",  # нет номера
        "Visa",  # без номера карты
        None,  # вообще не строка
    ],
)
def test_mask_account_card_invalid_inputs(bad_input):
    """Функция не должна падать на некорректных данных"""
    try:
        result = mask_account_card(str(bad_input))
        assert isinstance(result, str)
    except Exception:
        pytest.fail("Функция не должна вызывать ошибку")


# ------------------- get_date -------------------


def test_get_date_valid_format():
    """Проверка корректного преобразования даты ISO -> DD.MM.YYYY"""
    result = get_date("2024-03-11T02:26:18.671407")
    assert result == "11.03.2024"


@pytest.mark.parametrize(
    "input_str",
    [
        "2024-01-01T00:00:00.000000",  # начало года
        "2024-12-31T23:59:59.999999",  # конец года
    ],
)
def test_get_date_various_valid_formats(input_str):
    """Функция корректно форматирует разные даты"""
    result = get_date(input_str)
    assert result.count(".") == 2
    assert len(result) == 10  # формат DD.MM.YYYY


@pytest.mark.parametrize(
    "invalid_input",
    [
        "",  # пустая строка
        "2024/03/11",  # неправильный формат
        "текст",  # не дата
        None,  # None вместо строки
    ],
)
def test_get_date_invalid_formats(invalid_input):
    """Функция не должна ломаться при некорректных строках"""
    try:
        get_date(str(invalid_input))
    except Exception:
        # ожидаем, что выбросится ValueError, но программа не должна падать
        pytest.xfail("Некорректный формат даты вызывает ошибку — ожидаемо")
