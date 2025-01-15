text = ""
while True:
    line = input("Gib eine Zeile Text ein (leer lassen zum Beenden): ")
    if line == "":
        break
    text += line + "\n"

text = text.replace(".", "SNAKE_WAS_HERE")
with open("snake.txt", "w") as file:
    file.write(text)