##Formula cuadratica
import math
print("     Programa de la formula cuadratica")
print("  Este es un programa para la resolucion de polinomios tipo: ")
print(" ax^2 + bx+ c ")

ax = float (input("Ingrese valor de ax^2: "))
bx = float (input("Ingrese valor de bx: "))
c = float (input("Ingrese valor de c: "))

multi = (bx*bx)*-4*(ax*c)
division = 2*ax
if (multi>0):
    raiz = math.sqrt (multi)
    formula1 = float (-(bx) + raiz)/(division)
    formula2 = float (-(bx) - raiz)/(division)
    print("X1 = ", formula1)
    print("X2 = ", formula2)
    formula1=0
    formula2=0
elif (multi==0):
    print("Una unica solucion: ")
    formula3 = -bx /division
    print("X = ", formula3)
    formula3 = 0
else:
    formula3 = -bx /division
    imaginaria = math.sqrt(abs(multi)/division)
    formula4 = complex(formula3, imaginaria)
    formula5 = complex(formula3, - imaginaria)
    print("X1 = ", formula4)
    print("X2 = ", formula5)
    formula4 = 0
    formula5 = 0
##Jonathan Castillo 0901-22-8408