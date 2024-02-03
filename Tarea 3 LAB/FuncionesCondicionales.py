##Programa para la suma de dos datos, los cuales si son par o impar debe de mostrar su valor
mensaje1 = "Programa de la suma de dos numeros"
mensaje2 = "Funciones TRUE o FALSE"
print(mensaje1.center(100, "-"))
print(mensaje2.center(100, "+"))
numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
suma = numero1+numero2
print("Suma total de: ", suma)
resultado = suma % 2
if (resultado == 0):
    parametro = True
    print(parametro)
else:
    parametro = False
    print(parametro)
##Jonathan Castillo 0901-22-8408