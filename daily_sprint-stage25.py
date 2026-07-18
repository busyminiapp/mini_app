# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: DailySprint
import re

def validate_date(date_str):
    """Validates a date string in YYYY-MM-DD format and returns it or raises ValueError."""
    if not isinstance(date_str, str):
        raise ValueError("Дата должна быть строкой")
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(pattern, date_str):
        raise ValueError(f"Неверный формат даты: '{date_str}'. Ожидается формат YYYY-MM-DD (например, 2025-12-31)")
    year, month, day = map(int, date_str.split('-'))
    if month < 1 or month > 12:
        raise ValueError(f"Неверный месяц в дате '{date_str}'")
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[2] = 29
    if day < 1 or day > days_in_month[month]:
        raise ValueError(f"Неверный день в дате '{date_str}'")
    return date_str
