#Programa para determinar una cadena de caracteres de los tipo de parentesis y verificar
def cadena(parentesis):
    #Definir una funcion para verificar si la cadena esta correcta o no
    lista = []
    #Definir lista a comparar
    principal = {'{' : '}', '(' : ')', '[' : ']'}
    #Definir el uso correcto de apertura y cierre de un parentesis

    for p in parentesis:
        #Ciclo para analizar la lista
        if p in principal:
            lista.append(p)
            #Ciclo para analizar cada caracter de la cadena
        elif len(lista) == 0 or p != principal[lista.pop()]:
            #Ciclo contrario para identificar un error en la cadena y eliminar
            return False
        
    return len(lista) == 0
    #Mostrar la lista vacia

print ("Cadena: ()[]{} ->", cadena('()[]{}'))
print ("Cadena: ()[]{) ->", cadena('()[]{)'))
#Imprimir cadena
                            #Compar lo que se va a imprimir encontra de la funcion