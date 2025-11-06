print ("MENU OPCIONES")
print ("KM")
print ("M")
print ("MI")
print ("CM")
medida = str(input("ingrese la medida a calcular")).upper()
match medida:
    case "KM":
        valor = int(input("Ingrese km a convertir"))
        metro = medida * 1000
        print ("medida en metros es", metro)
        
        