#Programa de implementar una cola y reversion del orden de la mitad de la cosa en una lista
from collections import deque
    #Importar libreria de cola
import time
    #Importar libreria de tiempo

def cola(cola):
    #Definir funcion de cola
    queue = deque (cola)
    while queue:
        print ("Orden de cola: ",queue.popleftleft(), "\n")
        #Impresion de cola
            #metodo de mostrar el primer elemento de la lista en cola
        time.sleep(1)


print("Ingrese los elementos de la lista: (SEPARADOS POR ESPACIOS)".center(50, " "))
lista = input()
#Ingreso de elementos para la lista
lista = [float (x) for x in lista.split()]
    #Declaracion de lista
""" Inserte aqui para declarar el metodo de ordenar la cola en mitad"""