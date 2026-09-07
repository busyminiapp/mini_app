# === Stage 45: Добавь восстановление из резервной копии ===
# Project: DailySprint
import json
import os

BACKUP_FILE = "dailysprint_backup.json"

def load_backup():
    if not os.path.exists(BACKUP_FILE):
        return None
    with open(BACKUP_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def restore_backup(data):
    if data is None:
        print("Резервная копия не найдена.")
        return
    with open("dailysprint.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Резервная копия восстановлена из {BACKUP_FILE}")
