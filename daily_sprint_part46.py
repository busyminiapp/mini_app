# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: DailySprint
def migrate_to_v46(records):
    """Миграция структуры данных: добавление поля 'retro_notes' и нормализация 'focus'."""
    new_records = []
    for rec in records:
        new_rec = dict(rec)
        if 'focus' in new_rec and 'focus_notes' in new_rec:
            new_rec['retro_notes'] = new_rec.pop('focus_notes')
        elif 'retro_notes' not in new_rec:
            new_rec['retro_notes'] = ''
        new_records.append(new_rec)
    return new_records
