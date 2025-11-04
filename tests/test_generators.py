import pytest
from src.my_project.generators import filter_by_currency

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
