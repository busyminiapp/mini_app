# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: DailySprint
def check_integrity(sprints):
    issues = []
    for i, sprint in enumerate(sprints):
        if not sprint.get("date"):
            issues.append(f"Sprint {i}: missing date")
            continue
        if not sprint.get("focuses"):
            issues.append(f"Sprint {i}: missing focuses")
            continue
        for j, task in enumerate(sprint.get("tasks", [])):
            if not task.get("name"):
                issues.append(f"Sprint {i}, task {j}: missing name")
                continue
            if task.get("status") not in ("todo", "in_progress", "done"):
                issues.append(f"Sprint {i}, task {j}: invalid status '{task['status']}'")
    return issues

def repair_sprints(sprints):
    repaired = []
    for i, sprint in enumerate(sprints):
        new = {}
        if "date" in sprint:
            new["date"] = sprint["date"]
        else:
            new["date"] = "2025-01-01"
        new["focuses"] = sprint.get("focuses", [])
        new["tasks"] = []
        for j, task in enumerate(sprint.get("tasks", [])):
            t = {"name": task.get("name", f"Task {j+1}")}
            if task.get("status") not in ("todo", "in_progress", "done"):
                t["status"] = "todo"
            else:
                t["status"] = task["status"]
            if task.get("description"):
                t["description"] = task["description"]
            new["tasks"].append(t)
        repaired.append(new)
    return repaired
