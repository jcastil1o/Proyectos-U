##Programa para el control academico de un alumno, utilizando metodos y clases
##Creacion de clase
class Estudiante:
    def __init__(self, nombre, edad, calificacion):## __init__ y self son parametros ya definidos
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion
##Inicio del programa
mensaje1 = "BIENVENIDOS AL PROGRAMA ACADEMICO"
print(mensaje1.center(50, "@"))
mensaje2 = "Ingrese los datos del alumno: "
print(mensaje2.center(50, " "))
Estudiante.nombre = input("Nombre del alumno: ")
Estudiante.edad = input(f"Edad del alumno {Estudiante.nombre}: ")##Funcion de impresion de una variable declarada en una clase
Estudiante.calificacion = int (input("Calificacion del alumno: "))
                        ##Declarar el tipo de variable (entera) para poder condicionarla con operadores >, <, ==
if(Estudiante.calificacion>=60):
    mensaje3 = f"Aprobado con exito: {Estudiante.calificacion}"
    print(mensaje3.center(60, "*"))
else:
    mensaje3 = f"Reprobado: {Estudiante.calificacion}"
    print(mensaje3.center(60, "@"))
##Fin del programa

##Jonathan Castillo 0901-22-8408