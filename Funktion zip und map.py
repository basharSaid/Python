# Funktion-Zip
# Mehrere iterierbare Objekte
plz = [5800, 4700, 3600]
stadt = ["Wettingen", "Baden", "Zürich"]
bundsland = ["WE", "BA", "ZR"]
# Verbinden
kombi = zip(plz, stadt, bundsland)
# Ausgabe
for element in kombi:
    print(element)
print()


# Funktion-Map
# Funktion mit einem Parameter
def quad(x):
    erg = x * x
    return erg
# funktion mit mehr als einem Parameter
def summe(a, b, c):
    erg = a + b + c
    return erg
# Funktion mit einem Parameter mehrmals aufrufen
z = map(quad, [4, 2.5, -1.5])
# Jedes Ergebnis ausgeben
print("Quadrat:")
for element in z:
    print(element)
print()
# Funktion mit mehr als einem Parameter mehrmals aurufen
y = map(summe, [3, 1.2, 2], [4.8, 2, 4], [5, 0.1, 9])
        
# Jedes Ergebnis ausgeben
print("summe:")
for element in y:
        print(element)


