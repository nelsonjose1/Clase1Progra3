import tkinter as tk
import serial
import threading
arduino = serial.Serial('COM3', 9600) 
def procesar_datos(datos):
    print("Datos recibidos desde Arduino:", datos.decode().strip())
def enviar_comando(comando):
    arduino.write(comando.encode())
ventana = tk.Tk()
ventana.title("Dashboard")

estilo_boton = {
    'font': ('Italic', 11),
    'width': 20,
    'height': 10,
    'bg': 'white',  
    'fg': 'black',  
    'activebackground': 'greenyellow',  
    'activeforeground': 'black',  
    'bd': 2,  
    'highlightthickness': 2,  
}
estilo_boton_circulo = {
    'font': ('Italic', 11),
    'width': 20,
    'height': 4,
    'bg': 'yellow',  
    'fg': 'black',  
    'activebackground': 'greenyellow',  
    'activeforeground': 'black',  
    'bd': 0,  
    'highlightthickness': 0,  
}

boton_A = tk.Button(ventana, text="Encender grupo led 1", command=lambda: enviar_comando('A'), **estilo_boton)
boton_A.pack(pady=5)

boton_B = tk.Button(ventana, text="Encender grupo led 2", command=lambda: enviar_comando('B'), **estilo_boton)
boton_B.pack(pady=5)

boton_C = tk.Button(ventana, text="Encender grupo led 3", command=lambda: enviar_comando('C'), **estilo_boton)
boton_C.pack(pady=5)

boton_D = tk.Button(ventana, text="Encender grupo led 4", command=lambda: enviar_comando('D'),**estilo_boton )
boton_D.pack(pady=5)

boton_E = tk.Button(ventana, text="Apagar grupo led 1", command=lambda: enviar_comando('E'), **estilo_boton_circulo )
boton_E.pack(pady=5)

boton_F = tk.Button(ventana, text="Apagar grupo led 2", command=lambda: enviar_comando('F'), **estilo_boton_circulo)
boton_F.pack(pady=5)

boton_G = tk.Button(ventana, text="Apagar grupo led 3", command=lambda: enviar_comando('G'), **estilo_boton_circulo)
boton_G.pack(pady=5)

boton_H = tk.Button(ventana, text="Apagar grupo led 4", command=lambda: enviar_comando('H'),**estilo_boton_circulo)
boton_H.pack(pady=5)
def leer_datos_desde_arduino():
    while True:
        datos = arduino.readline()
        if datos:
            procesar_datos(datos)
thread_arduino = threading.Thread(target=leer_datos_desde_arduino)
thread_arduino.start()
ventana.mainloop()