"""
Aufgabe 1 Erstellen Sie ein Programm, das Ihren **Namen**, Ihr **Alter** und Ihr **Lieblingsessen** 
über eine Konsoleneingabe einliest. Geben Sie diese Informationen dann in einem Satz aus.
"""
#Variablen
vorname =           input("Bitte geben Sie ihren Vornamen an! ")
nachname =          input("Bitte geben Sie ihren Nachnamen an! ")
alter =             input("Wie Alt sind Sie? Ausgeschrieben oder als Zahl! ")
lieblingsessen =    input("Was ist ihr Lieblingsessen? ")

#Die Ausgabe mit den Variablen
print(f"Grüß Gott! {vorname} {nachname}, du bist {alter} Jahre alt, dein Lieblingsessen ist {lieblingsessen}.")
"""
print(f"text") (formatierter string) funktioniert genau so wie in C# mit Console.Writeline($"text") (interpolierter String)
formatierter string und interpolierter string Variablen und Ausdrücke direkt ausgewertet.
"""