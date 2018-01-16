# Zufallsgenerator

import random
random.seed()

# Werte un Berechnug

a = random.randint(1, 10)
b = random.randint(1, 10)
c = a + b
print ("Die Aufgabe:", a, "+", b)

# Schleife mir for

for i in 1, 2, 3, 4:

    # Eingabe

    print ("Bitte eine Zahl engeben:")
    z = input()
    zahl = int(z)

    # Verzweigung
    if zahl == c:
        print(zahl, "ist richtig")

        # abbruch der Schleife
        break
    else:
        print (zahl, "ist flasch")

# Ende

print("Ergebnis:", c)
