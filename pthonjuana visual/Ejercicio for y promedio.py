cant = int(input("ingrese la cantidad de personas a las cuales le solicitara los datos"))
edadT = 0
alturaT = 0
if (cant>0):
    for x in range(1,cant + 1):
        print("solicitando datos persona", x)
        nom = str(input("ingrese nombres"))
        edad = int(input("ingrese edad"))
        altura = float(input("ingrese altura"))
        edadT = edadT+edad
        alturaT = alturaT+altura
    prome = edadT / cant
    proma = alturaT / cant
    if (prome<15) | (proma<1.55):
        print("su promedio dice que su altura es un poco bajo para la edad")
    elif (prome>15) | (proma>1.68):
        print("su promedio dice que vas a ser alto")
    else:
        print("tu promedio de altura es bueno")
else:
    print("error")