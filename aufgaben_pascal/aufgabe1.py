
# Aufgabe 1
# Erstellen Sie ein Programm, das Ihren Namen, Ihr Alter und Ihr Lieblingsessen über eine Konsoleneingabe einliest. Geben Sie diese Informationen dann in einem Satz aus.

# z. B.: „Hallo Max, du bist 25 Jahre alt und dein Lieblingsessen ist Pizza.“


name = input("Wie heißt du?")
age = input("Wie alt bist du?")
fav_food = input("Was ist dein Lieblingsessen?")

print(f"Hallo {name}, du bist {age} Jahre alt und dein Lieblingsessen ist {fav_food}.")




personen_daten = {
    "Name": "",
    "Alter": "",
    "Lieblingsessen": ""
}

personen_daten["Name"] = input("Wie heißt du? ")
personen_daten["Alter"] = input("Wie alt bist du? ")
personen_daten["Lieblingsessen"] = input("Was ist dein Lieblingsessen? ")

print(f"Hallo {personen_daten['Name']}, du bist {personen_daten['Alter']} Jahre alt und dein Lieblingsessen ist {personen_daten['Lieblingsessen']}.")
