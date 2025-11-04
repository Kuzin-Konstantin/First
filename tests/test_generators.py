import pytest
from src.my_project.generators import filter_by_currency, transaction_descriptions

@pytest.fixture
def transactions():
    return [
        {
            "id": 1,
            "operationAmount": {"amount": "100.0", "currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "operationAmount": {"amount": "200.0", "currency": {"code": "RUB"}},
            "description": "Оплата услуг",
        },
        {
            "id": 3,
            "operationAmount": {"amount": "300.0", "currency": {"code": "USD"}},
            "description": "Перевод на карту",
        },
    ]


def test_filter_by_currency_usd(transactions):
    usd_transactions = list(filter_by_currency(transactions, "USD"))

    assert len(usd_transactions) == 2
    assert all(
        tx["operationAmount"]["currency"]["code"] == "USD"
        for tx in usd_transactions
    )


def test_filter_by_currency_no_match(transactions):
    eur_transactions = list(filter_by_currency(transactions, "EUR"))
    assert eur_transactions == []


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_filter_by_currency_missing_keys():
    transactions = [
        {"id": 1},
        {"id": 2, "operationAmount": {}},
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert result == []

def test_transaction_descriptions_basic(transactions):
    descriptions = list(transaction_descriptions(transactions))
    expected = [
        "Перевод организации",
        "Оплата услуг",
        "Перевод на карту",
    ]
    assert descriptions == expected

def test_transaction_descriptions_missing_field():
    data = [
        {"id": 1, "description": "Оплата"},
        {"id": 2},  # нет описания
        {"id": 3, "description": "Перевод"},
    ]
    result = list(transaction_descriptions(data))
    assert result == ["Оплата", "Перевод"]


def test_transaction_descriptions_empty():
    assert list(transaction_descriptions([])) == []


def test_transaction_descriptions_stop_iteration(transactions):
    gen = transaction_descriptions(transactions)

    # извлекаем все значения
    for _ in range(len(transactions)):
        next(gen)

    # следующий вызов должен вызвать StopIteration
    with pytest.raises(StopIteration):
        next(gen)
