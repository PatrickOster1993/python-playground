# ### Aufgabe 5 (freiwillig)
# Innerhalb der **playground.py** befindet sich eine Codesequenz, unterhalb des Kommentars mit dem Titel "Experten (nicht erforderlich)". 
# Versuchen Sie den Code selbständig nachzuvollziehen und machen Sie sich ggf. Notizen!

# > *Hinweis*: Die kreativsten Lösungen erlangen stets grenzenlose Ehre!

# Listen
zahlen_liste = [1, 2, 3, 4, 5]
print("Liste:", zahlen_liste[1])

# # List Comprehension -> verdopellt die Werte in der Liste
# verdoppelte_werte = [num * 2 for num in zahlen_liste]
# print("Verdoppelte Werte:", verdoppelte_werte)


# # Lambda-Funktion -> quasi dasselbe wie das dadrunter:
# quadrieren = lambda num: num * num
# print("Quadrat von 4 (Lambda-Funktion):", quadrieren(4))

# def quadrieren(num):
#     return num * num
# print("Quadrat von 4 (allgemeine Funktion):", quadrieren(4))


# filter (Liste mit Bedingung filtern)
gefilterte_zahlen = list(filter(lambda num: num > 3, zahlen_liste))
print("Gefilterte Zahlen > 3:", gefilterte_zahlen)

# # Eigene Fehler mit raise
# def check_positive(value):
#     if value < 0:
#         raise ValueError(f"Wert muss positiv sein, aber {value} wurde übergeben.")
#     return value

# try:
#     check_positive(-1)
# except ValueError as e:
#     print("Fehler erkannt:", e)

# # Switch-Case Alternative
# # Hinweis: Python hat kein echtes switch-case; Dictionary wird verwendet
# operation = {
#     "add": lambda a, b: a + b,
#     "subtract": lambda a, b: a - b,
#     "multiply": lambda a, b: a * b,
#     "divide": lambda a, b: a / b if b != 0 else "Division durch Null!",
# }

# op = "add"
# result = operation[op](10, 5)
# print(f"Operation {op}: Ergebnis =", result)

# # Dekoratoren
# def debug(func):
#     def wrapper(*args, **kwargs):
#         print(f"Aufruf von {func.__name__} mit {args}, {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Ergebnis: {result}")
#         return result
#     return wrapper

# @debug
# def multiplizieren(a, b):
#     return a * b

# multiplizieren(3, 4)

# # Generatoren und yield
# def zahlen_generator():
#     for i in range(5):
#         yield i

# for zahl in zahlen_generator():
#     print("Generator-Zahl:", zahl)

# # Wichtige und häufig verwendete Libs in Python (folgt)