# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: DailySprint
def export_to_json():
    import json
    from datetime import datetime
    state = {
        "daily_sprint": {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "focuses": list(focuses.keys()),
            "tasks": tasks,
            "results": results,
            "retro": retro
        },
        "metadata": {
            "version": "1.0",
            "exported_at": datetime.now().isoformat()
        }
    }
    return json.dumps(state, indent=2, ensure_ascii=False)
