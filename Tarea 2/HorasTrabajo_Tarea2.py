##Programa para el calculo de salario por horas de trabajo
mensaje  = "Bienvenido al calculo de salario por horas de trabajo"
impresion = mensaje.center(40, '"')
print(impresion)
print()
horas = float (input("Ingrese las horas laboradas: "))
print()
pago = float (input("Ingrese el precio por hora laborada: "))
salario = horas * pago
print ("Este es su salario total: Q", salario)
##Jonathan Castillo 0901-22-8408