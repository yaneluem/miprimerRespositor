print("mi calculadora en payton")
#ingresar los unmeros enlas variables nun 1 y nun2
num1 =float(input("ingresar el primer numero: "))
num2 =float(input("ingresar el segundo numero: "))
#nostrar numeros de operaciones
print("operaciones disponibles")
print("1. lasuma")
print("2. la reslta")
print("3. multiplicacion")
print("4. divicion")
operacion=input("elija una operacion ")
#logica con if / Elif / Else
if operacion=="1":
    resultado = num1+num2
    print("resultado de la sumaes: " ,resultado)
elif operacion== "2":
    resultado = num1-num2
    print("resultado de la resta es: " ,resultado)
elif operacion == "3":
     resultado = num1*num2
     print("resultado de la multiplicacion es: " ,resultado)
elif operacion == "4":
    resultado = num1/num2
    print("resultado de la divicion  es: " ,resultado)
else:
    print("opcion no valida")

print("¿desea seguir en la calculadora?")
print("1. si")
print("2. no")

contitunuar =input("ingresa la opcion")
if contitunuar == "1":
    print("se volvera a utilsr l calculadora ")
else: 
    print(" gracias por utilizar la calculadora ")
