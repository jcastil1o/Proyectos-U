import serial
from serial.tools.list_ports import comports
from time import sleep
from tkinter import *
from tkinter import Button
import tkinter as tk
import threading

puerto = serial.Serial('COM7', 9600)

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

interfaz.mainloop()