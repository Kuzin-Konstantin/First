def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Вернуть только элементы с заданным state."""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list[dict], descending: bool = True) -> list[dict]:
    """Отсортировать по строковому ключу 'date' (ISO-8601)."""
    # Если у элемента нет 'date', подставим пустую строку — такие уйдут в начало/конец.
    return sorted(data, key=lambda x: x.get("date", ""), reverse=descending)


data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(data))
print(filter_by_state(data, "CANCELED"))
print(sort_by_date(data))  # по убыванию (последние сверху)
