# Funktion-Dummy
import random
random.seed()
def QuadraturDesKreises():
    pass
# Funktionsaufruf
QuadraturDesKreises()
# Nur else-Zweig interessant
print("Bitte geben Sie a,b,c ein")
a = random.randint(-10, 10)
print("a ist:", a)
b = random.randint(-10, 10)
print("b ist:", b)
c = random.randint(-10, 10)
print("c ist:", c)
if a >= 0 and b >= 0 and c >=0:
    pass
else:
    print("Eine der Zahlen ist negativ")
# Ein Zweig nicht interssant
if a == 1:
    print("Fall 1")
elif a ==2:
    print("Fall 2")
elif a < 0:
    pass
else:
    print("Ansonsten")
