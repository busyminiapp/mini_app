# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: DailySprint
import json, os

DATA_FILE = "dailysprint_data.json"

def save_state(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_state():
    if not os.path.exists(DATA_FILE):
        return {"sprints": [], "settings": {}}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"sprints": [], "settings": {}}

def get_state():
    state = load_state()
    if not state.get("sprints"):
        save_state({"sprints": [], "settings": {}})
    return state
