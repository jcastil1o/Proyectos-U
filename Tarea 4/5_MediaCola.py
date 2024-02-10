#Programa de implementar una cola y reversion del orden de la mitad de la cosa en una lista
from collections import deque
#Importar libreria de cola
def revertir_cola(cola):
    #definir funcion de cola
    pila = []
    longitud = len(cola)
    #Obtener tamaño de cola
    mitad_cola = longitud // 2
    #Encontrar la mitad de la cola

    for _ in range(mitad_cola):
        pila.append(cola.popleft())
        #encontrar el primer dato en cola de la mitad

    for _ in range(mitad_cola):
        pila.append(cola.pop())
        #añadir elemento a la mitad de cola
    
    if longitud % 2 !=0:
        cola.append(pila.pop())
        #Verificar si la mitad de la cola es par o impar para dejar un espacio vacio

    while pila:
        cola.appendleft(pila.pop())
        #ciclo para mostrar el primer dato en cola
    return cola

lista_cola = deque(input("Ingrese los elementos de la lista: "))
#pedir los datos de la lista para volverlo cola
print("cola original: ", lista_cola)
#mostrar lista original
lista_cola = revertir_cola(lista_cola)
#poner en funcionamiento la mitad de reversion de la cola
print("Mitad revertida: ", lista_cola)
#mostrar la nueva cola invertida