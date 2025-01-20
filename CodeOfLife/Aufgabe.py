import time
import random
import os


zeilen = 10
spalten = 50

mein_array =  []

# für alle Buchstaben in zeilen und spalten - platz im 2Dim array machen
for z in range( zeilen ):  
    mein_array.append( [ ] )
    for s in range( spalten ):
        mein_array[z].append( "x" )





def zeichneArray(): # in eine methode gepackt
    for zeile_nr in range (zeilen):
     for spalten_nr in range (spalten):
         print(mein_array[zeile_nr][spalten_nr], end=" ") 
          #hier ist eine zeile fertig
     print() # < in nächste zeile gehen




def zuffy_array_werte():   #A10 lagere den code in eine fkt aus
    for x in range (zeilen):
        for y in range (spalten):
            randy = random.randrange(1, 3)
            if randy == 1:
                    mein_array[x][y] = "O"
            else:
                    mein_array[x][y] = " "

while True: #Endlosschleife (Gameloop)
   zuffy_array_werte()
   zeichneArray()
   time.sleep( 0.2 )   #30 FPS ??? in Millisek >> 1000 ms /30
   os.system("cls")
   




