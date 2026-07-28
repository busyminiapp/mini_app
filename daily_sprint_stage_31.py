# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: DailySprint
def switch_profile(profile_id):
    if not profiles:
        print("Нет сохранённых профилей.")
        return False
    profile = next((p for p in profiles if p["id"] == profile_id), None)
    if not profile:
        print(f"Профиль с id={profile_id} не найден.")
        return False
    active_profile["name"] = profile["name"]
    active_profile["role"] = profile.get("role", "dev")
    active_profile["daily_goal"] = profile.get("daily_goal", 3)
    print(f"Переключено на профиль: {active_profile['name']} ({profile['role']})")
    return True
