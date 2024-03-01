"""Parcial 1
    Jonathan Camilo Castillo Mendez 0901 - 22 - 8408 """
from collections import deque
def revertir_cola(cola):
    pila = []
    longitud = len(cola)
    mitad_cola = longitud // 2

    for _ in range(mitad_cola):
        pila.append(cola.popleft())

    for _ in range(mitad_cola):
        pila.append(cola.pop())
    if longitud % 2 !=0:
        cola.append(pila.pop())
    while pila:
        cola.appendleft(pila.pop())
    return cola

    

lista_cola = deque(input("Ingrese los elementos de la lista: "))
print("cola original: ", lista_cola)
lista_cola = revertir_cola(lista_cola)
print("Mitad revertida: ", lista_cola)