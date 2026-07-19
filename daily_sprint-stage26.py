# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: DailySprint
def demo():
    print("=== DailySprint Demo ===")
    sprint = Sprint()
    sprint.set_date("2024-03-15")
    sprint.add_focus("Исследовать API")
    sprint.add_task(Task("Изучить Swagger", "Описать эндпоинты"))
    sprint.add_task(Task("Написать тесты", "Закрыть 80% покрываемость"))
    sprint.set_result(9, 7)
    sprint.set_retro("Были готовы к API, но мало времени")
    sprint.save()

    sprints = load_sprints()
    for sp in sprints:
        print(f"Дата: {sp.date}, Фокусы: {', '.join(sp.focuses)}, Результат: {sp.result}, Ретро: {sp.retro}")
