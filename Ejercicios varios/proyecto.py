class Nodo:
    def _init_(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    def _init_(self):
        self.raiz = None

    def agregar_nodo(self, valor):
        nuevo_nodo = Nodo(valor)

        if self.raiz is None:
            self.raiz = nuevo_nodo
            return

        nodo_actual = self.raiz
        while True:
            if valor < nodo_actual.valor:
                if nodo_actual.izquierdo is None:
                    nodo_actual.izquierdo = nuevo_nodo
                    return
                else:
                    nodo_actual = nodo_actual.izquierdo
            else:
                if nodo_actual.derecho is None:
                    nodo_actual.derecho = nuevo_nodo
                    return
                else:
                    nodo_actual = nodo_actual.derecho

    def imprimir_arbol(self):
        self._imprimir_arbol_inorden(self.raiz)

    def _imprimir_arbol_inorden(self, nodo):
        if nodo is not None:
            self._imprimir_arbol_inorden(nodo.izquierdo)
            print(nodo.valor)
            self._imprimir_arbol_inorden(nodo.derecho)


# Ejemplo de uso
arbol = ArbolBinario()

# Agregar nodos al árbol
arbol.agregar_nodo("Programa madre")
arbol.agregar_nodo("Ventas")
arbol.agregar_nodo("Compras")
arbol.agregar_nodo("Ventas semanales")
arbol.agregar_nodo("Facturaciones")
arbol.agregar_nodo("Compras totales en tienda")
arbol.agregar_nodo("VistaUsuarioy")
arbol.agregar_nodo("Stock en tienda")
arbol.agregar_nodo("Comparacion de ventas")
arbol.agregar_nodo("Inventario \"Final\"")
arbol.agregar_nodo("Inventario \"Actual\"")
arbol.agregar_nodo("Determinacion de costos")
arbol.agregar_nodo("Ganancia Real")
arbol.agregar_nodo("Desperdicio")