from tkinter import Tk, Canvas

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

  def dibujar(self, window, radius=30):
    """ Dibuja el grafo en la ventana de Tkinter. """
    w = window.winfo_width()
    h = window.winfo_height()
    margin = 50  # Espacio alrededor del grafo

    # Calcula posiciones para los nodos (evita superposición)
    node_positions = {}
    available_positions = [(w // 3, h // 2), (2 * w // 3, h // 2)]
    for i, vertex in enumerate(self.vertices):
      node_positions[vertex] = available_positions[i]

    # Dibuja los nodos (círculos)
    for vertex, (x, y) in node_positions.items():
      window.create_oval(x - radius, y - radius, x + radius, y + radius, fill="lightblue")
      window.create_text(x, y, text=vertex, font=("Arial", 12))

    # Dibuja las aristas (líneas)
    for vertex, neighbors in self.vertices.items():
      for neighbor in neighbors:
        start_pos = node_positions[vertex]
        end_pos = node_positions[neighbor]
        window.create_line(start_pos[0], start_pos[1], end_pos[0], end_pos[1], width=2)

# Ejemplo de uso
g = Grafo()
g.agregar_vertice('A')
g.agregar_vertice('B')
g.agregar_vertice('C')
g.agregar_arista('A', 'B')
g.agregar_arista('B', 'C')

window = Tk()
window.title("Grafo")
g.dibujar(window)
window.mainloop()
