## programa de pilas y colas en python
cartas = []
    ##Creacion de una pila
cartas.append('C')
    ##metodo para inducir datos en las posiciones de la pila
cartas.append('A')
cartas.append('T')
cartas.append('G')

print(cartas)
##Extraer datos de una posicion especifica de la pila
ultimo_elemento = cartas.pop()
                        ##Metodo del ultimo elemento
print(ultimo_elemento, "\n")
                        ##Siguiente linea
##Primero en entrar y ultimo en salir
penultimo_elemento = cartas.pop()
##Posicionamiento en memoria
print(penultimo_elemento, "\n")