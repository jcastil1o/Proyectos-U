class Grafo:
    def __init__(self):
        self.vertices = {}  # Correct the attribute name

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, inicio, fin):
        if inicio in self.vertices and fin in self.vertices:
            self.vertices[inicio].append(fin)
            self.vertices[fin].append(inicio)  # Para un grafo no dirigido

    def __str__(self):
        return str(self.vertices)

# Ejemplo de uso
g = Grafo()
g.agregar_vertice('A')
g.agregar_vertice('B')
g.agregar_vertice('C')
g.agregar_arista('A', 'B')
g.agregar_arista('B', 'C')
print(g)
