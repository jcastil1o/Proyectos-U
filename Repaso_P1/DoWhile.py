#libreria random
import random

num = random.randint(1, 10)
#Funcion random

while num:
#Ciclo while de num
    ingresoValor = int(input("Adivina el numero: "))
    #Ingreso de datos
    if ingresoValor > num:
        print(f"CASI ya no puedes usar este numero: {ingresoValor} intenta con uno menor")
        #Comparacion de numero mayor
    elif ingresoValor < num:
        print(f"CASI ya no puedes usar este numero: {ingresoValor} intenta con uno mmayor")
        #Comparacion de numero menor
    else:
        print(f"FELICIDADES EL NUMERO ERA: {num} ADIVINASTE EL NUMERO")
        #Mensaje de felicitaciones
        break
    #Fin del break
    """
    Programa que pide el ingreso de un numero
    y lo compara con el valor de la funcion random
    Al comparar entra en un ciclo do while para saber si el dato ingresado es igual al dato de la funcion random
    """