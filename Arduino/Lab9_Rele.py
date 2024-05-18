import serial
from serial.tools.list_ports import comports
from time import sleep
from tkinter import *
from tkinter import Button
import tkinter as tk
import threading

def BOTON():
    puerto.write('1'.encode())
    print("1")
    b=print("0")
    interfaz.after(10000, b)

puerto = serial.Serial('COM7', 9600)

interfaz = tk.Tk()
interfaz.config(width=500, height=500, background="light cyan")
interfaz.title("RELÉ y LEDs")

title = Label (text="Control de luz", background="powder blue", foreground="black", font=("Times New Roman", 20))
title.place(x=100, y=50)

Boton = tk.Button(text="ENCENDER RELÉ", width=20, command=BOTON, background="dim gray")
Boton.place(x=200, y=200)

interfaz.mainloop()