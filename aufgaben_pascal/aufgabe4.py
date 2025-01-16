try:
    lines = []
    print("Geben Sie Zeilen ein (leere Eingabe beendet):")
    
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    original_text = "\n".join(lines)  # Zeilen miteinander verbinden
    modified_text = original_text.replace(".", "SNAKE_WAS_HERE")  # Punkte ersetzen

    with open("snake.txt", "w", encoding="utf-8") as file:
        file.write(modified_text)

    print("Ihr Text wurde in 'snake.txt' gespeichert.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
