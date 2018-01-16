# Berechnung einer summe
summe = 0
for i in range(1, 4):
    fehler = True
    while fehler:
        zahl = input(str(i) + ".Zahl eingeben:")
        try:
            summe += float(zahl)
            fehler = False
        except:
            print("Das war keine zahl")
            fehler = True
print("Summe:", summe)
print()
# Geografiespiel
hauptstadt = {"Italien":"Rom", "Spanien":"Madrid", "Potugal":"Lissabon"}
hs = hauptstadt.items()
for land, stadt in hs :
    eingabe = input("Bitte die Hauptstadt von " + land + " eingeben: ")
    if eingabe == stadt:
        print("richtig")
    else:
        print("Falsch, richtig ist", stadt)
        

            
