# === Stage 20: Добавь восстановление записей из архива ===
# Project: DailySprint
def archive_recovery():
    """Восстанавливает записи из архива, если они были сохранены ранее."""
    import json
    from pathlib import Path
    ARCHIVE_PATH = Path(__file__).parent / "archive.json"
    if not ARCHIVE_PATH.exists():
        return None
    try:
        with open(ARCHIVE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        elif isinstance(data, dict):
            return [data]
        else:
            raise ValueError("Неверный формат архива")
    except Exception as e:
        print(f"Ошибка загрузки архива: {e}")
        return None
