# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: DailySprint
import datetime

def schedule_reminder(task, date):
    """Создает напоминание для задачи с указанной датой."""
    return {
        "task": task,
        "date": date,
        "status": "pending",
        "reminder_time": None
    }


def get_upcoming_reminders(reminders_list):
    """Возвращает список напоминаний сортированных по дате."""
    today = datetime.date.today()
    upcoming = [r for r in reminders_list if r["date"] >= today]
    upcoming.sort(key=lambda x: x["date"])
    return upcoming


def mark_reminder_done(reminders_list, reminder_id):
    """Отмечает напоминание как выполненное."""
    for reminder in reminders_list:
        if reminder["task"].get("id") == reminder_id:
            reminder["status"] = "done"
            return True
    return False


def show_reminder_summary(reminders_list):
    """Показывает краткую статистику напоминаний."""
    total = len(reminders_list)
    done = sum(1 for r in reminders_list if r["status"] == "done")
    pending = total - done
    return f"Всего: {total}, Выполнено: {done}, Осталось: {pending}"


if __name__ == "__main__":
    reminders = [
        schedule_reminder({"id": 1, "title": "Написать отчёт"}, datetime.date(2024, 3, 15)),
        schedule_reminder({"id": 2, "title": "Обсудить ретро"}, datetime.date(2024, 3, 20)),
    ]

    print(show_reminder_summary(reminders))
    upcoming = get_upcoming_reminders(reminders)
    for r in upcoming:
        print(f"Напоминание: {r['task']['title']} на {r['date']}")
