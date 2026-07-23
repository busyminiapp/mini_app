# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: DailySprint
def count_project_metrics():
    """Подсчёт ключевых метрик проекта DailySprint."""
    total_sprints = 0
    completed_sprints = 0
    total_tasks = 0
    completed_tasks = 0
    
    with open("project_stats.txt", "w") as f:
        for line in file_lines:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            
            if stripped.startswith("SPRINT"):
                total_sprints += 1
                if "COMPLETED" in stripped.upper():
                    completed_sprints += 1
            elif stripped.startswith("TASK") and "COMPLETED" in stripped.upper():
                total_tasks += 1
                completed_tasks += 1
    
    print(f"Всего спринтов: {total_sprints}")
    print(f"Завершённых спринтов: {completed_sprints}")
    
    if total_sprints > 0:
        completion_rate = (completed_sprints / total_sprints) * 100
        print(f"Процент завершения спринтов: {completion_rate:.2f}%")
    
    return {
        "total_sprints": total_sprints,
        "completed_sprints": completed_sprints,
        "task_completion_count": completed_tasks,
        "sprint_completion_percentage": completion_rate if total_sprints > 0 else 0.0
    }

# Пример использования:
metrics = count_project_metrics()
