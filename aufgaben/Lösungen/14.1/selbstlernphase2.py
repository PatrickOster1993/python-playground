""" def temprechnerF_C():
    return (degrees -32) / 1.8

def temprechnerC_F():
    return degrees * 1.8 + 32

print("Temperatur Umrechner")
print("Welche umrechner brauchen Sie?")
print("1: Fahrenheit nach Normal")
print("2: Normal nach Fahrenheit")
choice = input("Ihre Entscheidung lautet: ")
input_degrees = input("Und wieviel Grad? ")
degrees = float(input_degrees)

if choice == "1":
    output = temprechnerF_C()
    print(f"{input_degrees} Fahrenheit ist {output} Celsius.")

elif choice == "2":
    output = temprechnerC_F()
    print(f"{input_degrees} Celsius ist {output} Fahrenheit.")

else:
    print("Bitte 1 oder 2 eingeben.") """

temp_rechner = {
    "1": lambda degrees: (degrees -32) / 1.8,
    "2": lambda degrees: degrees * 1.8 + 32,
}

grad_anzeige = {
    "1": "Celsius",
    "2": "Fahrenheit",
}

print("Temperatur Umrechner")
print("Welche umrechner brauchen Sie?")
print("1: Fahrenheit nach Normal")
print("2: Normal nach Fahrenheit")
choice = input("Ihre Entscheidung lautet: ")
isFloat = False

while(isFloat == False):
    try:
        degrees = float(input("Und wieviel Grad? "))
        isFloat = True
    except ValueError:
        print("Keine Zahl angegeben")
    result = temp_rechner[choice](degrees)

try:
    if choice == "1":
        print(f"{degrees} Grad in {grad_anzeige["2"]} ist {result} in {grad_anzeige['1']}.")
    elif choice == "2":
        print(f"{degrees} Grad in {grad_anzeige["1"]} ist {result} in {grad_anzeige['2']}.")
    else:
        print("Bitte 1 oder 2 eingeben.")
except ValueError:
    print("Bitte ein Zahl eingeben.")
except Exception:
    print("Unerwartete Kritische Fehler, Ihre Festplatte wird jetzt gelöscht.")