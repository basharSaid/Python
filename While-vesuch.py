# Zufallsgenerator
import random
random.seed()

# Werte und Berechnung
a = random.randint(1, 10)
b = random.randint(1, 10)
c = a + b
print("Die Aufgabe:", a, "+", b)

# Schleife initialisiren
zahl = c + 1

# Anzahl initialisiren
versuch = 0

# While - Schleife
while zahl != c:

    #Anzahl Versuche
    versuch = versuch + 1

    # Eingabe mit Umwandlung
    print("Bitte eine Zahl eingeben:")
    z = input()
    zahl = int(z)

# Verzweigung
    if zahl == c:
        print(zahl, "ist richtig")
    else :
        print(zahl, "ist falsch")

# Anzahl ausgeben
print("Ergebnis:", c)
print("Anzahl Versuche:", versuch)
