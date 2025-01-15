"""
Aufgabe 4
Schreiben Sie eine Funktion, die Ihnen einen längeren Text (z. B. die im heutigen Unterricht erlernten Themen) 
über die Konsole einliest, jeden **"." (Punkt)** durch **"SNAKE_WAS_HERE"** ersetzt und den bearbeiteten 
Text dann in einer **snake.txt** abspeichert.

> *Hinweis*: Überlegen Sie sich eine sinnvolle Möglichkeit, wie Sie auch Texte über mehrere Zeilen eingeben können!
"""

# Nutzer auffordern, Text einzugeben
print("Geben Sie Ihren Text ein (mehrzeilig möglich).")
print("Drücken Sie ENTER nach jeder Zeile und eine leere Zeile, um die Eingabe zu beenden.")

# Text einlesen
text = ""  # Leerer String, um den Text zu speichern
while True:
    line = input()  # Zeile vom Nutzer einlesen
    if line == "":  # Wenn die Eingabe leer ist, die Schleife beenden
        break
    text += line + "\n"  # Zeile zum Text hinzufügen, mit Zeilenumbruch

# Punkte durch "SNAKE_WAS_HERE" ersetzen
text = text.replace(".", "SNAKE_WAS_HERE")

# In Datei speichern
with open("snake.txt", "w") as file:
    file.write(text)

# Erfolgsnachricht
print("Der bearbeitete Text wurde in 'snake.txt' gespeichert!")

""""""