from collections import deque 

class ColaConDosPilas:
    def __init__(self):
        self.piladeEntrada = [] ##Pila para encolar los elementos el de abajo hace lo mismo pero alrevés
        self.piladeSalida = [] 
    def enqueue (self, elemento):
        self.piladeEntrada.append(elemento) ##Agregar los elementos a la primera pila
    
    def dequeue(self):
        if not self.piladeSalida: 
            while self.piladeEntrada:
                self.piladeSalida.append(self.piladeEntrada.pop())  ##función para transferir los elementos a la pila
        if self.piladeSalida: 
            return self.piladeSalida.pop()
        else: 
            return None
cola = ColaConDosPilas()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
cola.enqueue(4)
cola.enqueue(30)
print(cola.dequeue()) 
print(cola.dequeue()) 
print(cola.dequeue()) 
print(cola.dequeue()) 
print(cola.dequeue()) 
print(cola.dequeue()) 
print(cola.dequeue()) 