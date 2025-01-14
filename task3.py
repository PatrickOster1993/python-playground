# ### Aufgabe 3
# Implementieren Sie das klassische **FizzBuzz-Spiel**. Schreiben Sie hierzu ein Programm, das die Zahlen von 1 bis 100 ausgibt, aber für Vielfache von 3 soll es **„Fizz“** ausgeben, für Vielfache von 5 **„Buzz“** und für Vielfache von sowohl 3 als auch 5 **„FizzBuzz“**.

# > **Tipp**: Wie wäre es mit dem Modulo-Operator?

# > **Anmerkung**: Geben Sie das Ergebnis bitte als Antwortsatz aus!

print("Aufgabe 3") # Ausgabe des Titels der Aufgabe
for i in range(1, 101): # Schleife von 1 bis 100
    if i % 3 == 0 and i % 5 == 0: # Wenn i durch 3 und 5 teilbar ist
        print("FizzBuzz") # Ausgabe von "FizzBuzz"
    elif i % 3 == 0: # Wenn i durch 3 teilbar ist
        print("Fizz") # Ausgabe von "Fizz"
    elif i % 5 == 0: # Wenn i durch 5 teilbar ist
        print("Buzz") # Ausgabe von "Buzz"
    else: # Wenn i weder durch 3 noch durch 5 teilbar ist
        print(i) # Ausgabe von i
# Ende des Programms
