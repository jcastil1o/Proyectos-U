##Tipos de variables
print("     Programa para conocer el tipo de variable")
print("Ingrese algo a la consola")
dato = input("Dato: ")

def determinar_tipo_variable(valor):
    # Determina el tipo de la variable utilizando la función type()
    tipo = type(valor)._name_
    return tipo

# Solicita al usuario ingresar una variable
entrada_usuario = input("Ingrese una variable: ")

# Intenta convertir la entrada del usuario a un número si es posible
try:
    entrada_usuario = eval(entrada_usuario)
except:
    pass

# Determina y muestra el tipo de la variable
tipo_variable = determinar_tipo_variable(entrada_usuario)
print(f"El tipo de la variable es: {tipo_variable}")
##Jonathan Castillo 0901-22-8408