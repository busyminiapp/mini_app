# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: DailySprint
class DailySprint:
    def __init__(self):
        self._records = []
    
    def add_focus(self, topic: str) -> None:
        record = {"type": "focus", "topic": topic}
        self._records.append(record)
    
    def add_task(self, description: str, status: str = "todo") -> None:
        record = {"type": "task", "description": description, "status": status}
        self._records.append(record)
    
    def add_result(self, achievement: str) -> None:
        record = {"type": "result", "achievement": achievement}
        self._records.append(record)
    
    def add_retro(self, feedback: str) -> None:
        record = {"type": "retro", "feedback": feedback}
        self._records.append(record)
    
    def get_records(self) -> list:
        return self._records.copy()
