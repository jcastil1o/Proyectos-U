##Programa para implementar una condicional if para determinar un numero
def numeros(numero):
    return numero.isdigit
try:
    mensaje = "Programa para determinar si un numero es positivo, negativo o cero"
    print(mensaje.center(100, "+"))
    numero =int (input("Ingresa un numero: "))
    if (numero==0):
        print("El numero es cero")
    elif(numero > 0):
        print("El numero es postivo")
    elif(numero < 0):
        print("El numero es negativo")
except ValueError:
    print("El valor que ingresa no es un numero")
##Jonathan Castillo 0901-22-8408