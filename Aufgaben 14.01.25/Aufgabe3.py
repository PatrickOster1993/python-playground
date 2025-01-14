# Aufgabe 3 
# Implementieren Sie das klassische FizzBuzz-Spiel. Schreiben Sie hierzu ein Programm, 
# das die Zahlen von 1 bis 100 ausgibt, aber für Vielfache von 3 soll es „Fizz“ ausgeben,
#  für Vielfache von 5 „Buzz“ und für Vielfache von sowohl 3 als auch 5 „FizzBuzz“.

for zahl in range(1, 101):

    if zahl % 3 == 0:
        print("Fizz")

    if zahl % 5 == 0:
        print("Buzz")

    if zahl % 3 == 0 and zahl % 5 ==0:
        print("FizzBuzz")

    else:
        print(zahl)