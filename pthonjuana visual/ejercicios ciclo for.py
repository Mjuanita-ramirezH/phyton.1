#mostrar palabra 10 veces
palabra = str(input("ingrese la palabra a repetir"))
for x in range(0,11):
    print(palabra)

#preguntar edad y mostrar todos lo años que ha cumplido desde 1 hasta su edad y mostrar al final si es mayor o menor de edad
edad = int(input("ingrese su edad"))
for x in range(0,edad,1):
    print(x)
if(edad<18):
    print("usted es menor de edad")
else:
    print("usted es mayor de edad")

#pedir numero entero positivo y mostrar los numeros impares desde 1 hasta el numero, separados por comas
num = int(input("ingrese un numero entero positivo"))
for x in range(1,num + 1):
    if x % 2 !=0:
        print(x,end=",")
        
#pedir un numero entero y mostar la taba de multiplicar dep 1 al 10 de ese numero ingresado
num2 = int(input("ingrese un numero entero a multiplicar"))
for x  in range(1,11):
    mul = num2*x
    print(num2,"x", x, "=", mul)
          
                