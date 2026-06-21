# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: DailySprint
def main():
    print("DailySprint CLI")
    while True:
        cmd = input("\nКоманда (1-Фокус, 2-Задача, 3-Итог, 4-Ретро, 5-Выход): ").strip()
        if not cmd or cmd == "0": break
        elif cmd == "1": focus_input(); print("Фокус сохранен.")
        elif cmd == "2": task_input(); print("Задача добавлена.")
        elif cmd == "3": result_input(); print("Итог записан.")
        elif cmd == "4": retro_input(); print("Ретро проведено.")
        else: print("Неизвестная команда.")

if __name__ == "__main__": main()
