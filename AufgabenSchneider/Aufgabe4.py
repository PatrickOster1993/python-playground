# Aufgabe 4
#Schreiben Sie eine Funktion, die Ihnen einen längeren Text (z. B. die im heutigen Unterricht erlernten Themen)
# über die Konsole einliest, jeden **"." (Punkt)** durch **"SNAKE_WAS_HERE"** ersetzt und
# den bearbeiteten Text dann in einer **snake.txt** abspeichert.
try:

    user_input = input("Tragen Sie Ihre Gedanken ein.")

    neuer_text = user_input.replace(".", "SNAKE_WAS_HERE")

    print("Ersetzter Text:", neuer_text)

    with open("snake.txt", "w", encoding="utf-8") as file:
        file.write(neuer_text)

    print("Ihr Text wurde hoffentlich in 'snake.txt' gespeichert...")

except Exception as e:
    print(f"Ein fehler ist aufgetreten: {e}")