# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: DailySprint
def delete_entry(entry_type: str, entry_id: int) -> bool:
    if not hasattr(DailySprint, entry_type):
        raise ValueError(f"Unknown entry type: {entry_type}")
    collection = getattr(DailySprint, entry_type)
    if entry_id in collection:
        del collection[entry_id]
        return True
    print(f"Entry with id={entry_id} not found or already deleted.")
    return False

def delete_sprint(sprint_date: str) -> bool:
    sprint_key = f"sprint_{sprint_date}"
    if hasattr(DailySprint, 'focuses') and sprint_key in DailySprint.focuses:
        del DailySprint.focuses[sprint_key]
        return True
    print(f"Sprint for {sprint_date} not found.")
    return False

def delete_task(task_id: int) -> bool:
    if hasattr(DailySprint, 'tasks') and task_id in DailySprint.tasks:
        del DailySprint.tasks[task_id]
        return True
    print(f"Task with id={task_id} not found.")
    return False

def delete_goal(goal_id: int) -> bool:
    if hasattr(DailySprint, 'goals') and goal_id in DailySprint.goals:
        del DailySprint.goals[goal_id]
        return True
    print(f"Goal with id={goal_id} not found.")
    return False

def delete_retro(retro_date: str) -> bool:
    retro_key = f"retro_{retro_date}"
    if hasattr(DailySprint, 'retros') and retro_key in DailySprint.retros:
        del DailySprint.retros[retro_key]
        return True
    print(f"Retro for {retro_date} not found.")
    return False
