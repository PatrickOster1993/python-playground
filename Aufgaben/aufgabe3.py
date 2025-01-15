### Aufgabe 3
### Implementieren Sie das klassische **FizzBuzz-Spiel**. Schreiben Sie hierzu ein Programm, das die Zahlen von 1 bis 100 ausgibt, aber für Vielfache von 3 soll es **„Fizz“** ausgeben, für Vielfache von 5 **„Buzz“** und für Vielfache von sowohl 3 als auch 5 **„FizzBuzz“**.
### Tip: Wie wäre es mit dem Modulo-Operator?

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)