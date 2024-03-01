"""Parcial 1
    Jonathan Camilo Castillo Mendez 0901 - 22 - 8408 """

#Lista como parametro y devolver la suma de todos los elementos
def anadir (lista):
    pila = []
    for elemento in lista:
        pila.append(elemento)

print("Bienvenido a este programa".center(45, '#'))
try:
    print("Ingresa los elementos de la lista: \n")
    lista = input()
except ValueError:
    print("Ingresa numeros validos")

i = int
i = 0
longitud = len(lista)
for x in range (i<=longitud):
    suma = float
    indice = lista.index(i) + lista.index(i+1)
    break