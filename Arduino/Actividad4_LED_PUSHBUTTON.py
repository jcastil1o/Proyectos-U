import serial
from serial.tools.list_ports import comports
from time import sleep
from tkinter import *
from tkinter import Button
import tkinter as tk
import threading

puerto = serial.Serial('COM7', 9600)


def ENCENDER_TODO ():
    print("Encender todo")
    puerto.write('5'.encode())

def APAGAR_TODO():
    print("Apagar todo")
    puerto.write('0'.encode())

def Grupo1():
    print("Grupo #1 encendido")
    puerto.write('1'.encode())

def Grupo2():
    print("Grupo #2 encendido")
    puerto.write('2'.encode())

def Grupo3():
    print("Grupo 3 encendido")
    puerto.write('3'.encode())

def Grupo4():
    print("Grupo #4 encendido")
    puerto.write('4'.encode())
"""
# Botones encendido/apagado
global is_on
is_on = True

def switch():
    global is_on 
    #determinar apagado/encendido
    if is_on:
        on.config(text="off", command= APAGAR_TODO)
        is_on = True
    else: 
        on.config(text="on", command= ENCENDER_TODO)
        is_on = False
"""
control = tk.Tk()
control.config( width=800, height=500)
control.title("LEDs y PUSHBUTTONS")


titulo = Label(text="Control de LEDs", background="snow", foreground="black", font=("Times New Roman", 15))
titulo.place(x=325, y=75)

on_all = tk.Button(text="Encender todo", width= 10, command= ENCENDER_TODO, background="yellow")
on_all.place(x=250, y=150)
off_all = tk.Button(text="Apagar todo", width=10, command= APAGAR_TODO, background="gray")
off_all.place(x=460, y=150)


A_boton = tk.Button(text="Grupo 1", width= 20, command= Grupo1, background="gold")
A_boton.place(x=100, y=250)
B_boton = tk.Button(text="Grupo 2", width= 20, command= Grupo2, background="green")
B_boton.place(x=250, y=250)
C_boton = tk.Button(text="Grupo 3", width= 20, command= Grupo3, background="red")
C_boton.place(x=400, y=250)
D_boton = tk.Button(text="Grupo 4", width= 20, command= Grupo4, background="spring green")
D_boton.place(x=550, y=250)

"""
on = Button(control, text="on", bd=0, command=ENCENDER_TODO)
on.pack(pady=50) 
on.place(x=300, y=300)
"""
control.mainloop()