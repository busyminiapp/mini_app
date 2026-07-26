# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: DailySprint
class SprintProfile:
    def __init__(self, name, daily_focus, tasks_per_sprint=3):
        self.name = name
        self.daily_focus = daily_focus
        self.tasks_per_sprint = tasks_per_sprint

    def to_dict(self):
        return {"name": self.name, "daily_focus": self.daily_focus, "tasks_per_sprint": self.tasks_per_sprint}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["daily_focus"], data.get("tasks_per_sprint", 3))


class ProfileManager:
    _profiles = {}

    @staticmethod
    def register_profile(name, daily_focus, tasks_per_sprint=3):
        if name in ProfileManager._profiles:
            raise ValueError(f"Profile '{name}' already exists")
        ProfileManager._profiles[name] = SprintProfile(name, daily_focus, tasks_per_sprint)

    @staticmethod
    def get_profile(name):
        return ProfileManager._profiles.get(name)

    @staticmethod
    def list_profiles():
        return list(ProfileManager._profiles.values())

    @staticmethod
    def remove_profile(name):
        if name in ProfileManager._profiles:
            del ProfileManager._profiles[name]
            return True
        return False
