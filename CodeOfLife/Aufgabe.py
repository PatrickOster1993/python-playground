import time
import random
import os 


zeilen  = 10
spalten = 50

mein_array = []


# für alle Buchstaben in zeilen und spalten - platz im 2Dim array machen
for z in range( zeilen ):   
    mein_array.append( [ ] ) 
    for s in range( spalten ):
        mein_array[z].append( "x" )
    


def zeicheArray():
     for zeilen_nr in range (zeilen):
         for spalten_nr in range (spalten):
             print( mein_array[zeilen_nr][spalten_nr] , end=" " )
         print( ) # < in nächste Zeile gehen



def zuffy_array_werte():
    for x in range (zeilen):
        for y in range (spalten):
            randy = random.randrange( 1 , 3)
            if randy == 1:
                mein_array[x][y] = "0"
            else: 
                mein_array[x][y] = " "



while True:  # Endlosschleife (Gameloop)
   zuffy_array_werte()
   zeicheArray() 
   time.sleep( 0.2 ) 
   os.system( "cls" )