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
    PreCirculo()
def INORDEN():
    print("InOrden")
    puerto.write('2'.encode())
    InCirculo()

def POSTORDEN():
    print("PostOrden")
    puerto.write('3'.encode())
    PostCirculo()

def APAGAR():
    print("APAGAR LEDs")
    puerto.write('0'.encode())
    ApagarCirculo()

#Circulos

def circulo1():
    canvas.delete("circle")
    canvas.create_oval(230, 30, 280, 80, fill="dark sea green", tags="circle")
    #                   x        y
def circulo2():
    canvas.create_oval(200, 70, 250, 120, fill="gold", tags="circle")
    #                   x        y
def circulo3():
    canvas.create_oval(260, 70, 310, 120, fill="tomato", tags="circle")
    """
                        1
                    /       \
                2               3

                --------------------
                        Verde
                    /       \
                Amarillo      Rojo
    """
def PreCirculo():
    canvas.delete("circle")
    interfaz.after(1, circulo1)
    interfaz.after(100, circulo2)
    interfaz.after(10000, circulo3)
    
def InCirculo():
    canvas.delete("circle")
    interfaz.after(1, circulo2)
    interfaz.after(100, circulo1)
    interfaz.after(10000, circulo3)
    
def PostCirculo():
    canvas.delete("circle")
    interfaz.after(1, circulo2)
    interfaz.after(100, circulo3)
    interfaz.after(10000, circulo1)
    
def ApagarCirculo():
    canvas.delete("circle")
#Funcion del potenciómetro
def actualizar_barra():
    datos = puerto.readline().decode().strip()  # Lee datos del puerto serial

    if datos:  # Revisa si se recibieron datos
       try:
            valor = int(datos)  # Intenta la conversión directamente (opcional)
            valor_normal = int((valor / 1023) * 100)
            canvas.coords(bar, 5, 105 - valor_normal, 35, 105)
            print(datos, "\n")
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

Apagar_boton = tk.Button(text="APAGAR", width=10, command= APAGAR, background="peach puff")
Apagar_boton.place(x=400, y=150)

canvas = tk.Canvas(interfaz, width=400, height=300)
canvas.pack()
bar = canvas.create_rectangle(0, 105, 35, 105, fill="pale green")
bar_text = canvas.create_text(200, 250, text="", font = ("Resist Mono Variable Italic", 12, "bold"), anchor=tk.W, fill='black', angle=90)


canvas.configure(background="papaya whip")
canvas.place(x=105, y=200)
title_potenciometro = Label (text="Potenciometro", background="gainsboro", foreground="dark slate gray", font=("Resist Mono", 10))
title_potenciometro.place(x=10, y=250)

while True:
    actualizar_barra()


#fin
interfaz.mainloop()