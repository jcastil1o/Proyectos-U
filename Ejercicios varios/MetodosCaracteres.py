##Clase 25 de enero
texto = "hola Mundo"
    ##Creacion de un objeto
print("Metodo Capitalize")
resultado = texto.capitalize()
    ##Instancia del objeto
        ##Metodo capitaliza
print (resultado)
print()
    ##Impresion en pantalla

print("Metodo find")
resultado = texto.find("Mundo")
print (resultado)
print()

print ("Metodo Center")
resultado = texto.center(20, '*')
    ##Centra el texto entre los caracteres que indicamos
print (resultado)
print()

print("Metodo alfanumerico")
resultado = texto.isalnum()
    ##Indica por medio de un booleano si la comparacion es verdadera o falta hacia un caracter alfanumerico
print(resultado)
print("Cambio de Hola mundo a: 555")
texto = "555"
print(resultado)
print()

print("Metodo digitos")
resultado = texto.isdigit()
    ##Metodo de mostrar la cantidad de digitos que contiene la variable a comparar
print(resultado)
print()