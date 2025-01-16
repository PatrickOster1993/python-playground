

bool = True



while bool == True:
    celsiusOderFahrenheit = input("Wählen Sie '1' um eine Temperatur von Celsius in Fahrenheit umzuwandeln oder '2' um eine Temperatur von Fahrenheit in Celsius umzuwandeln\n")
    if celsiusOderFahrenheit == "1":
        UserEingabe = float(input("Geben Sie die Temperatur in Celsius an um diese in Fahrenheit umzuwandeln:\n"))
        TemperaturAusgabe = 1.8 * UserEingabe + 32
        print(f"{UserEingabe}° Celsius in Fahrenheit ist {TemperaturAusgabe} F\n")
    elif celsiusOderFahrenheit == "2":
        UserEingabe = float(input("Geben Sie eine Temperatur in Fahrenheit ein um diese in ° Celsius umzuwandeln:\n"))
        TemperaturAusgabe = (UserEingabe-32)*5/9
        print(f"{UserEingabe} F entspricht {TemperaturAusgabe} in ° Celsius\n")
    elif celsiusOderFahrenheit == "3":
        bool = False
    else:
        print("Ungültige Eingabe")



