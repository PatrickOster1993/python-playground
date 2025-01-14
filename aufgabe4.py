# ### Aufgabe 4
# Schreiben Sie eine Funktion, die Ihnen einen längeren Text (z. B. die im heutigen Unterricht erlernten Themen) über die Konsole einliest, jeden **"." (Punkt)** durch **"SNAKE_WAS_HERE"** ersetzt und den bearbeiteten Text dann in einer **snake.txt** abspeichert.

# > *Hinweis*: Überlegen Sie sich eine sinnvolle Möglichkeit, wie Sie auch Texte über mehrere Zeilen eingeben können!

text = ""
while True:
    line = input("Gib eine Zeile Text ein (leer lassen zum Beenden): ")
    if line == "":
        break
    text += line + "\n"

text = text.replace(".", "SNAKE_WAS_HERE")
with open("snake.txt", "w") as file:
    file.write(text)