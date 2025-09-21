def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Вернуть только элементы с заданным state."""
    return [item for item in data if item.get("state") == state]

def sort_by_date(data: list[dict], descending: bool = True) -> list[dict]:
    """Отсортировать по строковому ключу 'date' (ISO-8601)."""
    # Если у элемента нет 'date', подставим пустую строку — такие уйдут в начало/конец.
    return sorted(data, key=lambda x: x.get("date", ""), reverse=descending)



