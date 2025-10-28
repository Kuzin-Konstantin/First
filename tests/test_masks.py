from src.my_project.masks import get_mask_card_number, get_mask_account


def test_mask_basic():
    """Проверяем, что номер карты маскируется правильно"""
    result = get_mask_card_number("7000792289606361")
    assert result == "7000 79** **** 6361"


def test_mask_short_number():
    """Если номер слишком короткий — функция всё равно должна отработать"""
    result = get_mask_card_number("1234")
    assert "****" in result


def test_mask_empty_string():
    """Если передана пустая строка — возвращается строка со звёздочками"""
    result = get_mask_card_number("")
    assert "**" in result


def test_mask_with_letters():
    """Функция не должна ломаться, если есть буквы"""
    result = get_mask_card_number("ABCD12EFGH5678")
    assert "**" in result


def test_mask_account_basic():
    """Проверяем, что номер счёта маскируется правильно"""
    result = get_mask_account("40817810099910004312")
    assert result == "**4312"


def test_mask_account_short_number():
    """Если номер слишком короткий — функция всё равно должна вернуть звёздочки и хвост"""
    result = get_mask_account("123")
    # У короткого номера просто возвращается весь номер после звёздочек
    assert result == "**123"


def test_mask_account_empty_string():
    """Если передана пустая строка — возвращаем только звёздочки"""
    result = get_mask_account("")
    assert result == "**"


def test_mask_account_different_formats():
    """Функция не должна ломаться, если в номере есть пробелы или буквы"""
    result1 = get_mask_account("AB1234567")
    result2 = get_mask_account(" 987654321 ")
    assert result1.startswith("**")
    assert result2.startswith("**")
    assert len(result1) >= 3  # минимум две звёздочки + цифры
    assert len(result2) >= 3
