# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: DailySprint
def print_sprint_record(sprint):
    if not sprint:
        return "Нет записей."
    lines = [f"📅 {sprint['date']} | 🎯 Фокус: {sprint['focus']}", f"   Задачи:",
             *[f"     ✅ {t}" for t in sprint.get('tasks', [])], f"   Итоги:",
             *[f"     • {r}" for r in sprint.get('outcomes', [])]]
    if sprint.get('retro'):
        lines.append(f"   Ретро: {sprint['retro']}")
    print("\n".join(lines))

def main():
    data = [
        {"date": "2025-01-06", "focus": "Улучшить UI", "tasks": ["Переделать карточки", "Добавить фильтр"], "outcomes": ["Скорость выросла на 30%"], "retro": "Нужно больше тестов"},
        {"date": "2025-01-07", "focus": "Написать докстринг", "tasks": ["API доки", "README"], "outcomes": []}
    ]
    print_sprint_record(data[0])
