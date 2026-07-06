# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: DailySprint
class SprintTag:
    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Тег должен быть непустой строкой")
        self.name = name.strip()

    def __repr__(self):
        return f"<SprintTag '{self.name}'>"


class Sprint:
    def __init__(self, date=None, focus=None, tasks=None, review=None):
        self.date = date
        self.focus = focus
        self.tasks = tasks or []
        self.review = review
        self.tags = set()

    def add_tag(self, tag_or_name):
        if isinstance(tag_or_name, SprintTag):
            name = tag_or_name.name
        elif isinstance(tag_or_name, str):
            name = tag_or_name.strip()
        else:
            raise TypeError("Передан не тег и не строка")
        self.tags.add(SprintTag(name))

    def remove_tag(self, tag_or_name):
        if isinstance(tag_or_name, SprintTag):
            name = tag_or_name.name
        elif isinstance(tag_or_name, str):
            name = tag_or_name.strip()
        else:
            raise TypeError("Передан не тег и не строка")
        self.tags.discard(SprintTag(name))

    def has_tag(self, tag_or_name):
        if isinstance(tag_or_name, SprintTag):
            return tag_or_name.name in {t.name for t in self.tags}
        return tag_or_name.strip() in {t.name for t in self.tags}
