##Programa para definir operaciones de cola de añadir, eliminar y mostrar el primer elemento
from collections import deque
import time

##Definir funcion de cola de una lista
def cola(cola):
    queue = deque (cola)
    while queue:
        print ("Dato en cola: ", queue.popleft(), "\n")
                                ##Metodo de mostrar el primer dato en cola
        time.sleep(1)

a = [0, 1, 2, 3]
print("Lista original: ", a)
print("Elemtento agregado", a.append(4))
print("Primer elemento: ",a.pop(0))
print("2da posicion", a.index(2))

print("Ingrese los datos de la lista: ".center(50, "<"))
print("SEPARADOS POR ESPACIOS")
ingreso = input()
lista = [float(x) for x in ingreso.split()]
print("Orden de atencion de datos: ", "\n")
cola(lista)
print("Atencion de datos completa".center(50, "*"))