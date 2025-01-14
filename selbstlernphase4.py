with open("python.md", "r") as file1:
    content = file1.read()
    snake_content = content.replace(".", "**SNAKE_WAS_HERE**")

with open("snake.txt", "w") as file2:
    file2.write(snake_content)
