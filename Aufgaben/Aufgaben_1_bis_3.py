# ### Aufgabe 10
# Erstellen Sie ein Programm, das Ihren **Namen**, Ihr **Alter** und Ihr **Lieblingsessen** über eine Konsoleneingabe einliest. Geben Sie diese Informationen dann in einem Satz aus.

# > z. B.: „Hallo Max, du bist 25 Jahre alt und dein Lieblingsessen ist Pizza.“

# Eingabe vom Nutzer
benutzer_input_name = input("Geben Sie Ihren Namen ein: ")
benutzer_input_alter = input("Geben Sie Ihr Alter ein: ")
benutzer_input_essen = input("Geben Sie Ihr Lieblingsessen ein: ")
# F-String
print(f"Hallo {benutzer_input_name}, du bist {benutzer_input_alter} Jahre alt und dein Lieblingsessen ist {benutzer_input_essen}.")

# String-Konkatenation
print("Hallo " + benutzer_input_name + ", du bist " + str(benutzer_input_alter) + " Jahre alt und dein Lieblingsessen ist " + benutzer_input_essen + ".")

# sep-Parameter
print("Hallo ", benutzer_input_name, ", du bist ", benutzer_input_alter, " Jahre alt und dein Lieblingsessen ist ", benutzer_input_essen, ".", sep="")

