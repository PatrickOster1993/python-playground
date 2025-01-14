def temprechnerF_C():
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
    print("Bitte 1 oder 2 eingeben.")