from collections import deque
import time
import random

#Ejercicios varios para practica de parcial 1
#Operaciones logicas y aritmeticas
class operaciones_aritmeticas: 
    def __init__(self, numero1, numero2):
        #definir numeros a ingresar
        self.numero1 = numero1
        self.numero2 = numero2
    
    def suma(self):
        #definir funcion de suma
        return self.numero1 + self.numero2
    
    def restar(self):
        #definir funcion de resta
        return self.numero1 - self.numero2

    def multi(self):
        #definir funcion de multiplicar
        return self.numero1 * self.numero2

    def division(self):
        #definir funcion de dividir
        return self.numero1 / self.numero2

    def residuo1(self):
        #definir funcion de residuo
        return self.numero1 % 2
    def residuo2(self):
        #definir funcion de residuo
        return self.numero2 % 2

class operaciones_logicas:
    def __init__(self, numero3, numero4):
        #definir numeros
        self.numero3 = numero3
        self.numero4 = numero4
    def operador_and(self):
        #operacion and
        return self.numero3 and self.numero4
    def operador_or(self):
        #operacion or
        return self.numero3 or self.numero4
        
def cola_lista(cola):
    queue = deque (cola)
    while deque:
        print("Dato en cola: ", queue.popleft(), "\n")
        time.sleep(1)
def anadir (lista):
    pila = []
    for elemento in lista:
        pila.append(elemento)

print("Bienvenido al programa:".center(30, '#'))
print("1. Operadociones aritmeticas\n")
print("2. Operaciones lógicas\n")
print("3. Listas")
while True:
    try:
        opcion = int(input("Ingresa una opcion: \n"))
        break
    except ValueError:
        print("Ingrese una opción válida")

if opcion==1:
    try:
        numero1 = float(input("Ingresa un numero: \n"))
        numero2 = float(input("Ingresa el otro numero: \n"))
    except ValueError:
        print("Ingrese valores numéricos válidos")
        exit()
    operaciones = operaciones_aritmeticas(numero1, numero2)
    suma = operaciones.suma()
    resta = operaciones.restar()
    multi = operaciones.multi()
    division = operaciones.division()
    residuo1 = operaciones.residuo1()
    residuo2 = operaciones.residuo2()
    print("Operaciones aritmeticas:".center(40, '+'))
    print("Suma:", suma)
    print("Resta:", multi)
    print("Multi:", multi)
    print("Division:", division)
    print("Residuo 1:", residuo2)
    print("Residuo 2:", residuo2)       
elif opcion == 2:
    try:
        numero3 = float(input("Ingresa un numero: \n"))
        numero4 = float(input("Ingresa el otro numero: \n"))
    except ValueError:
        print("Ingrese valores numéricos válidos")
        exit()
    operaciones2 = operaciones_logicas(numero3, numero4)
    op_and = operaciones2.operador_and()
    op_or = operaciones2.operador_or()
    print("Operadociones lógicas")
elif opcion == 3:
    print("Listas".center(50, '*'))
    print("1. Simular cola\n")
    print("2. Agregar un elemento\n")
    print("3. Revertir una lista")
    print("4. Ordenamiento de burbuja")
    while True:
        try:
            opcion2 = int(input("Ingresa una opcion: \n"))
            break
        except ValueError:
            print("Ingrese una opción válida")
    if opcion2 == 1:
        print("Ingrese una lista (SEPARADOS POR ESPACIOS)")
        lista = input()
        ordenar = [float(x) for x in lista.split()]
        ordenar.sort()
        print("Lista ordenada: ", ordenar)
        cola_lista(ordenar)
        print("Todos los datos finalmente procesados...")
    if opcion2 == 2:
        print("Agregar un elemento")
        print("Ingrese los elementos de la lista: ")
        lista = input()
        print("Esta es una lista: ", lista)
        a = input("Ingrese un numero: ")
        lista.append(a)
        print("Se agrego un elemento: ", lista)

else:
    print("Opción no válida")