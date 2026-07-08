# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: DailySprint
def archive_sprint(sprints: dict, cutoff_days=90) -> list:
    """Archive sprints older than cutoff_days (default 90). Returns list of archived sprint IDs."""
    import datetime
    today = datetime.date.today()
    cutoff_date = today - datetime.timedelta(days=cutoff_days)
    archived_ids = []
    for sid, sprint in sprints.items():
        if sprint.get("date", "") and sprint["date"] < cutoff_date:
            sprint["archived_at"] = str(today)
            sprint["status"] = "archived"
            archived_ids.append(sid)
    return archived_ids
