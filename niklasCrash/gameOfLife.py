# Aufgabe 1: Erstelle ein 2-dimensionales Array mit Buchstabensymbolen
# Ein 2x3 Array wird erstellt mit verschiedenen Buchstaben

# Spielfeld Größe
zeilen = 10
spalten = 50

mein_array = []

for z in range ( zeilen ):
    mein_array.append([])
    for s in range ( spalten ):
        mein_array[z].append("x")


def zeichne_array():
    for zeilen_nr in range(zeilen):
        for spalten_nr in range(spalten):
            print(mein_array[zeilen_nr][spalten_nr], end=" ")
        print( )  # Leerzeile am Ende jeder Zeile

#print(mein_array)

# # Array ausgeben zur Kontrolle
# print("Aufgabe 1 - 2D Array:")
# print(mein_array[0])  # Erste Zeile
# print(mein_array[1])  # Zweite Zeile

# # Aufgabe 2: Schleife die 20 Zeichen nacheinander ausgibt
# print("\nAufgabe 2 - Schleife mit Zahlen:")
# for x in range(20):
#     print(x, end=" ")  # end=" " fügt ein Leerzeichen statt Zeilenumbruch ein

# Aufgabe 3: Schleife die ein 20x20 Gitter ausgibt
# ausgeschnitten in Funktion

# Zusätzliche Leerzeile am Ende für bessere Lesbarkeit

# Aufgabe 5

# def zeichne_array():
#     for zeilen_nr in range(3):
#         for spalten_nr in range(3):
#             print(mein_array[zeilen_nr][spalten_nr], end=" ")
#         print( )  # Leerzeile am Ende jeder Zeile

# # zeichne_array()

# Aufgabe 6
# Schreibe in der Main Funktion eine Schleife
# die dauerhaft läuft und immer wider die Funktion aufruft

# while True: #Endlosschleife (Gameloop)
#     zeichne_array() #Funktion aufrufen

# Aufgabe 7
# Finde heraus wie man das PRogramm für 100 Milisekunden "schlafen" lässt
# Zeitmodul importieren

import time
import random
import os

def zuffy_array_werte():
    for x in range(zeilen):
        for y in range(spalten):
                randy = random.randrange(1, 3)
                if randy == 1:
                    mein_array[x][y] = "X"             
                else:
                    mein_array[x][y] = " "
                                

while  True: # Endlosschleife (Gameloop)
    zuffy_array_werte()
    zeichne_array()
    time.sleep(0.2) # 100 Milisekunden
    os.system("cls") # Bildschirm löschen
    

#     print("\n")

# Aufgabe 8
# Finde heraus wie man in Python eine Zufallszahl zwischen 1 und 2 erzeugt diese auf der Konsole bei jedem neuen Durchluf ausgibt

# Aufgabe 9
# Schreibe über die dauerhaft laufenden Schleifen zwei ineinader
# verschachtelste Schleifen, die für jeden Eitnrag im 2 dimensionalen Array
# eine Zufallszahl zwischen 1 und 2 erzeugt und dann entwder ein "X" oder "o" an der
# entsprechenden Stelle ausgibt

# Aufgabe 10
# Lagere den Code, der die zufälligen X und O Werte erzeugt in eine eigene Funktion aus
# Rufe diese Funktion in der dauerhaft laufenden Schleife auf

# import time
# import random
# import os 


# zeilen  = 10
# spalten = 50

# mein_array = []


# # für alle Buchstaben in zeilen und spalten - platz im 2Dim array machen
# for z in range( zeilen ):   
#     mein_array.append( [ ] ) 
#     for s in range( spalten ):
#         mein_array[z].append( "x" )
    


# def zeicheArray():
#     for zeilen_nr in range (zeilen):
#         for spalten_nr in range (spalten):
#             print( mein_array[zeilen_nr][spalten_nr] , end=" " )
#         print( ) # < in nächste Zeile gehen



# def zuffy_array_werte():
#     for x in range (zeilen):
#         for y in range (spalten):
#             randy = random.randrange( 1 , 3 )
#             if randy == 1:
#                 mein_array[x][y] = "0"
#             else: 
#                 mein_array[x][y] = " "



# while True:  # Endlosschleife (Gameloop)
#    zuffy_array_werte()
#    zeicheArray() 
#    time.sleep( 0.2 ) 
#    os.system( "cls" )


