import os

def clear_screen():
    """Löscht den Bildschirm, je nach Betriebssystem."""
    os.system("cls" if os.name == "nt" else "clear")
