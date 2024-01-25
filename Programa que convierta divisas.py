##Programa que convierta divisas (dolares a quetzales)
def dolares_a_quetzales(quetzales):
    dolares = (quetzales * 7.82)
    return dolares
conversion = float(input("Ingresa los dolares"))
convertido= dolares_a_quetzales(conversion)
print(f"{conversion}Dolares ingresados son equivalentes a {convertido} quetzales")
