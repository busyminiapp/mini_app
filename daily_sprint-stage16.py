# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: DailySprint
def calculate_monthly_stats(sprints_data):
    from collections import defaultdict
    stats = defaultdict(lambda: {'focuses': 0, 'tasks_completed': 0, 'retros_count': 0})
    for sprint in sprints_data:
        date_str = sprint.get('date') or sprint.get('created_at', '')[:7]  # YYYY-MM
        if not date_str: continue
        stats[date_str]['focuses'] += len(sprint.get('focuses', []))
        stats[date_str]['tasks_completed'] += sum(1 for t in sprint.get('tasks', []) if t.get('completed'))
        stats[date_str]['retros_count'] += 1
    return sorted(stats.items(), key=lambda x: x[0])
