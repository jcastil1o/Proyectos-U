import serial
from serial.tools.list_ports import comports
from time import sleep
from tkinter import *
from tkinter import Button
#prueba 3
import tkinter as tk

    #libreria para la interfaz
def ENCENDER():
    #funcion encender
    print("Encender todo")
    puerto.write('1'.encode())
    #comunicacion al puerto

def APAGAR():
    #funcion apagar
    print("Apagar todo")
    puerto.write('0'.encode())
    #comunicacion al puerto

def ON_ROJO():
    #funcion LED roja
    print("Encender ROJO")
    puerto.write('2'.encode())

def OFF_ROJO():
    #funcion LED roja
    print("Apagar ROJO")
    puerto.write('3'.encode())

def ON_VERDE():
    #funcion LED verde
    print("Encender VERDE")
    puerto.write('4'.encode())

def OFF_VERDE():
    #funcion LED verde
    print("Apagar VERDE")
    puerto.write('5'.encode())

def ON_AMARILLO():
    #funcion LED amarillo
    print("Encender AMARILLO")
    puerto.write('6'.encode())

def OFF_AMARILLO():
    #funcion LED amarillo
    print("Apagar AMARILLO")
    puerto.write('7'.encode())

puerto = serial.Serial('COM7')
#puerto a comunicar

pantalla = tk.Tk()
#pantalla a usar interfaz
pantalla.config(width=500, height=200)
#Tamano de pantalla
pantalla.title("Controlar LEDs")
#Titulo de pantalla
titulo = Label(text="Encendido de LEDs", background="white", foreground= "black", font=("Arial", 15))
titulo.place(x= 175, y=5)

#crear un boton de accion
encender_boton  = tk.Button(text="ENCENDER", width= 10, command= ENCENDER, background="orange")
                    #tipo de boton  texto       tamano      accion
encender_boton.place(x = 175, y = 35)
#posicion del boton
apagar_boton = tk.Button(text="APAGAR", width=10, command= APAGAR, background="gray")
                    #tipo de boton  texto       tamano      accion
apagar_boton.place(x= 275, y= 35)

#LED ROJA
rojo_boton = tk.Button(text="ROJO", width= 15, command= ON_ROJO, background= "red")
rojo_boton.place(x=50, y=100)
#LED VERDE
verde_boton = tk.Button(text="VERDE", width= 15, command= ON_VERDE, background= "green")
verde_boton.place(x=200, y=100)
#LED AMARILLO
amarillo_boton = tk.Button(text="AMARILLO", width= 15, command= ON_AMARILLO, background= "yellow")
amarillo_boton.place(x=350, y=100)
pantalla.mainloop()
        #ciclo infinito de la ventana
#puerto.close()