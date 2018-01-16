# zufallsgenerator
import random
random.seed()
# Werte und Berechnung
a = random.randint(1, 10)
b = random.randint(1, 10)
c = a + b
print(" Die Ausgabe:",a, "+", b)
# Eingabe
print("Bitte eine Zahl eingeben:")
z = input()
zahl = int(z)
# Mehrfache verzweigung, logische Operatoren
# Bedigung mit mehreren vergleichsoperatoren
if zahl ==c:
    print(zahl, "ist richtig")
elif zahl < 0 or  zahl > 100 :
    print(zahl, "ist ganz flasch")
elif c-1 <= zahl <= c+1:
    print(zahl, "ist ganz nahe dran")
else:
    print(zahl, "ist falsch")
# Ende
print("Ergebnis: ", c)
    
