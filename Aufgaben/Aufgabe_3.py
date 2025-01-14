"""
Aufgabe 3
Implementieren Sie das klassische **FizzBuzz-Spiel**. Schreiben Sie hierzu ein Programm, 
das die Zahlen von 1 bis 100 ausgibt, aber für Vielfache von 3 soll es **„Fizz“** ausgeben, 
für Vielfache von 5 **„Buzz“** und für Vielfache von sowohl 3 als auch 5 **„FizzBuzz“**.
WHAT THE HELL IS A FIZZBUZZ?!
Quelle
https://stackoverflow.com/questions/22743860/python-fizzbuzz
"""

c=1
while c<101:print((c%3<1)*'Fizz'+(c%5<1)*'Buzz'or c);c+=1

"""
# Prüft, ob c durch 3 teilbar ist:
    # - Der Ausdruck c % 3 gibt den Rest der Division von c durch 3 zurück.
    # - Wenn der Rest 0 ist, bedeutet das, dass c durch 3 teilbar ist.
    # - Der Vergleich c % 3 < 1 ist wahr (True), wenn c % 3 == 0, da 0 < 1.
    # - Wenn c durch 3 teilbar ist, wird 'Fizz' ausgegeben.
    #
    # Prüft, ob c durch 5 teilbar ist:
    # - Analog funktioniert c % 5 < 1, was True ist, wenn c % 5 == 0.
    # - Wenn c durch 5 teilbar ist, wird 'Buzz' ausgegeben.
    #
    # Der Ausdruck kombiniert beide Prüfungen und gibt:
    # - 'FizzBuzz', wenn c durch 3 und 5 teilbar ist,
    # - 'Fizz', wenn nur durch 3 teilbar,
    # - 'Buzz', wenn nur durch 5 teilbar,
    # - oder die Zahl selbst, wenn keine Teilbarkeit vorliegt.
"""
