import pytest
from src.my_project.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_data():
    """Пример данных для тестов"""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-11T02:26:18.671407"},
        {"id": 2, "state": "CANCELED", "date": "2023-05-10T09:15:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-01T00:00:00.000000"},
        {"id": 4, "state": "PENDING", "date": "2022-12-31T23:59:59.999999"},
    ]


# ------------------------- filter_by_state -------------------------


@pytest.mark.parametrize(
    "status,expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 1),
        ("PENDING", 1),
        ("UNKNOWN", 0),
    ],
)
def test_filter_by_state_various_statuses(sample_data, status, expected_count):
    """Фильтрация по разным статусам"""
    result = filter_by_state(sample_data, state=status)
    assert isinstance(result, list)
    assert all(item["state"] == status for item in result)
    assert len(result) == expected_count


def test_filter_by_state_default_param(sample_data):
    """Если не передать статус, берётся 'EXECUTED'"""
    result = filter_by_state(sample_data)
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_no_matches():
    """Если ни один элемент не подходит под статус"""
    data = [{"state": "CANCELED"}, {"state": "PENDING"}]
    result = filter_by_state(data, "EXECUTED")
    assert result == []


# ------------------------- sort_by_date -------------------------


def test_sort_by_date_descending(sample_data):
    """Сортировка по убыванию (последние сверху)"""
    result = sort_by_date(sample_data, descending=True)
    dates = [item["date"] for item in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending(sample_data):
    """Сортировка по возрастанию"""
    result = sort_by_date(sample_data, descending=False)
    dates = [item["date"] for item in result]
    assert dates == sorted(dates)


def test_sort_by_date_same_dates():
    """Если даты одинаковые — порядок не ломается"""
    data = [
        {"id": 1, "date": "2024-03-11T02:26:18.671407"},
        {"id": 2, "date": "2024-03-11T02:26:18.671407"},
    ]
    result = sort_by_date(data)
    assert [item["id"] for item in result] == [1, 2]  # порядок сохраняется


def test_sort_by_date_invalid_format():
    """Некорректные форматы дат не ломают сортировку"""
    data = [
        {"id": 1, "date": "2024/03/11"},
        {"id": 2, "date": "11-03-2024"},
        {"id": 3, "date": None},
        {"id": 4},  # без ключа 'date'
    ]
    # Должна просто отсортироваться без ошибок
    result = sort_by_date(data)
    assert isinstance(result, list)
    assert len(result) == 4
