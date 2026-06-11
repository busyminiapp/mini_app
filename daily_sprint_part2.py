# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: DailySprint
class SprintData:
    def __init__(self, focus: str, tasks: list[str], outcome: str = "", retro: str = ""):
        self.focus = focus
        self.tasks = tasks
        self.outcome = outcome
        self.retro = retro

    @property
    def is_valid(self) -> bool:
        return len(self.focus.strip()) > 0 and len(self.tasks) > 0

class InputValidator:
    MAX_TASKS = 10
    MIN_TASK_LEN = 3
    MAX_TASK_LEN = 50

    @staticmethod
    def validate_input(focus: str, tasks: list[str], outcome: str = "", retro: str = "") -> tuple[bool, list[str]]:
        errors = []
        
        if not focus or len(focus.strip()) == 0:
            errors.append("Фокус должен быть непустым текстом.")
        
        for i, task in enumerate(tasks):
            if not task or len(task.strip()) == 0:
                errors.append(f"Задача #{i+1} не может быть пустой.")
            elif len(task) < InputValidator.MIN_TASK_LEN:
                errors.append(f"Задача #{i+1} слишком короткая (минимум {InputValidator.MIN_TASK_LEN} символов).")
            elif len(task) > InputValidator.MAX_TASK_LEN:
                errors.append(f"Задача #{i+1} слишком длинная (максимум {InputValidator.MAX_TASK_LEN} символов).")

        if len(tasks) > InputValidator.MAX_TASKS:
            errors.append(f"Максимальное количество задач: {InputValidator.MAX_TASKS}.")

        return len(errors) == 0, errors
