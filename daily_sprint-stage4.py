# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: DailySprint
def edit_sprint_record(record_id, updates):
    if record_id not in sprint_records:
        print(f"Запись с ID {record_id} не найдена.")
        return False
    
    for key, value in updates.items():
        if key in sprint_record_schema and key != 'id':
            sprint_records[record_id][key] = value
        else:
            print(f"Недопустимое поле для редактирования: {key}")
    
    print(f"Запись с ID {record_id} успешно обновлена.")
    return True

# Пример вызова (раскомментируйте при необходимости):
# edit_sprint_record(1, {'focus': 'Изучить Playwright', 'tasks': ['Установить зависимости']})
