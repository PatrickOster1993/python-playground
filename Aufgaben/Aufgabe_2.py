"""
Aufgabe 2
Schreiben Sie ein Programm, das eine Temperatur in **Celsius** in **Fahrenheit** umrechnet 
und dann anschließend das Ergebnis in der Konsole ausgibt. Die Umrechnungsformel lautet wie folgt: `F = 1.8 * C + 32`

mit F: Temperatur in **Fahrenheit**;
sowie C: Temperatur in **Celsius**

> **Anmerkung**: Geben Sie das Ergebnis bitte als Antwortsatz aus!

21Quelle
https://stackoverflow.com/questions/69171137/convert-fahrenheit-to-celsius-python
"""

# Temperatur von Celsius in Fahrenheit

celsius = float(input("Gib eine Temperatur in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
#ausgabe 
#print(f"{celsius} Celsius sind: {fahrenheit} Fahrenheit") Altvernative schriebweise wie in Aufgabe_1 (C# ähnlich write.line($))
print(str(celsius) + " Celsius sind: " + str(fahrenheit) + " Fahrenheit")

#eine leere Zeile einfügen für die Übersicht
print()

# Temperatur von Fahrenheit nach Celsius
fahrenheit = float(input("Gib eine Temperarur in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} Fahrenheit sind: {celsius:.0f} Celsius") #Alternativeschreibweise hier funktioniert {celsius:.0f}!!!
#print(str(fahrenheit) + " Fahrenheit sind: " + str(celsius) + " Celsius")

"""
fun fact 33.8 Fahrenheit sind ist Aufgrund der Gleitkommazahlen (Binäre Rechnung) nicht 1 sondern 0.9999999999999984 im PC
man kann mit {celsius.0f} auf keine stelle hinterm komma die zahl runden lassen. 
"""