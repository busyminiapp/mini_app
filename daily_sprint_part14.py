# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: DailySprint
def generate_summary(data):
    if not data:
        return "Данные пусты."
    
    today = datetime.now().date()
    sprint_end = (today + timedelta(days=1)).strftime("%Y-%m-%d")
    
    summary_lines = [f"=== Сводка на {sprint_end} ===", f"Фокусов: {len(data.get('focuses', []))}", 
                     f"Задач выполнено: {data.get('completed_tasks_count', 0)}",
                     f"Итого задач сегодня: {data.get('total_tasks_today', 0)}"]
    
    if data.get('retro_notes'):
        summary_lines.append(f"Ретро: {data['retro_notes'][:100]}...")
        
    return "\n".join(summary_lines)
