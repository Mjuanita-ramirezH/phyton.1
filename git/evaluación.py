print ("TRANSPORTAME")
print ("RUTA 1.  PASAJE: $2000")
print ("RUTA 2.  PASAJE: $2200")
print ("RUTA 3.  PASAJE: $2400")
print ("RUTA 4.  PASAJE: $2600")
print ("RUTA 5.  PASAJE: $2800")
print ("6. SALIR")
total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
for x in range(0,5,1):
    ruta = int(input("ingrese el numero de ruta"))
    match ruta:
        case "1":
            print ("RUTA 1.  PASAJE: $2000")
            
        case "2":
            print ("RUTA 2.  PASAJE: $2200")
            
        case "3":
            print ("RUTA 3.  PASAJE: $2400")
            
        case "4":
            print ("RUTA 4.  PASAJE: $2600")
            
        case "5":
            print ("RUTA 5.  PASAJE: $2800")
            
        case _:
            print ("salir")

    total1=total1+2000
    
    total2=total1+2000
    
    total3=total1+2000
    
    total4=total1+2000
    
    total5=total1+2000
    print ("Total ruta=", total1)
print ("finalizar")       