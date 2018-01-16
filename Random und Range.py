import random
random.seed()

# Werte un Berechnug
a = random.randint(1, 10)
b = random.randint(1, 10)
c = a + b
print ("Die Aufgabe:", a, "+", b)
# Schleifr mit Range
for versuch in range(1, 10):
    #Eingabe
    print("Bitte eine Zahl eingeben:")
    z = input()
    zahl = int(z)
    # Verzweigung
    if zahl == c:
        print(zahl, "ist richtig")
        # Abbruch der Schleife
        break
    else:
        print(zahl,"ist flasch")
# Anzahl ausgaben
print("Ergebnis:",c)
print("Anzahl Versuche:", versuch)
        
