# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: DailySprint
TEMPLATES = {
    "daily_sprint": {
        "focuses": ["Фокус 1", "Фокус 2"],
        "tasks": [],
        "results": {},
        "retro": ""
    },
    "task_only": {
        "focuses": [],
        "tasks": [{"title": "Задача 1", "done": False, "notes": "", "priority": "medium"}],
        "results": {},
        "retro": ""
    }
}

def apply_template(name):
    if name not in TEMPLATES:
        raise ValueError(f"Нет шаблона: {name}")
    template = TEMPLATES[name]
    sprint = {k: v[:] for k, v in template.items()}
    return sprint
