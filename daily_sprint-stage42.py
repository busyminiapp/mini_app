# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: DailySprint
import sys

if sys.platform == "win32":
    _colors_off = True
else:
    _colors_off = False


def _reset():
    if _colors_off:
        return
    sys.stdout.write("\033[0m")


def _bold(text):
    if _colors_off:
        return text
    return f"\033[1m{text}\033[0m"


def _red(text):
    if _colors_off:
        return text
    return f"\033[31m{text}\033[0m"


def _green(text):
    if _colors_off:
        return text
    return f"\033[32m{text}\033[0m"


def _yellow(text):
    if _colors_off:
        return text
    return f"\033[33m{text}\033[0m"


def _cyan(text):
    if _colors_off:
        return text
    return f"\033[36m{text}\033[0m"


def _magenta(text):
    if _colors_off:
        return text
    return f"\033[35m{text}\033[0m"


def _white(text):
    if _colors_off:
        return text
    return f"\033[37m{text}\033[0m"


def _bright_red(text):
    if _colors_off:
        return text
    return f"\033[91m{text}\033[0m"


def _bright_green(text):
    if _colors_off:
        return text
    return f"\033[92m{text}\033[0m"


def _bright_yellow(text):
    if _colors_off:
        return text
    return f"\033[93m{text}\033[0m"


def _bright_cyan(text):
    if _colors_off:
        return text
    return f"\033[96m{text}\033[0m"


def _bright_magenta(text):
    if _colors_off:
        return text
    return f"\033[95m{text}\033[0m"


def _bright_white(text):
    if _colors_off:
        return text
    return f"\033[97m{text}\033[0m"
