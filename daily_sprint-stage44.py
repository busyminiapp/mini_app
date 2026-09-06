# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: DailySprint
import shutil
from datetime import datetime

def backup_data_file(filepath: str, backup_dir: str = "backups") -> str:
    """Создаёт резервную копию файла данных с датой в имени."""
    try:
        os.makedirs(backup_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(backup_dir, f"{os.path.basename(filepath)}.backup_{timestamp}")
        shutil.copy2(filepath, backup_path)
        print(f"Backup saved to {backup_path}")
        return backup_path
    except Exception as e:
        print(f"Backup failed: {e}")
        raise e
