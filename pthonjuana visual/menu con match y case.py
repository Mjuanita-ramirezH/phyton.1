animal = "eagle".capitalize()#paraque salga la primera en mayuscula y el resto en minuscula
#animal = "eagle".lower()
#animal = "eagle".upper()
match animal:
    case "eagle" | "parrot": #si quito del | para delnte solo cpmrara con la primera hasta encontrar la que es igual a la variable
        print ("bird")
    case "lion" | "tiger":
        print ("Mammal")
    case "python" | "cocodrile":
        print ("reptile")
    case _: 
        print ("Unknown class")
        
        
#Ejemplo menu
print ("Menu de envios")
print ("Get")
print ("post")
print ("put")
print ("delete")
print ("salir")
opc = int(input("ingrese opcion")).capitalize()
match opc:
    case "get": #se puede poner en numero pero con guien bajo 2_3_4 y luego va el | y el resto
        print ("fetching resource...")
    case "post":
        print ("creating resource...")
    case "put":
        print ("updating resource...")
    case "delete":
        print ("deleting resource...")
    case _:
        print ("unsupported HTTP method...")
