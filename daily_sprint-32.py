# === Stage 32: Добавь журнал действий пользователя ===
# Project: DailySprint
class ActionLog:
    def __init__(self):
        self.entries = []
    
    def log(self, user, action_type, details=""):
        entry = {
            "user": user,
            "timestamp": datetime.now().isoformat(),
            "action": action_type,
            "details": details
        }
        self.entries.append(entry)
        return entry
    
    def get_log(self):
        return list(reversed(self.entries))
    
    def clear_log(self):
        self.entries.clear()
