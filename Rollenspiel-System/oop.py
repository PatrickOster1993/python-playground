class Auto:
    #????
    marke = "BMW" ## << klassenvariabeln wird geteilt
    
    def __init__( self ): # __init__ Konstruktor  ## self übergibt die daten ein neu gemachtet auto
        #in das self objekt bauen wir eine neue variable "ps" ein
        self.ps = 123 #<<Instanzvariable
        self.marke ="BMW" ## << Instanzvariable 
        
        print()