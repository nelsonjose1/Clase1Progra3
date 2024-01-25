##Un programa que calcule al ingresar la hora que indique cuantos segundos han trascurrido del dia
def calcular_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos
def obtener_hora_actual():
    import datetime
    ahora = datetime.datetime.now()
    return ahora.hour, ahora.minute, ahora.second
hora_actual = obtener_hora_actual()

hora_usuario = int(input("Ingresa la hora en formato de 24 horas"))
minutos_usuario = int(input("Ingresa los minutos: "))
segundos_usuario = int(input("Ingresa los segundos: "))

segundos_transcurridos = calcular_segundos(hora_usuario, minutos_usuario, segundos_usuario)
print(f"Desde la noche hasta la hora ingresada han transcurrido {segundos_transcurridos} segundos")