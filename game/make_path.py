import os
import sys

def resource_path(relative_path):
    """Получить абсолютный путь к ресурсу, работает для разработки и PyInstaller"""
    try:
        # PyInstaller создает временную папку и сохраняет путь в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Если это не PyInstaller, используем текущую папку
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)