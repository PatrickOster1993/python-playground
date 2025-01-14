### Aufgabe 4
### Schreiben Sie eine Funktion, die Ihnen einen längeren Text (z. B. die im heutigen Unterricht erlernten Themen) über die Konsole einliest, jeden **"." (Punkt)** durch **"SNAKE_WAS_HERE"** ersetzt und den bearbeiteten Text dann in einer **snake.txt** abspeichert.
### Hinweis: Überlegen Sie sich eine sinnvolle Möglichkeit, wie Sie auch Texte über mehrere Zeilen eingeben können!

print("Geben Sie den Text ein (beenden Sie die Eingabe mit einer leeren Zeile):")

lines = []
    
while True:
    line = input()
    if line == "!save":
        break 
    lines.append(line)
    
full_text = "\n".join(lines)
    
modified_text = full_text.replace(".", "SNAKE_WAS_HERE")
    
with open("snake.txt", "w") as file:
    file.write(modified_text)
    
print("Der bearbeitete Text wurde in 'snake.txt' gespeichert.")

