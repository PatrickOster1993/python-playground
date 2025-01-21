##Aufgabe 1
#Erstelle ein zweidimensionales Array,
#In das man buchstaben eintragen kann.

zeilen = 10
spalten =50


mein_array =[]   

for z in range( zeilen ):  
    mein_array.append( [ ] )
    for s in range( spalten ):
        mein_array[z].append( "x" )
 


def zeichneArray():
    for zeilen_nr in range (zeilen):
        for spalten_nr in range(spalten):
            print( mein_array[zeilen_nr][spalten_nr],end="" )
        print()#< hier wird in die nächste zeile gegangen
          

import time
import random
import os

def zuffy_Array_werte():
    for x in range (zeilen):
        for y in range(spalten):
            randy = random.randrange(1 , 3) 
            if randy ==1:
                mein_array[x][y] = "!"
            else:
                mein_array[x][y] = " "

while True: #Endlosschleife (Gameloop) wie windows
    zuffy_Array_werte()
    zeichneArray()
    time.sleep( 0.252 )
    os.system( "cls" )
    
    
