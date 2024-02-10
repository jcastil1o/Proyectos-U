#Programa de implementar una cola y reversion del orden de la mitad de la cosa en una lista
from collections import deque
    #Importar libreria de cola
import time
    #Importar libreria de tiempo

class Cola:
    def __init__(self, lista):
        self.cola = deque(lista)   
    def __str__(self):
        return str(self.cola)
    def enqueue(self, elemento):
        self.cola.append(elemento)
    def dequeue (self):
        return self.cola.popleft() 

def cola(cola):
    #Definir funcion de cola
    queue = deque (cola)
    while queue:
        print ("Orden de cola: ", queue.popleft(), "\n")
        #Impresion de cola
            #metodo de mostrar el primer elemento de la lista en cola
        time.sleep(1)

def colarevertir(cola):
    pila = []
    longitud_cola = len(cola)
    mitad_longitud = longitud_cola//2

    for _ in range (mitad_longitud):
        elemento = cola.dequeue()
        pila.append(elemento)

    for _ in range (longitud_cola):
        elemento = pila.pop()
        cola.enqueue(elemento)
        
        return cola

print("Ingrese los elementos de la lista: (SEPARADOS POR ESPACIOS)".center(50, " "))
lista = input()
#Ingreso de elementos para la lista
lista = [float (x) for x in lista.split()]
    #Declaracion de lista
cola(lista)
cola_invertida = colarevertir(deque(lista))
print("Orden de cola invertida: ")
while cola_invertida:
    print(cola_invertida.popleft(), "\n")
    time.sleep(1)
""" Inserte aqui para declarar el metodo de ordenar la cola en mitad"""