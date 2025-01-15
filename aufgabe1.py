def check_positive(value):
    if value < 0:
        raise ValueError(f"Wert muss positiv sein, aber {value} wurde übergeben.")
    return value

personen_daten = {
    "Name": "",
    "Alter": "",
    "Lieblingsessen": ""
}

personen_daten["Name"] = input("Wie heißt du? ")

while True:
    try:
        age_input = int(input("Bitte geben Sie Ihr Alter ein: "))
        personen_daten["Alter"] = check_positive(age_input)
        break
    except ValueError:
        print("Bitte geben Sie eine positive Zahl ein.")
        continue

personen_daten["Lieblingsessen"] = input("Bitte geben Sie Ihr Lieblingsessen ein: ")

print(f"Hallo {personen_daten["Name"]}, du bist {personen_daten["Alter"]} Jahre alt und dein Lieblingsessen ist {personen_daten['Lieblingsessen']}.")