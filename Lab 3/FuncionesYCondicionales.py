##Funciones y condicionales
def suma(num1, num2):
    agrego = num1 + num2
    return agrego % 2 == 0
num1= float(input("Ingresa un numero: "))
num2 = float(input("Ingresa el otro numero: "))

resultado = suma(num1,num2)
print(f"La suma de los dos numeros es par : {resultado}")
