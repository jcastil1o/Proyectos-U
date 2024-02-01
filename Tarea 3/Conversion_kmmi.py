##Programa de conversion de km a mi
def conversionKM_MI(km):
    return km.isnumeric()
try:
    mensaje = "Programa para convertir KM a MI: "
    pantalla = mensaje.center(40, " ")
    print(pantalla)
    km=int(input("Ingrese cantidad de KM: "))
##  if conversionKM_MI(km):
    if km >= 0:
        conversion = km/1.609
        print("Esta es la cantidad de millas: ", conversion)
    else:
        mensaje = "Ingrese una cantidad positiva"
        pantalla = mensaje.center(40, "*")
        print(pantalla)

except ValueError:
    mensaje = "Digite correctamente el dato"
    pantalla = mensaje.center(60, "*")
    print(pantalla)