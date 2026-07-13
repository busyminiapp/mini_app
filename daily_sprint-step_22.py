# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: DailySprint
def check_overdue_reminders():
    now = datetime.now()
    overdue = []
    for sprint in daily_sprints:
        if sprint.reminder and (now - sprint.reminder) > timedelta(days=1):
            overdue.append(sprint)
    return overdue

if __name__ == "__main__":
    overdue = check_overdue_reminders()
    print(f"Просроченных напоминаний: {len(overdue)}")
