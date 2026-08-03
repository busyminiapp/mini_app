# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: DailySprint
def next_action_suggestion(sprint, todos) -> dict:
    """Сформирует рекомендацию следующего действия на основе текущего состояния спринта."""
    suggestion = {"action": "review", "reason": ""}
    
    if not sprint["focuses"]:
        suggestion.update({"action": "set_focus", "reason": "Нет фокусов — сначала определи, что важно."})
        return suggestion
    
    done_count = sum(1 for t in todos if t.get("done"))
    total_done = len(todos) if todos else 0
    
    if total_done == 0:
        undone = [t for t in todos]
        if not undone:
            suggestion.update({"action": "start_sprint", "reason": "Нет задач — создай хотя бы одну."})
        elif len(undone) == 1:
            suggestion.update({
                "action": "do_task", 
                "task_id": undone[0]["id"],
                "reason": f"Есть одна незавершённая задача #{undone[0]['id']} — сделай её."
            })
        else:
            next_id = min(t["id"] for t in undone)
            suggestion.update({
                "action": "do_task", 
                "task_id": next_id,
                "reason": f"Начни с задачи #{next_id} — она в приоритете."
            })
    elif done_count < total_done:
        remaining = [t for t in todos if not t.get("done")]
        if remaining:
            next_id = min(t["id"] for t in remaining)
            suggestion.update({
                "action": "do_task", 
                "task_id": next_id,
                "reason": f"Продолжай с задачей #{next_id} — она ещё не сделана."
            })
    
    if done_count > 0 and total_done == done_count:
        suggestion.update({"action": "retro", "reason": "Все задачи завершены — проведи ретро."})
    
    return suggestion
