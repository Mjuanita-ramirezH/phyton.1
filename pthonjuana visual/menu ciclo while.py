print ("Menu de envios")
print ("1.Get")
print ("2.post")
print ("3.put")
print ("4.delete")
print ("6.salir")
opc = str(input("ingrese opcion: ")).capitalize()
while (opc!="salir"):
    match opc:
        case "1": #se puede poner en numero pero con guien bajo 2_3_4 y luego va el | y el resto
            print ("1.Get")
            print ("fetching resource...")
        case "2":
            print ("2.post")
            print ("creating resource...")
        case "3":
            print ("3.put")
            print ("updating resource...")
        case "4":
            print ("4.delete")
            print ("deleting resource...")
        case _:
            print("unsupported HTTP method...")
    print ("Menu de envios")
    print ("1.Get")
    print ("2.post")
    print ("3.put")
    print ("4.delete")
    print ("6.salir")
    opc = str(input("ingrese opcion: ")).capitalize()
print ("Salir")