# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: DailySprint
def reset_demo_data():
    """Сбросить все демо-данные в исходное состояние."""
    import demo_data as dd
    for key in list(dd.data.keys()):
        if key.startswith("_demo"):
            del dd.data[key]
    # Восстановить дефолтные фокусы и задачи
    dd.data["_demo_focuses"] = [
        {"title": "Исследовать API", "priority": 1},
        {"title": "Написать докстринг", "priority": 2},
    ]
    dd.data["_demo_tasks"] = [
        {"title": "Спринт-1: База", "status": "done"},
        {"title": "Спринт-2: UI", "status": "in_progress"},
    ]
    dd.data["_demo_results"] = []
    dd.data["_demo_retros"] = []

def clear_all_state():
    """Полная очистка данных и сброс в дефолтное состояние."""
    reset_demo_data()
    import demo_data as dd
    for key in list(dd.data.keys()):
        if key.startswith("_user") or key.startswith("_session"):
            del dd.data[key]

def print_status():
    """Вывести текущее количество фокусов, задач и результатов."""
    import demo_data as dd
    print(f"Фокусы: {len(dd.data.get('_demo_focuses', []))}")
    print(f"Задачи: {len(dd.data.get('_demo_tasks', []))}")
    print(f"Результаты: {len(dd.data.get('_demo_results', []))}")
    print(f"Ретро: {len(dd.data.get('_demo_retros', []))}")
