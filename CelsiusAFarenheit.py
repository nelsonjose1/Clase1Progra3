##Programa que calcule grados celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
temperatura_celsius = float(input("Ingresa la temperatura en grados celsius"))
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius} grados Celsius con equivalentes a {temperatura_fahrenheit} grados Farenheit")