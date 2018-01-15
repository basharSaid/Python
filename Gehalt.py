x = "true"
for i in x :

    print("Geben Sie Ihr Bruttogehalt in Euro ein:")
    gehalt = float(input())
    print("Geben Sie Ihre Familienstand ein:","(1=ledig, 2=verheiratet)")
    fs = int(input())
    if gehalt > 4000 and fs == 1:
        sb = gehalt*0.26
    elif gehalt <= 4000 and fs == 2:
        sb = gehalt*0.18
    else:
        sb = gehalt*0.22
    print("Es ergibt sich ein Steurbetrag von", sb ,"Euro")

    

        


    
    




