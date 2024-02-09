#Programa enfocado a la implentacion de colas y ordenamiento en dos listas que ingrese el usuario y simular una fila de espera.
from collections import deque
    #Importar libreria de cola
import time
    #Importar libreria de tiempo

def cola(cola):
    #Definir funcion de cola
    queue = deque (cola)
    while queue:
        print ("Atendiendo a: ", queue.popleft(), "\n")
                                ##Metodo de mostrar el primer dato en cola
                #Impresion de cola
        time.sleep(1)
            #Tiempo de espera en la fila
        
"""contador = int(2)
for contador in range (contador):
    print("Ingrese los elementos de la cola: ".center(50, "+"))
    lista1 = input("SEPARADOS POR ESPACIOS -> ")
    contador+=1
"""
print("Ingrese los elementos de la cola: #1".center(50, "+"))
lista1 = input("SEPARADOS POR ESPACIOS -> ")
    #Ingreso de primera lista o pila
print("Ingrese los elementos de la cola: #2".center(50, "+"))
lista2 = input("SEPARADOS POR ESPACIOS -> ")
    #Ingreso de segunda lista o pila

lista1 = [float (x) for x in lista1.split()]
lista1.sort()
    #Metodo de ordenar la pila
lista2 = [float (x) for x in lista2.split()]
lista2.sort()
    #Metodo de ordenar la pila

lista3 = lista1 + lista2
    #Concatenar listas
#lista3 = [float (x) for x in lista3.split()]
lista3.sort()
    #Ordenar la tercera lista
cola(lista3)
    #Introducir la concatenacion de listas a la funcion de cola
print("Antencion de datos completa...".center(50, "*"))
    #Mensaje de despedida
                                        #Metodo de impresion en pantalla en posicion central