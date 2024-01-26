##Tipos de variables
print("     Programa para conocer el tipo de variable")
print("Ingrese algo a la consola")
dato = input("Dato: ")

if dato.isdigit():
    print("Es un dato entero: ", dato)
elif dato.replace(".", "").isdigit():
    print("Es un dato flotante: ", dato)
elif dato.lower() in ["true", "false"]:
        booleano  = True 
        print("Es un booleano: ", dato)

elif dato.startswith("[") and dato.endswith("]"):
    lista = eval(dato)
    if isinstance(lista, list):
        print("Es un arreglo: ", lista)      
    else:
        print("Lista no valida")
elif dato.isalpha:
    print("Es un dato string: ", dato)

else:
    print("Tipo de variable no encontrada")    
##Jonathan Castillo 0901-22-8408