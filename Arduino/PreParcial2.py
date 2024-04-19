import tkinter as tk
import serial
from serial.tools.list_ports import comports
from time import sleep
from tkinter import *
from tkinter import Button
import threading
from serial.tools.list_ports import comports

def mouse_move(event):
    x = event.x
    y = event.y
    label.config(text=f'Posición del ratón: x={x}, y={y}')
    label.place(x=130, y=180)

def key_press(event):
    key = event.keysym
    label.config(text=f'Tecla presionada: {key}')
    label.place(x=130, y=180)

def key_release(event):
    label.config(text='')
    label.place(x=130, y=180)

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Captura de Eventos de Ratón y Teclado")
root.config(width=300, height=300, background="misty rose")
root.title("CAPTURA DE TECLADO Y MOUSE")

title = Label (text="EJEMPLOS DE CAPTURA: ", background="lavender", foreground="dim gray")
title.place(x=130, y=100)

# Crear una etiqueta para mostrar la posición del ratón y la tecla presionada
label = tk.Label(root, text="")
label.pack()

# Asociar el evento de movimiento del ratón con la función mouse_move
root.bind('<Motion>', mouse_move)

# Asociar el evento de presionar una tecla con la función key_press
root.bind('<KeyPress>', key_press)

# Asociar el evento de soltar una tecla con la función key_release
root.bind('<KeyRelease>', key_release)

# Ejecutar el bucle principal
root.mainloop()