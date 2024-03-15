import serial
from time import sleep
from tkinter import *
from serial.tools.list_ports import comports

estadoLed = 0

def setup():
    global puerto
    puerto = serial.Serial(list(comports())[0].device, 9600)
    sleep(2)  # Espera a que se establezca la conexión

def draw():
    global estadoLed
    canvas.delete("all")
    if estadoLed == 0:
        boton.config(bg="red")
        canvas.create_oval(width/2 - 25, height/2 - 25, width/2 + 25, height/2 + 25, outline="grey", fill="red")
    elif estadoLed == 1:
        boton.config(bg="#F4FFA5")
        canvas.create_oval(width/2 - 22.5, height/2 - 22.5, width/2 + 22.5, height/2 + 22.5, outline="grey", fill="#F4FFA5")

def mousePressed():
    global estadoLed
    if estadoLed == 0:
        estadoLed = 1
        puerto.write(b'1')
    else:
        estadoLed = 0
        puerto.write(b'0')
    draw()

# Configuración de la ventana
root = Tk()
width = 200
height = 200
root.geometry(f"{width}x{height}")
canvas = Canvas(root, width=width, height=height)
canvas.pack()

setup()

# Agregar un botón a la ventana Tkinter
boton = Button(root, text="Click me", command=mousePressed, bd=0, highlightthickness=0)
boton.pack()

root.mainloop()
