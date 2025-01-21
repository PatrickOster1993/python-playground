from Roman import Roman
from Sachbuch import Sachbuch

# Instanziierung eines Sachbuch-Objekts
mein_sachbuch = Sachbuch(
    titel_ein="Physik ist toll",
    autor_ein="Albert Zweistein",
    isbn_ein="123456789",
    thema_ein="Physik"
)

# Aufruf der Methode wissenVermitteln
mein_sachbuch.wissenVermitteln()

# Instanziierung eines Roman-Objekts
mein_roman = Roman(
    titel_ein="Drachen Chroniken",
    autor_ein="Peter Brand",
    isbn_ein="123456789",
    genre_ein="Fantasy"
)

# Aufruf der Methode details
print(mein_roman.details())