#Actividad en clase 12 de marzo
import serial
import time

puerto = 'COM7'
velocidad = 9600
ser = serial.Serial(puerto, velocidad, timeout=1)
time.sleep(2)

python = b'H'
ser.write(python)
time.sleep(1)