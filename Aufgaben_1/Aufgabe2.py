
#Aufgabe 2
##Schreiben Sie ein Programm, das eine Temperatur in Celsius in Fahrenheit umrechnet und dann anschließend das Ergebnis in der Konsole ausgibt.
##Die Umrechnungsformel lautet wie folgt: F = 1.8 * C + 32
##mit F: Temperatur in Fahrenheit; sowie C: Temperatur in Celsius
##Anmerkung: Geben Sie das Ergebnis bitte als Antwortsatz aus!

# Eingabe vom Nutzer
eingabe_celsiusinFahrenheit = float(input("Gebe bitte deine Celsius Zahl ein: "))


berechnung  = 1.8 * eingabe_celsiusinFahrenheit + 32

print("Celsius ergibt in Fahrenheit " + str(berechnung) )

