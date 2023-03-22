cadena = "Geringoso"
vocal=["a","e","i","o","u","A","E","I","O","U"]
capadepenapa = "" #cadena en geringonoso
for i in cadena:
    if i in vocal:
        capadepenapa = capadepenapa + i + "p" + i
    else:
        capadepenapa = capadepenapa + i
print(capadepenapa)