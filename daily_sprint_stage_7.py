# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: DailySprint
def sort_records(records, key='date'):
    if not records: return []
    def parse_date(r):
        try:
            dt = datetime.fromisoformat(r['date'].replace('Z', '+00:00'))
            return (dt.year, dt.month, dt.day)
        except: return (9999, 12, 31)
    if key == 'priority':
        priority_map = {'high': -1, 'medium': 0, 'low': 1}
        return sorted(records, key=lambda r: (r.get('completed', False), priority_map.get(r.get('priority', 'medium'), 0)))
    elif key == 'name':
        return sorted(records, key=lambda r: r.get('title', '').lower())
    else: # date default
        return sorted(records, key=lambda r: parse_date(r))
