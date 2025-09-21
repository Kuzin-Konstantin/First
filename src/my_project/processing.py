def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Вернуть только элементы с заданным state."""
    return [item for item in data if item.get("state") == state]



