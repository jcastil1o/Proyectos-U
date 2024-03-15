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
    puerto.write('on rojo'.encode())

def OFF_ROJO():
    #funcion LED roja
    print("Apagar ROJO")
    puerto.write('off rojo'.encode())

def ON_VERDE():
    #funcion LED verde
    print("Encender VERDE")
    puerto.write('on verde'.encode())

def OFF_VERDE():
    print("Apagar VERDE")
    puerto.write('off verde'.encode())

def ON_AMARILLO():
    print("Encender AMARILLO")
    puerto.write('on amarillo'.encode())

def OFF_AMARILLO():
    print("Apagar AMARILLO")
    puerto.write('off amarillo'.encode())

puerto = serial.Serial('COM7')
#puerto a comunicar

pantalla = tk.Tk()
#pantalla a usar interfaz
pantalla.config(width=500, height=300)
#Tamano de pantalla
pantalla.title("Controlar LEDs")
#Titulo de pantalla

#crear un boton de accion
encender_boton  = tk.Button(text="ENCENDER", width= 10, command= ENCENDER, background="yellow")
                    #tipo de boton  texto       tamano      accion
encender_boton.place(x = 150, y = 10)
#posicion del boton
apagar_boton = tk.Button(text="APAGAR", width=10, command= APAGAR, background="gray")
                    #tipo de boton  texto       tamano      accion
apagar_boton.place(x= 250, y= 10)
pantalla.mainloop()
        #ciclo infinito de la ventana

#puerto.close()