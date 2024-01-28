nom_trabajador = str(input("Bienvenido ingresa tu nombre: "))
horas_trabajadas = int(input("Ingresa las horas de trabajo: "))
coste_hora = float(input("Ingresa el costo por hora trabajadas: "))
pago_trabajador = horas_trabajadas * coste_hora 
print("Tus horas son ", horas_trabajadas, " de trabajo. ", nom_trabajador, " , tu paga sera de: Q ", pago_trabajador) 