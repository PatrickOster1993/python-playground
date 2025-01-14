# ### Aufgabe 3
# Implementieren Sie das klassische **FizzBuzz-Spiel**. Schreiben Sie hierzu ein Programm, das die Zahlen von 1 bis 100 ausgibt, aber für Vielfache von 3 soll es **„Fizz“** ausgeben,
# für Vielfache von 5 **„Buzz“** und für Vielfache von sowohl 3 als auch 5 **„FizzBuzz“**.

# > **Tipp**: Wie wäre es mit dem Modulo-Operator?

##############################
# FizzBuzz mit Modulo-Operator
# for zahl in range(1, 101):
#     if zahl % 3 == 0 and zahl % 5 == 0:
#         print("FizzBuzz")
#     elif zahl % 3 == 0:
#         print("Fizz")
#     elif zahl % 5 == 0:
#         print("Buzz")
#     else:
#         print(zahl)

###############################
# FizzBuzz ohne Modulo-Operator
zähler_3 = 0
zähler_5 = 0

for zahl in range(1, 101):
    zähler_3 += 1
    zähler_5 += 1
    
    ausgabe = ""
    
    if zähler_3 == 3:
        ausgabe += "Fizz"
        zähler_3 = 0  
    
    if zähler_5 == 5:
        ausgabe += "Buzz"
        zähler_5 = 0  
    
    if not ausgabe:
        ausgabe = str(zahl)
    
    print(ausgabe)