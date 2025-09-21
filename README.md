# Виджет банковских операций клиента

Учебный проект для работы с банковскими операциями клиента.  
Проект демонстрирует:
- Маскирование номеров карт и счетов
- Фильтрацию операций по состоянию (`EXECUTED`, `CANCELED`)
- Сортировку операций по дате
- Преобразование дат в удобный формат

## Установка и настройка

### 1. Клонировать репозиторий
```bash
git clone https://github.com/Kuzin-Konstantin/First
cd my-project
```

### 2. Установить зависимости через [Poetry](https://python-poetry.org/)
```bash
poetry install
```

Если Poetry не установлен, сначала поставить его:
```bash
pip install poetry
```

### 3. Активация виртуального окружения
```bash
poetry shell
```

## Зависимости

Управляются через `pyproject.toml`. Основные инструменты:
- Python 3.13+
- flake8
- black
- isort
- mypy
## Примеры работы функций

```python
from my_project.masks import get_mask_card_number, get_mask_account
from my_project.processing import filter_by_state, sort_by_date
from my_project.widget import mask_account_card, get_date

print(get_mask_card_number("7000792289606361"))
# 7000 79** **** 6361

print(get_mask_account("73654108430135874305"))
# **4305

print(get_date("2024-03-11T02:26:18.671407"))
# 11.03.2024
```
