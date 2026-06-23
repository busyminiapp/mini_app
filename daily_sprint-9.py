# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: DailySprint
import json, os

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки."""
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект (dict).")
        
        # Валидация структуры данных
        required_keys = ['focuses', 'tasks', 'retros']
        for key in required_keys:
            if key not in data:
                print(f"Предупреждение: отсутствует ключ '{key}'. Будет создан пустой список.")
                data[key] = []
        
        # Инициализация полей с дефолтными значениями, если они отсутствуют или None
        for section in ['focuses', 'tasks', 'retros']:
            if not isinstance(data[section], list):
                print(f"Ошибка: поле '{section}' должно быть списком.")
                return None
        
        # Проверка вложенных структур задач и ретро
        for i, task in enumerate(data['tasks']):
            if not isinstance(task.get('id'), int) or not isinstance(task.get('title'), str):
                print(f"Ошибка: задача {i} имеет неверную структуру.")
                return None
        
        for i, retro in enumerate(data['retros']):
            if not isinstance(retro.get('date'), str) or not isinstance(retro.get('notes'), str):
                print(f"Ошибка: ретро {i} имеет неверную структуру.")
                return None
                
        return data

    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return None
