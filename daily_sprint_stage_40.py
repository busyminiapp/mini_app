# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: DailySprint
import argparse

def main():
    parser = argparse.ArgumentParser(description="DailySprint - Планировщик ежедневных спринтов")
    sub = parser.add_subparsers(dest="command", required=True)

    p_plan = sub.add_parser("plan", help="Составить план")
    p_plan.add_argument("--focus", "-f", action="append", help="Фокус для спринта")

    p_tasks = sub.add_parser("tasks", help="Добавить задачи")
    p_tasks.add_argument("--task", "-t", action="append", help="Задача")

    p_summary = sub.add_parser("summary", help="Составить итоги")

    p_retro = sub.add_parser("retro", help="Провести ретро")

    args = parser.parse_args()
    if args.command == "plan" and args.focus:
        print(f"Фокусы спринта: {', '.join(args.focus)}")
    elif args.command == "tasks" and args.task:
        print(f"Задачи: {', '.join(args.task)}")
    elif args.command == "summary":
        print("Итоги спринта сформированы.")
    elif args.command == "retro":
        print("Ретро-встреча проведена.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
