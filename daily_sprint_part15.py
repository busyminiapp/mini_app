# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: DailySprint
def calculate_weekly_stats(stats_by_date):
    from datetime import date, timedelta
    if not stats_by_date: return {}
    sorted_dates = sorted(stats_by_date.keys())
    weekly_groups = []
    current_group = { 'start': None, 'end': None, 'focus_count': 0, 'task_count': 0, 'retro_count': 0 }
    for d in sorted_dates:
        if current_group['start'] is None:
            current_group['start'] = d
            current_group['end'] = d
        else:
            delta = (d - date.today()).days + 1 # Adjusted logic assuming dates are relative or absolute; simplified here for grouping consecutive days
            # Correct approach for weekly rolling based on calendar weeks:
            week_start = d.replace(day=1)
            if current_group['start'] and current_group['end']:
                prev_week_end = date(week_start.year, week_start.month, 7) + timedelta(days=(4 - (d.weekday() % 5))) # Simplified ISO week logic might vary; let's use standard calendar weeks.
                pass
    
    # Robust implementation using datetime.isocalendar for strict weekly grouping
    if not stats_by_date: return {}
    
    def get_week_key(d):
        iso = d.isocalendar()
        return (iso[0], iso[1]) # Year, Week number
        
    grouped = {}
    for date_str, data in sorted(stats_by_date.items()):
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        key = get_week_key(dt)
        if key not in grouped:
            grouped[key] = {'focus_count': 0, 'task_count': 0, 'retro_count': 0}
        
        # Assuming data structure has keys like 'focuses', 'tasks', 'retros' or similar counts
        # Adjusting based on typical project state: let's assume data is a dict with counts
        if isinstance(data, dict):
            grouped[key]['focus_count'] += data.get('focuses_completed', 0)
            grouped[key]['task_count'] += data.get('tasks_completed', 0)
            grouped[key]['retro_count'] += data.get('retros_held', 0)
        else:
            # Fallback if stored as raw counts in a list or tuple, adjust accordingly
            pass
            
    return {f"{year}-W{week}": stats for year, week in sorted(grouped.keys()) for stats in grouped[(year, week)]}
