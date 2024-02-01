##Programa de creación de un arbol binario en clases
class Node:
    def __init__(self,valor):
        self.valor = valor
        self.izquierdo = Node
        self.derecho = Node

raiz = Node (1)
raiz.izquierdo = Node (2)
raiz.derecho = Node (3)
raiz.izquierdo.izquierdo = Node (4)
raiz.derecho.derecho = Node (5)