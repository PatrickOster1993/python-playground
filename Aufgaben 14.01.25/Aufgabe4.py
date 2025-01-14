# Aufgabe 4
#Schreiben Sie eine Funktion, die Ihnen einen längeren Text (z. B. die im heutigen Unterricht erlernten Themen)
# über die Konsole einliest, jeden **"." (Punkt)** durch **"SNAKE_WAS_HERE"** ersetzt und
# den bearbeiteten Text dann in einer **snake.txt** abspeichert.

user_input = input("Tragen Sie Ihre Gedanken ein.")

neuer_text = user_input.replace(".", "SNAKE_WAS_HERE")

print("Ersetzter Text:", neuer_text)

#muss noch in snake.txt gespeichert werden 