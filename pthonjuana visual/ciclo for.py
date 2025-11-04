for x in range(0, 4, 2): #se pone un numero mas para que cumpla todas las vueltas, si necesito que muestre hasta el 3 pongo el 4 como aqui, se le pone el dos para que vaya de dos en dos, el primer unmero es de dodne inicia, el segundo hasta doodne va y el tercero paso a paso
    print("estamos en la interaccion " + str(x))
    print("/n")#esto es para que haga un espacio en el interlineado
    
for y in range(20, -1, -1): #este es para que vaya decendiendo, se tabula para que haga los dos seguidos
    print("estamos en la interaccion " + str(y))
    
start = int(input("ingrese el inicio"))
stop = int(input("ingrese el final"))
step = int(input("ingrese el rango"))
for x in range(start, stop, step):
    print("Ciclo No. ", x)
    
