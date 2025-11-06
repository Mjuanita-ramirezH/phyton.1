print ("MENU OPERACIONES")
print ("1.Sumar dos números")
print ("2.Restar dos números")
print ("3.Multiplicar dos números")
print ("4.Salir")
opc = str(input("ingrese opcion "))
match opc:
    case  "1":
        print ("Sumar dos números")
    case "2":
        print ("Restar dos números")
    case "3":
        print ("Multiplicar dos números")
    case _:
        print ("Salir")
