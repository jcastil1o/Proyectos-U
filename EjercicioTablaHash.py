"""
class TablaHash:
  def __init__(self, tamano):
    self.tamano = tamano
    self.tabla = [None] * self.tamano

  def funcion_hash(self, clave):
    # Función hash simple (suma de códigos ASCII)
    suma = 0
    for caracter in clave:
      suma += ord(caracter)
    return suma % self.tamano

  def insertar(self, clave, valor):
    indice_hash = self.funcion_hash(clave)
    posicion = indice_hash

    # Se comprueba si hay colisión
    while self.tabla[posicion] is not None:
      if self.tabla[posicion][0] == clave:
        # Si la clave ya existe, se actualiza el valor
        self.tabla[posicion][1] = valor
        print(f"Clave {clave} actualizada con valor {valor}")
        return
      
      # Se busca la siguiente posición libre
      posicion = (posicion + 1) % self.tamano

    # Se inserta el elemento en la posición libre
    self.tabla[posicion] = [clave, valor]
    print(f"Clave {clave} insertada en la posición {posicion}")

  def mostrar_tabla(self):
    for i in range(self.tamano):
      if self.tabla[i] is not None:
        print(f"Posición {i}: {self.tabla[i]}")
      else:
        print(f"Posición {i}: Vacía")

# Ejemplo de uso
tabla_hash = TablaHash(15)

# Inserción de elementos
tabla_hash.insertar("Juan", 32)
tabla_hash.insertar("Maria", 28)
tabla_hash.insertar("Pedro", 18)
tabla_hash.insertar("Ana", 25)
tabla_hash.insertar("Luis", 40)
tabla_hash.insertar("Carlos", 32)  # Colisión con "Juan"

# Mostrar la tabla
tabla_hash.mostrar_tabla()
"""

class TablaHash:
  def __init__(self, tamano):
    self.tamano = tamano
    self.tabla = [None] * self.tamano

  def funcion_hash(self, clave):
    suma = 0
    for caracter in clave:
      suma += ord(caracter)
    return suma % self.tamano

  def insertar(self, indice, clave, valor):
    if 0 <= indice < self.tamano:
      posicion = indice
    else:
      print(f"Índice inválido: {indice}. Debe estar entre 0 y {self.tamano - 1}")
      return

    # Se comprueba si hay colisión
    while self.tabla[posicion] is not None:
      if self.tabla[posicion][0] == clave:
        # Si la clave ya existe, se actualiza el valor
        self.tabla[posicion][1] = valor
        print(f"Clave {clave} actualizada con valor {valor}")
        return
      
      # Se busca la siguiente posición libre
      posicion = (posicion + 1) % self.tamano

    # Se inserta el elemento en la posición libre
    self.tabla[posicion] = [clave, valor]
    print(f"Clave {clave} insertada en la posición {posicion}")

  def mostrar_tabla(self):
    for i in range(self.tamano):
      if self.tabla[i] is not None:
        print(f"Posición {i}: {self.tabla[i]}")
      else:
        print(f"Posición {i}: Vacía")

# Ejemplo de uso
tabla_hash = TablaHash(10)

while True:
  # Menú de opciones
  print("\nOpciones:")
  print("1. Insertar elemento")
  print("2. Mostrar tabla")
  print("3. Salir")

  opcion = int(input("Ingrese una opción: "))

  if opcion == 1:
    indice = int(input("Ingrese el índice: "))
    clave = input("Ingrese la clave: ")
    valor = input("Ingrese el valor: ")
    tabla_hash.insertar(indice, clave, valor)
  elif opcion == 2:
    tabla_hash.mostrar_tabla()
  elif opcion == 3:
    break
  else:
    print("Opción inválida.")
