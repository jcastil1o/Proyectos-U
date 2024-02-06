##Programa para identificar un timeless entre impresion/guardar datos en pantalla
from collections import deque
                        ##Colas
import time
    ##Libreria de manejo del tiempo

def simular_lineaEspera (clientes):
    ##Definir una funcion
    ##print(queue, "\n")
    queue = deque (clientes)
    ##metodo de creacion de cola a fila, para formar un arreglo de lista
    while queue:
        print("Atendiendo al cliente: ", queue.popleft())
                                            ##Metodo de impresion del ultimo dato en cola
        time.sleep(1)
            ##Tiempo de espera
        
##Separar el bloque de la funcion con la impresion de consola
clientes_en_espera = ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4"]
print("Bienvenido al banco, se estará a atendiendo según el orden: ", "\n")
simular_lineaEspera(clientes_en_espera)
print("Todos los clientes han sido atendidos...")   