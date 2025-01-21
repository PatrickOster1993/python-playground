from abc import ABC, abstractmethod

class Zahlung(ABC):
    @abstractmethod
    def bezahlen(self, betrag):
        pass

class Kreditkarte(Zahlung):
    def bezahlen(self, betrag):
        print(f"Zahlung von {betrag}€ mit Kreditkarte.")

class PayPal(Zahlung):
    def bezahlen(self, betrag):
        print(f"Zahlung von {betrag}€ mit PayPal.")

# Polymorphismus: Beide Klassen werden gleich behandelt
def process_payment(zahlungsart: Zahlung, betrag):
    zahlungsart.bezahlen(betrag)

kreditkarte = Kreditkarte()
paypal = PayPal()

process_payment(kreditkarte, 50)  # Ausgabe: Zahlung von 50€ mit Kreditkarte.
process_payment(paypal, 100)     # Ausgabe: Zahlung von 100€ mit PayPal.
