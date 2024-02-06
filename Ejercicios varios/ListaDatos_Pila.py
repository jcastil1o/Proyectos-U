##Programa para revertir el orden de una lista
def revertir_lista(lista):
    ##Definir funcion
    pila = []
        ##Creacion de pila
    for elemento in lista:
        ##for para cambiar el orden
        pila.append(elemento)
            ##Extraccion de elementos de la lista
        lista_revertida = []
        while pila:
            lista_revertida.append(pila.pop())
                                      ##Ingreso de los elementos de la lista original
                        ##Llamada a la anterior lista
        return lista_revertida
        ##Muestra la lista nueva
    
        
lista_original = [1,2,3,4,5]
lista_revertida = revertir_lista(lista_original)
print("Lista original: ", lista_original, "\n")
print("Lista invertida: ", lista_revertida, "\n")
