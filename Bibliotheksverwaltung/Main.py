from Basebook import Book
from Roman import Roman
from Sachbuch import Sachbuch

Sachbuch1 = Sachbuch("Python für Anfänger", "John Doe", "978-3-123-45678-9", "Programmierung")
Roman1 = Roman("Der Herr der Ringe", "J.R.R. Tolkien", "978-3-608-93801-3", "Fantasy")

print(Sachbuch1.details())
print(Roman1.details())