def parentesisBalanceados(cadena):##funcion
    Pila = [] 
    for caracter in cadena:
        if caracter == '(':
            Pila.append(caracter) 
        elif caracter == ')':
            if not Pila or Pila.pop() != '(': ##Verifica si hay un paréntesis de cerrado 
                return False
    return not Pila ##Si la pila está vacía al final 
cadena_1 = "()" ##cadena
cadena_2 = ")([]{}" 
cadena_3 = ")(" 
cadena_4 = ")[()]" 
cadena_5 = "{[]}" 
print(parentesisBalanceados(cadena_1))
print(parentesisBalanceados(cadena_2))
print(parentesisBalanceados(cadena_3))
print(parentesisBalanceados(cadena_4))
print(parentesisBalanceados(cadena_5))