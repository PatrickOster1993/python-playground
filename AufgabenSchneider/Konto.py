class BankKonto:
	def __init__(self, blz, pin):
		self.blz = blz # Öffentlich
		self._bankCode =  "XYZ123"  # Geschützt
		self.__pin = pin # Privat (Namens-Mangling)

	def checkPin(self, eingabe):
	
		return eingabe ==  self.__pin

	def zeigeBankcode(self):
	
		return self._bankCode

# Nutzung:
konto = BankKonto("MEINE_BANKLEITZAHL", "1234")
print(konto.blz)  				# Öffentlich: MEINE_BANKLEITZAHL
print(konto.zeigeBankcode())  	# Geschützt, kontrollierter Zugriff:XYZ123
print(konto.checkPin("1234"))  	# True (korrekter PIN)
print(konto.checkPin("0000"))  	# False (falscher PIN)

# Direkter Zugriff:
# print(konto.__pin) 			# Fehler: Zugriff nicht erlaubt