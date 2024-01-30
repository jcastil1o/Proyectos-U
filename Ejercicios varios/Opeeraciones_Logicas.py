##Ejemplo operación and
condicion_and = (5>3) and (10<20)
print(condicion_and)

##Ejemplo operador or
condicion_or = (5>3) or (10>20)
print(condicion_or)

##Definición de función
def puede_votar(edad):
    ##parametro
    return edad>=18
try: 
    edad_usuario = int (input("Ingresa tu edad: "))
                                ##Error en capa 8, cuando un usuario ingresa mal los datos
    if puede_votar(edad_usuario):##Expresión booleana
        print("Puede votar")
    else:
        print("Lo siento, no puedes votar")
except ValueError:
    ##Posibilidad de un error en la condición
    print("Por favor, ingresa un número de edad válido")
