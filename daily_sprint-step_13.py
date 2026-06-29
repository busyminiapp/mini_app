# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: DailySprint
def search_sprints(query, fields=None):
    if not query:
        return []
    query = query.lower().strip()
    if fields is None:
        fields = ['focus', 'task', 'result', 'retro']
    results = []
    for sprint in sprints_list:
        match_count = 0
        for field_name in fields:
            value = getattr(sprint, field_name, '')
            if isinstance(value, str):
                if query in value.lower():
                    match_count += 1
        if match_count > 0:
            results.append(sprint)
    return results
