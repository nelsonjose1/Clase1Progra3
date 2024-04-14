import serial
import tkinter as tk
import threading
ser = serial.Serial('COM3', 9600)
def serial_reader():
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            if data:
                handle_code(data)
def turn_on_circle(circle, color):
    canvas.itemconfig(circle, fill=color)
def turn_off_circle(circle):
    canvas.itemconfig(circle, fill="white")
def handle_code(code):
    try:
        digit = int(code)
        print("Código recibido:", digit)
        for circle in circles:
            turn_off_circle(circle)
        if digit == 1:
            turn_on_circle(circles[0], "yellow")
        elif digit == 2:
            turn_on_circle(circles[1], "green")
        elif digit == 3:
            turn_on_circle(circles[2], "red")
        update_bar_graph(digit)
    except ValueError:
        print("Mensaje desde Arduino:", code)
def update_bar_graph(value):
    normalized_value = value / 1023
    x0 = 50
    y0 = 400
    x1 = 50 + normalized_value * 500  
    y1 = 450
    color = '#%02x%02x%02x' % (int(255 - (normalized_value * 255)), int(normalized_value * 255), 0)
    canvas.coords(bar, x0, y0, x1, y1)
    canvas.itemconfig(bar, fill=color)


root = tk.Tk()
root.title("Btn Controlador")
root.geometry("800x600")

canvas = tk.Canvas(root, width=600, height=500, bg='black')
canvas.pack()
bar = canvas.create_rectangle(50, 400, 50, 450, fill='green')  

circles = []
for i in range(3):
    circle = canvas.create_oval(50 + i * 70, 150, 100 + i * 70, 200, outline="black", width=2)
    canvas.create_text(75 + i * 70, 175, text=str(i+1), font=("Turquoise Sans", 12))
    circles.append(circle)

title_text = tk.Label(root, text="Lab 7")
title_text.place(x=350, y=25)

button_text = tk.Label(root, text="Leds")
button_text.place(x=375, y=100)

pot_text = tk.Label(root, text="Potenciometro")
pot_text.place(x=350, y=370)

serial_thread = threading.Thread(target=serial_reader)
serial_thread.daemon = True
serial_thread.start()

root.mainloop()