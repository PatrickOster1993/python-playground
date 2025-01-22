class Inhaltsverzeichnis:
    def __init__(self,ein_Autor , ein_Titel, ein_jahr):
        self.autor = ein_Autor
        self.titel = ein_Titel
        self.jahr = ein_jahr
        
    def ausgabe(self):
        print(f"hallo wie gehts {self.autor}, das ist der Titel {self.titel}, hier das jahr : {self.jahr}")        
        #print(f"Hallo, wie geht's {self.autor}? Das ist der Titel: {self.titel}. Hier das Jahr: {self.jahr}.")
        
        
        
        
        
hey = Inhaltsverzeichnis(
    ein_Autor="Mete" ,
    ein_Titel="Lernen macht spaß!",
    ein_jahr="2025",
)


#hey.ausgabe()



