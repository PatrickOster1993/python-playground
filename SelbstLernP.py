# Aufgabe 1

# Name = input("Wie heißt du?")
# Alter = input("Wie alt bist du?")
# Essen = input("Was ist dein Lieblingsessen?")
# print("Hallo", Name, ",du bist", Alter, "Jahre alt und dein Lieblingsessen ist", Essen)

# Aufgabe 2

def fahrenheit_zu_celsius(fahrenheit):
    return((fahrenheit-32)/1.8)

def celcius_zu_fahrenheit(celsius):
    return(1.8*celsius+32)

print("Celsius - Fahrenheit Rechner:")
print("1. Fahrenheit zu Celsius")
print("2. Celsius zu Fahrenheit")
Auswahl = input("Wie möchten Sie fortfahren? (1. oder 2.)")

if Auswahl =="1":

    fahrenheit = float(input("Temp. in Fahrenheit eingeben."))
    celsius = fahrenheit_zu_celsius(fahrenheit)
    print("Die Temp. in Celsius betrifft:", celsius, "Grad.")

elif Auswahl =="2":

    celsius = float(input("Temp. in Celcius eingeben."))
    fahrenheit = celcius_zu_fahrenheit(celsius)
    print("Die Temp. in Fahrenheit betrifft:", fahrenheit, "Grad.")

else:
    print("Ungültige Eingabe.")

