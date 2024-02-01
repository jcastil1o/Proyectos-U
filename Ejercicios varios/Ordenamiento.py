##Ordenamiento de numeros de menor a mayor, separados por comas
numero = input ("Ingrese algunos numeros separados por espacios: ")
lista = [float(x) for x in numero.split()]
    ##Ordenamiento con punto flotante en forma de lista []  
lista.sort()
    ##Ordenamiento de menor a mayor
print(lista)
