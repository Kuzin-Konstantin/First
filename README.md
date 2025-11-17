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
- pytest 
- pytest-cov

## Тестирование

### 1. Запуск тестов
Для запуска всех тестов используйте команду:
```bash
pytest -v
```

### 2. Проверка покрытия кода тестами
Чтобы увидеть процент покрытия (coverage):
```bash
pytest --cov=src/my_project
```

### 3. Отчёт в виде HTML
Для просмотра красивого отчёта в браузере:
```bash
pytest --cov=src/my_project --cov-report=html
```
После выполнения команды откройте файл `htmlcov/index.html`.

---
## 🧠 Модуль `generators`

Модуль **`generators`** предназначен для эффективной работы с большими объёмами данных о банковских транзакциях с помощью **генераторов Python**.

### Реализованные функции

#### 1️⃣ `filter_by_currency(transactions, currency_code)`
Возвращает итератор по транзакциям, где валюта совпадает с указанной (`"USD"`, `"RUB"` и т.д.).

**Пример:**
```python
from src.my_project.generators import filter_by_currency

transactions = [
    {"id": 1, "operationAmount": {"amount": "100.0", "currency": {"code": "USD"}}},
    {"id": 2, "operationAmount": {"amount": "200.0", "currency": {"code": "RUB"}}},
]

for tx in filter_by_currency(transactions, "USD"):
    print(tx)
```

**Результат:**
```python
{'id': 1, 'operationAmount': {'amount': '100.0', 'currency': {'code': 'USD'}}}
```

---

#### 2️⃣ `transaction_descriptions(transactions)`
Генератор, возвращающий описания (`description`) операций по очереди.

**Пример:**
```python
from src.my_project.generators import transaction_descriptions

transactions = [
    {"description": "Перевод организации"},
    {"description": "Оплата услуг"},
]

for desc in transaction_descriptions(transactions):
    print(desc)
```

**Результат:**
```
Перевод организации
Оплата услуг
```

---

#### 3️⃣ `card_number_generator(start, stop)`
Генератор номеров банковских карт в формате `XXXX XXXX XXXX XXXX`,  
где `X` — цифра номера. Диапазон включителен.

**Пример:**
```python
from src.my_project.generators import card_number_generator

for number in card_number_generator(1, 5):
    print(number)
```

**Результат:**
```
0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
0000 0000 0000 0004
0000 0000 0000 0005
```

---

### 🧪 Тестирование модуля `generators`

Для проверки корректности работы реализованы тесты с использованием **pytest**.

```bash
pytest tests/test_generators.py -v
```

Проверка покрытия только для модуля `generators`:
```bash
pytest --cov=src.my_project.generators --cov-report=term-missing
```

📊 Фактическое покрытие тестами: **100%**

---
