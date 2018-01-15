#!/Users/Bashar/Documents/virtualenv/bin/python
#Allgemeine Check-Funktion
import cgi, cgitb
def chk(element):
    global form
    if element in form:
        erg = form[element].value
    else:
        erg = ""
    return erg

# Ausgabe bei Fehler
cgitb.enable()

#Objekt der Klsse FieldStorage
form = cgi.FieldStorage()
print("Content-type: text/html")
print()
print("<!DOCTYPE html><html>")
print("<head><meta charest='utf-8'></head>")
print("<body>")

#Anrede
print("<p> Guten Tag", chk("vn"), chk("nn"), "</p>")

#Adresse
print("<p> Ihre Adresse:", chk("st"), chk("hn"), "in", chk("pz"), chk("or"), "</p>")

#Pizza-type
print("<p> Ihre Bestellung: Pizza", chk("pt"))

# Beginn Berechnung Preis
preisliste = {
    "Salami":6, "Thunfisch":6.5,"Quattro Stagioni":7.5, "Python":8.5
}
preis = preisliste[form["pt"].value]
 #Zusatz
zusatzliste = {
    "Pepproni":1, "Oliven":1.2, "Sardelen":1.5
}
if "zu" in form:
    try:
        print("mit", form["zu"].value)
        preis += zusatzliste[form["zu"].value]
    except:
        for element in form["zu"]:
            print(",mit", element.value)
            preis += zusatzliste[element.value]
print("</p>")

# Express-Service
if "ex" in form:
    print("<p> Mit Express-Service</>")
    preis += 1.5
#Bemerkung

if "bm" in form:
    print("<p>Bemerkung:", form["bm"].value, "</p>")
#Rabatt
if "kc" in form:
    if form["ku"].value == "S" and form["kc"].value == "Bingo":
        preis = preis * 0.95
        print("<p>Rabatt 5%</p>")
# Preis
print("preis (ohne Bemerkung): {0:.2f} &euro;".format(preis))

print("</body>")
print("</html>")
