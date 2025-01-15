lines = []
while True:
    line = input("Gib eine Zeile Text ein (leer lassen zum Beenden): ")
    if line == "":
        break
    lines.append(line + "\n")

text = "".join([line.replace(".", "SNAKE_WAS_HERE") for line in lines])

with open("snake.txt", "w") as file:
    file.write(text)

