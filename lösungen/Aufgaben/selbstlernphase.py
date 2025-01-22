""" name = input("Gib deinen Namen ein: ")
age = input("Gib dein Alter ein: ")
fav_food = input("Gib dein Lieblingsessen ein: ")

print(f"Hallo {name}, wie gehts? Hast du die letzte Zeit nog {fav_food} gegessen oder bist du mit {age} zu alt für Lieblingsessen?...")
 """

person_data = {
    "Name": "",
    "Age": "",
    "Fav_food": ""
}

person_data["Name"] = input("Wie heißt du? ")
person_data["Age"] = input("Wie alt bist du? ")
person_data["Fav_food"] = input("Was ist dein Lieblingsessen? ")

print(f"Hallo {person_data['Name']}, wie gehts? Hast du die letzte Zeit nog {person_data['Fav_food']} gegessen oder bist du mit {person_data['Age']} zu alt für Lieblingsessen?...")



