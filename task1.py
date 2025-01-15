# ### Aufgabe 1
# Erstellen Sie ein Programm, das Ihren **Namen**, Ihr **Alter** und Ihr **Lieblingsessen** über eine Konsoleneingabe einliest. Geben Sie diese Informationen dann in einem Satz aus.
# > z. B.: „Hallo Max, du bist 25 Jahre alt und dein Lieblingsessen ist Pizza.“

print("Aufgabe 1")
print("Bitte geben Sie Ihren Namen, Ihr Alter und Ihr Lieblingsessen ein.")
print("Name:")
name = input()
# Exception-Handling für die Eingabe des Alters
while True:
    try:
        alter = int(input("Alter:"))
        if alter < 0:
            print("Bitte geben Sie ein Alter größer oder gleich 0 ein.")
        else:
            break
    except ValueError:
        print("Bitte geben Sie eine gültige Zahl für das Alter ein.")
print("Lieblingsessen:")
lieblingsessen = input()
while True:
    if lieblingsessen:
        break
    else:
        print("Bitte geben Sie ein Lieblingsessen ein.")
        lieblingsessen = input()
print("Hallo " + name + ", du bist " + str(alter) + " Jahre alt und dein Lieblingsessen ist " + lieblingsessen + ".")
