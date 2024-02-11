class PilaYcola: ##Se crea la clase Pila y Cola
    def __init__(self):## Funciones para hacer las operaciones básicas
        self.lista = [] 
    def push(self, elemento):##Sirve para añadir el elemento a una lista
        self.lista.append(elemento)
    def pop(self):
        if not self.pila_vacia(): ## Elimina y devuelve el elemento en la parte de arriba de la lista
            return self.lista.pop()
        else:
            return None ##Devolver None si la pila se encuentra vacía 
    def peek(self):
        if not self.pila_vacia():
            return self.lista[-1] 
        else:
            return None 
    def pila_vacia(self):
        return len(self.lista) == 0 
def invertir_lista(lista):
    pila = PilaYcola() 
    for elemento in lista:
        pila.push(elemento) 
    lista_Invertida = [] ##lista vacía 
    while not pila.pila_vacia():
        lista_Invertida.append(pila.pop())
    return lista_Invertida
lista_original = [1, 2, 3, 4, 5]
print("Lista original:", lista_original)
lista_Invertida = invertir_lista(lista_original) 
print("Lista invertida:", lista_Invertida)