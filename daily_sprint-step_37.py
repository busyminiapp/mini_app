# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: DailySprint
import unittest
from datetime import datetime, timedelta


class TestDailySprint(unittest.TestCase):
    def test_add_task(self):
        sprint = DailySprint()
        sprint.add_focus("Фокус 1")
        sprint.add_task("Задача 1", "Фокус 1", 45)
        sprint.add_task("Задача 2", "Фокус 1", 30)
        self.assertEqual(len(sprint.tasks), 2)
        self.assertEqual(sprint.tasks[0].name, "Задача 1")
        self.assertEqual(sprint.tasks[0].focus, "Фокус 1")
        self.assertEqual(sprint.tasks[0].duration, 45)

    def test_add_result(self):
        sprint = DailySprint()
        sprint.add_focus("Фокус 1")
        sprint.add_task("Задача 1", "Фокус 1", 45)
        sprint.add_result("Задача 1", "Готово", 35)
        self.assertEqual(len(sprint.results), 1)
        self.assertEqual(sprint.results[0].name, "Задача 1")
        self.assertEqual(sprint.results[0].status, "Готово")
        self.assertEqual(sprint.results[0].actual_duration, 35)

    def test_add_retro(self):
        sprint = DailySprint()
        sprint.add_focus("Фокус 1")
        sprint.add_task("Задача 1", "Фокус 1", 45)
        retro = SprintRetro("Фокус 1")
        retro.add_sprint(sprint)
        retro.add_comment("Сделали задачу за 35 минут")
        retro.add_comment("Нужно меньше отвлекающих факторов")
        self.assertEqual(len(retro.comments), 2)
        self.assertIn("Сделали задачу за 35 минут", retro.comments[0])

    def test_add_summary(self):
        sprint = DailySprint()
        sprint.add_focus("Фокус 1")
        sprint.add_task("Задача 1", "Фокус 1", 45)
        sprint.add_result("Задача 1", "Готово", 35)
        summary = SprintSummary("Фокус 1")
        summary.add_sprint(sprint)
        summary.add_result("Задача 1", "Готово", 35)
        summary.add_focus("Фокус 1")
        self.assertEqual(summary.title, "Фокус 1")
        self.assertEqual(len(summary.results), 1)
        self.assertEqual(summary.results[0].name, "Задача 1")
        self.assertEqual(summary.results[0].status, "Готово")


if __name__ == "__main__":
    unittest.main()
