class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self, raiz):
        self.raiz = raiz

    def agregar(self, valor, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self.agregar(valor, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self.agregar(valor, nodo.derecha)

    def generar_dot(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        dot = ''
        if nodo.izquierda:
            dot += f'"{nodo.valor}" -> "{nodo.izquierda.valor}"\n'
            dot += self.generar_dot(nodo.izquierda)
        if nodo.derecha:
            dot += f'"{nodo.valor}" -> "{nodo.derecha.valor}"\n'
            dot += self.generar_dot(nodo.derecha)
        return dot

# Crear un árbol binario con un nodo raíz
arbol = ArbolBinario(Nodo("Programa Madre"))

# Agregar nodos al árbol
arbol.agregar("Subprograma de Inventario")
arbol.agregar("Subprograma de Ventas")
arbol.agregar("Subprograma de Inventario Final")
arbol.agregar("Costo Final de Ventas")
arbol.agregar("Costos de Mermas")
arbol.agregar("Gastos Operativos")
arbol.agregar("Gastos Fijos")

# Generar código DOT
dot_code = 'digraph G {\n'
dot_code += arbol.generar_dot()
dot_code += '}'

# Imprimir el código DOT
print(dot_code)
