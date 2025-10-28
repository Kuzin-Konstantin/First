from datetime import datetime

from src.my_project.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Определяет тип (карта или счёт) и маскирует номер"""

    # 🛡 Защита от пустых или неверных входных данных
    if not info or not isinstance(info, str) or not info.strip():
        return "Некорректные данные"

    if info.startswith("Счет"):
        parts = info.split()
        if len(parts) < 2:
            return "Некорректные данные"
        number = parts[-1]
        return f"Счет {get_mask_account(number)}"
    else:
        parts = info.split()
        if len(parts) < 2:
            return "Некорректные данные"
        name = " ".join(parts[:-1])  # например, Visa Platinum
        number = parts[-1]  # только номер
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """Преобразует дату из '2024-03-11T02:26:18.671407' в '11.03.2024'"""
    dt = datetime.fromisoformat(date_str)
    return dt.strftime("%d.%m.%Y")


if __name__ == "__main__":  # pragma: no cover
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
