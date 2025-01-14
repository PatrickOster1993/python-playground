# ### Aufgabe 4
# Schreiben Sie eine Funktion, die Ihnen einen längeren Text (z. B. die im heutigen Unterricht erlernten Themen) über die Konsole einliest, jeden **"." (Punkt)** durch **"SNAKE_WAS_HERE"** ersetzt und den bearbeiteten Text dann in einer **snake.txt** abspeichert.

# > *Hinweis*: Überlegen Sie sich eine sinnvolle Möglichkeit, wie Sie auch Texte über mehrere Zeilen eingeben können!

# > **Anmerkung**: Geben Sie das Ergebnis bitte als Antwortsatz aus!

# > **Beispiel**:
# > ```
# > Bitte geben Sie einen Text ein:
# > Hallo. Mein Name ist Snake. Ich bin ein Python.
# > ```
# > ```
# > Der bearbeitete Text wurde in der Datei „snake.txt“ gespeichert.
# > ```
# > **snake.txt**:
# > ```
# > HalloSNAKE_WAS_HERE Mein Name ist SnakeSNAKE_WAS_HERE Ich bin ein PythonSNAKE_WAS_HERE
# > ```
#
# Funktion zum Ersetzen von Punkten
def ersetze_punkte(text):
    return text.replace(".", "SNAKE_WAS_HERE")

print("Aufgabe 4") # Ausgabe des Titels der Aufgabe
print("Bitte geben Sie einen längeren Text ein:")
text = input() # Eingabe des Textes
text = ersetze_punkte(text) # Ersetzen von Punkten
with open("snake.txt", "w") as file: # Öffnen der Datei
    file.write(text) # Schreiben des bearbeiteten Textes in die Datei
print("Der bearbeitete Text wurde in der Datei „snake.txt“ gespeichert.") # Ausgabe des Erfolgs
# Ende des Programms
