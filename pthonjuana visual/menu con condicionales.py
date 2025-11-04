print ("MENU")
print ("1.suma")
print ("2.resta")
print ("3.multiplicacion")
print ("4.opcion salir")
opc = int(input("Ingrese la opcion a realizar "))
print (opc)
if (opc==1):
    print ("su opcion es 1")
    num1 = int(input("ingrese primer numero "))
    num2 = int(input("ingrese segundo numero "))
    suma = num1+num2
    print (num1, "+", num2 , "=", suma)
elif (opc ==2):
    print ("su opcion es 2")
    num1 = int(input("ingrese primer numero "))
    num2 = int(input("ingrese segundo numero "))
    resta = num1-num2
    print (num1, "-", num2 , "=", resta)
elif (opc==3):
    print ("su opcion es 3")
    num1 = int(input("ingrese primer numero "))
    num2 = int(input("ingrese segundo numero "))
    multi = num1*num2
    print (num1, "*", num2 , "=", multi)
else:
    print ("Finzalizado")      