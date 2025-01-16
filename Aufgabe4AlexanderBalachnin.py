"""
Schreiben Sie eine Funktion, die Ihnen einen längeren Text (z. B. die im heutigen Unterricht erlernten Themen) über die Konsole einliest, 
jeden "." (Punkt) durch "SNAKE_WAS_HERE" ersetzt und den bearbeiteten Text dann in einer snake.txt abspeichert.

Hinweis: Überlegen Sie sich eine sinnvolle Möglichkeit, wie Sie auch Texte über mehrere Zeilen eingeben können!
"""

# Eingabe vom Nutzer
benutzer_input = input("Gib einen längeren Text ein:\n")

# Funktion
def SnakeErsatz():
    neuer_text = benutzer_input.replace(".", "SNAKE_WAS_HERE")
    with open("Snake.txt", "W") as file:
        file.write(neuer_text)
        
        

# Lesen
with open("Snake.txt", "r") as file:
    content = file.read()
print("Inhalt der Datei:", content)





