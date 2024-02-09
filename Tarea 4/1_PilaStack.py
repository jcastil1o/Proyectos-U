##Crear pila de una lista en python, funciones basicas de push, pop, peek
##Debe de invertir el orden de la lista con QUEUE
from collections import deque
##Importacion de libreria de cola
import time
##Importacion de libreria del tiempo

def anadir (lista):
    pila = []
    for elemento in lista:
        pila.append(elemento)
##Definir funcion de append
def cola_lista (cola):
    queue = deque (cola)
    while queue:
        print("Dato en cola: ", queue.popleft(), "\n")
        time.sleep(1)
##Definir funcion de cola, con variable de tiempo



lista = [0, 1, 2, 3, 4, 5]
print("Lista original: ", lista)
lista.append(6)
    ##Añadir un elemento al final de la lista
print("Metodo de agregar elementos".center(50, "-"))
                                    ##Metodo de impresion centrada en pantalla
print ("Elemento agregado: ", lista)
print("Metodo pop".center(50, "-"))
print("Eliminar los elementos excepto: ", lista.pop())
                                            ##Metodo pop para eliminar los demas datos de la estructura, excepto el que se indica
print("Metodo peek o index".center(50, "-"))
print("Elemento extraido [posicion 5]: ", lista.index(5), "\n")
                                            ##Metodo de impresion de un elemento especifico de la lista
print("Ingrese datos para crear una lista: (SEPARADOS POR ESPACIOS)".center(50," "))
lista2 = input()
ordenar = [float(x) for x in lista2.split()]  ##Funcion de ordenar los datos ingresados de la lista
ordenar.sort()
print(ordenar)
print("Implementacion de colas en una lista".center(60, "*"))
print("\n", " Dato en proceso: ", "\n")
cola_lista(ordenar)
print("Todos los datos finalmente procesados...")