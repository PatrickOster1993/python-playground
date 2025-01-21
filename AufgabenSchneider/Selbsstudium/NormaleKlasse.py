class Tier:
    def bewegen(self):
        pass  # Diese Methode ist nicht verpflichtend

class Hund(Tier):
    def bewegen(self):
        print("Der Hund rennt.")

class Katze(Tier):
    pass  # Keine Methode `bewegen`

# Hier entsteht ein Problem:
tiere = [Hund(), Katze()]
for tier in tiere:
    tier.bewegen()  # Katze hat keine `bewegen`-Methode -> Fehler
