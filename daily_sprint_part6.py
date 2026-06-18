# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: DailySprint
def filter_sprints(sprints, status=None, category=None, tags=None):
    if not sprints: return []
    filtered = [s for s in sprints]
    if status is not None: filtered = [s for s in filtered if s.get('status') == status]
    if category is not None: filtered = [s for s in filtered if s.get('category') == category]
    if tags is not None: filtered = [s for s in filtered if set(tags).issubset(set(s.get('tags', [])))]
    return filtered
