import os
import sys


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате XXXX XX** **** XXXX"""
    # первые 6 символов
    first = card_number[:6]
    # последние 4 символа
    last = card_number[-4:]
    # собираем строку по шаблону
    return f"{first[:4]} {first[4:6]}** **** {last}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета **XXXX"""
    return f"**{account_number[-4:]}"


# Этот код выполнится только если файл запустить напрямую
if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))  # 7000 79** **** 6361
    print(get_mask_account("73654108430135874305"))  # **4305
