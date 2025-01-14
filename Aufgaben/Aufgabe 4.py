# ### Aufgabe 4
# Schreiben Sie eine Funktion, die Ihnen einen längeren Text (z. B. die im heutigen Unterricht erlernten Themen)
# über die Konsole einliest, jeden **"." (Punkt)** durch **"SNAKE_WAS_HERE"** ersetzt und den bearbeiteten Text dann in einer **snake.txt** abspeichert.

# > *Hinweis*: Überlegen Sie sich eine sinnvolle Möglichkeit, wie Sie auch Texte über mehrere Zeilen eingeben können!

def replace_and_save():
    # Eingabe des Textes über mehrere Zeilen
    print("Geben Sie den Text ein (mit 'stop' beenden):")
    
    text = ""
    
    while True:
        # Jede Zeile einlesen
        line = input()
        
        # Beenden der Eingabe, wenn 'stop' eingegeben wird
        if line.lower() == "stop":
            break
        
        # Hängt die Zeile an den Text an
        text += line + "\n"
    
    # Ersetzen des Punktes durch "SNAKE_WAS_HERE"
    modified_text = text.replace(".", "SNAKE_WAS_HERE")
    
    # Ändern des Pfades: Hier wird die Datei im spezifischen Verzeichnis gespeichert
    output_path = "c:/Users/IT-User/python-playground/Aufgaben/snake.txt"

    # Speichern des bearbeiteten Textes in der Datei
    # Der bearbeitete Text wird in einer Datei namens snake.txt gespeichert
    # Die Datei wird im Schreibmodus ("w") geöffnet. Falls die Datei bereits existiert, wird sie überschrieben
    with open(output_path, "w") as file:
        file.write(modified_text)
    
    print("Text wurde erfolgreich bearbeitet und in 'snake.txt' gespeichert.")

# Aufruf der Funktion
replace_and_save()
