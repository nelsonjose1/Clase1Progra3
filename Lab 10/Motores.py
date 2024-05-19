import serial
import tkinter as tk
from math import sin, cos, radians

# Configurar la conexión serial
ser = serial.Serial('COM3', 9600)

# Configurar la ventana principal
root = tk.Tk()
root.title("Futuristic Control Dashboard")
root.configure(bg='black')

# Configurar el tamaño y la posición de la ventana
ancho_ventana = 500
alto_ventana = 500
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
x_pos = (ancho_pantalla - ancho_ventana) // 2
y_pos = (alto_pantalla - alto_ventana) // 2
root.geometry(f'{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}')

# Etiqueta de título con fuente personalizada y estilo
titulo_label = tk.Label(root, text="Control de Dispositivos", bg='black', fg='cyan', font=('Helvetica', 24, 'bold'))
titulo_label.pack(pady=20)

# Crear un Canvas para agregar elementos gráficos
canvas = tk.Canvas(root, width=400, height=400, bg='black', highlightthickness=0)
canvas.pack()

# Función para enviar comandos a través de la conexión serial
def enviar_comando(comando):
    ser.write(comando.encode())

# Crear y configurar los botones con estilos personalizados
botonStepper = tk.Button(root, text="Iniciar Stepper", command=lambda: enviar_comando('1'), bg='blue', fg='white', font=('Helvetica', 12, 'bold'), width=15, height=2)
botonServo = tk.Button(root, text="Iniciar Servo", command=lambda: enviar_comando('2'), bg='green', fg='white', font=('Helvetica', 12, 'bold'), width=15, height=2)

# Posiciones circulares para los botones
cx, cy, r = 200, 200, 150
stepper_pos = (cx + r * cos(radians(45)), cy - r * sin(radians(45)))
servo_pos = (cx - r * cos(radians(45)), cy + r * sin(radians(45)))

# Colocar los botones en el Canvas
canvas.create_window(stepper_pos[0], stepper_pos[1], window=botonStepper)
canvas.create_window(servo_pos[0], servo_pos[1], window=botonServo)

# Dibujar un círculo en el Canvas
canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline='cyan', width=2)

# Dibujar líneas radiales para un efecto futurista
num_lines = 12
for i in range(num_lines):
    angle = (360 / num_lines) * i
    x_end = cx + r * cos(radians(angle))
    y_end = cy - r * sin(radians(angle))
    canvas.create_line(cx, cy, x_end, y_end, fill='cyan', width=1)

# Texto explicativo debajo de los botones
texto_explicativo = tk.Label(root, text="Haz clic en un botón para iniciar el dispositivo", bg='black', fg='white', font=('Helvetica', 12, 'italic'))
texto_explicativo.pack(side=tk.BOTTOM, pady=20)

# Iniciar el bucle principal de la aplicación
root.mainloop()