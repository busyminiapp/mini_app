# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: DailySprint
import json, os

def load_sprint_data(filepath: str) -> dict | None:
    try:
        if not os.path.exists(filepath):
            print(f"Файл {filepath} не найден.")
            return None
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("Некорректный формат JSON данных")
        print(f"Данные успешно загружены из {filepath}")
        return data
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка при загрузке файла: {type(e).__name__}: {e}")
        return None
