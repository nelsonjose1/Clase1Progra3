##Escribe una función en Python que reciba una lista como parámetro y devuelva la suma de todos los elementos de la lista. 
def sumar_lista(lista):##se define el nombre de la lista que se llama sumar_lista 
    suma = sum(lista)##se utiliza la operación suma con la variable sum y lista para poder sumar la lista
    return suma ##hace retornar la suma
mi_lista = [1, 2, 3, 4, 5] ##se define la lista que son de 5 números el cual debe de dar como resultado 15
resultado = sumar_lista(mi_lista) ##es el resultado de los 5 números 
print("La suma de los elementos de la lista son:", resultado)##se imprime en la pantalla el resultado de la lista