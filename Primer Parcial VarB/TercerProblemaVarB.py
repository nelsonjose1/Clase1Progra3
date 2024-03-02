##3. Escribe un programa que pida al usuario una lista de números y luego imprima la suma de los números pares en la lista. 
numeros = input("Ingresa una lista de números: ")
numeros_lista = [int(num) for num in numeros.split(',')]
suma_pares = sum(num for num in numeros_lista if num % 2 == 0)
print("La suma de los números pares en la lista es:", suma_pares)