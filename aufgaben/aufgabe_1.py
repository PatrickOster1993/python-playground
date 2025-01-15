name = input("Wie heißt du? ")
alter = input("Wie alt bist du? ")
lieblingsessen = input("Was ist dein Lieblingsessen? ")

personen_daten = {
    "Name": name,
    "Alter": alter,
    "Lieblingsessen": lieblingsessen
}

print(f"Hallo {personen_daten['Name']}, du bist {personen_daten['Alter']} Jahre alt und dein Lieblingsessen ist {personen_daten['Lieblingsessen']}.")
