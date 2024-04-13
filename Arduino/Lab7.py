import serial
from serial.tools.list_ports import comports
from time import sleep
from tkinter import *
from tkinter import Button
import tkinter as tk
import threading
from serial.tools.list_ports import comports

puerto = serial.Serial('COM7', 9600)

#Funciones de botones
def PREORDEN():
    print("PreOrden")
    puerto.write('1'.encode())
def INORDEN():
    print("InOrden")
    puerto.write('2'.encode())

def POSTORDEN():
    print("PostOrden")
    puerto.write('3'.encode())

def APAGAR():
    print("APAGAR LEDs")
    puerto.write('0'.encode())

#Funcion del potenciómetro
def actualizar_barra():
    datos = puerto.readline().decode().strip()  # Lee datos del puerto serial

    if datos:  # Revisa si se recibieron datos
        try:
            valor = int(datos)  # Intenta la conversión directamente (opcional)
            valor_normal = int((valor / 1023) * 100)
            canvas.coords(bar, 5, 105 - valor_normal, 35, 105)
            interfaz.update_idletasks()
            interfaz.update()
        except ValueError:  # Maneja errores de conversión
            print("No hay datos del potenciómetro")  # Mensaje informativo

interfaz = tk.Tk()
interfaz.config(width=500, height=500, background="papaya whip")
interfaz.title("POTENCIOMETRO y LEDs")

title = Label (text="Centro de control", background="gainsboro", foreground="dark slate gray", font=("Resist Mono", 20))
title.place(x=130, y=50)

PreOrden_boton = tk.Button(text="PREORDEN", width= 10, command= PREORDEN, background="light salmon")
PreOrden_boton.place(x=20, y=150)

InOrden_boton = tk.Button(text="INORDEN", width=10, command=INORDEN, background="light pink")
InOrden_boton.place(x=20, y=180)

PostOrden_boton = tk.Button(text="POSTORDEN", width=10, command= POSTORDEN, background="sky blue")
PostOrden_boton.place(x=20, y=210)

canvas = tk.Canvas(interfaz, width=40, height=105)
canvas.pack()
bar = canvas.create_rectangle(0, 105, 35, 105, fill="pale green")
canvas.configure(background="dim gray")
canvas.place(x=100, y=250)
title_potenciometro = Label (text="Potenciometro", background="gainsboro", foreground="dark slate gray", font=("Resist Mono", 10))
title_potenciometro.place(x=10, y=250)

while True:
    actualizar_barra()


#fin
interfaz.mainloop()