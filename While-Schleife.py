#zufallsgenerator
import random
random.seed()

# Initialisirung
summe = 0

# Whlie-Schliefe
while summe < 30 :
    zzahl = random.randint(1, 10)
    summe = summe + zzahl
    print("zahl:", zzahl, "Zwischensumme", summe)
    
# Ende   
print("Ende")

