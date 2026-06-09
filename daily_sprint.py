# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: DailySprint
def init_demo_data():
    """Инициализация демонстрационных данных для DailySprint."""
    today = "2023-10-27"
    
    # Фокусы дня
    focuses = [
        {"id": 1, "title": "Разработка модуля авторизации", "status": "in_progress"},
        {"id": 2, "title": "Написание документации по API", "status": "todo"}
    ]
    
    # Задачи дня (связанные с фокусами)
    tasks = [
        {"id": 101, "focus_id": 1, "description": "Спроектировать схему БД пользователей", "done": False},
        {"id": 102, "focus_id": 1, "description": "Реализовать валидацию токена", "done": True},
        {"id": 103, "focus_id": 2, "description": "Описать эндпоинт /login", "done": False}
    ]
    
    # Итоги дня (заполняются после работы)
    daily_results = {
        "date": today,
        "completed_tasks_count": 1,
        "notes": "Удалось завершить валидацию токена. Документация пока отложена."
    }
    
    # Ретро-сессия (заполняется вечером)
    retro_session = {
        "date": today,
        "what_went_well": "Быстрая обратная связь от ментора.",
        "improvements": "Нужно лучше планировать время на документацию."
    }
    
    # Хранилище состояния приложения (в памяти для демо)
    app_state = {
        "focuses": focuses,
        "tasks": tasks,
        "daily_results": daily_results,
        "retro_session": retro_session
    }
    
    return app_state
