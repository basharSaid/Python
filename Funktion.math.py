import math
a  = 4.75
print("Variabel a : ", a)
print("Quadratwurzel von a :", math.sqrt(a))
print("Natürliche Logaritmus von a :", math.log(a))
print("e hoch a : ", math.exp(a))
print("10er-logaritmus von a :", math.log10(a))

print()
print("Kreiszahl pi :", math.pi)
print("Eulersche Zahl e :", math.e)

print()
print("Fakultät von 5 :", math.factorial(5))
print("grösster gem.Teiler von 60 und 135 ist: ", math.gcd(60, 135))

if(math.isclose(3, 2.96, rel_tol=0.01)):
     print("Nahe dran")
else:
     print("Nicht nahe dran")
if(math.isclose(3, 2.97, rel_tol=0.01)):
     print("Nahe dran")

else:
      print("Nicht nahe dran")
      



