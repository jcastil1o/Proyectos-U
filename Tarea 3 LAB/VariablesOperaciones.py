##Programa consta sobre la solución de ingreso de dos números y realizar operaciones aritméticas
mensaje1 = "Bienvenido a este programa"
mensaje2 = "Operaciones Aritmeticas"
print(mensaje1.center(40, "-"))
print(mensaje2.center(40, "+"))
numero1 = int (input("Ingresa el primer numero: "))
numero2 = int (input("Ingresa el segundo numero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multi = numero1 * numero2
divis = float (numero1 / numero2)
print ("Esta es la suma: ", suma)
print ("Esta es la resta: ", resta)
print ("Esta es la multiplicacion", multi)
print ("Esta es la division: ", "{:.2f}". format(divis))
##Jonathan Castillo 0901-22-8408