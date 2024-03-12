#libreria para manejar arduino
import serial
#libreria de tiempo
import time

#declarar el puerto conectado al arduino
puerto = 'COM7'
#velocidad de frecuencia de arduino
velocidad = 9600

#cominicar python al arduino
"""
    convertir a Serial, puerto a usar, velocidad y tiempo de espera
"""
ser = serial.Serial(puerto, velocidad, timeout= 1)
#tiempo de comunicacion
time.sleep(2)
#Imprimir un mensaje al arduino
        #convertir a binario
ser.write(b'Enciende la LED')
#Respuesta del arduino
                #linea          codigo en arduino
respuesta = ser.readline().decode('utf-8') 
#mensaje en pantalla
print('LED encendido', respuesta)

#Cerrar conexion
ser.close()