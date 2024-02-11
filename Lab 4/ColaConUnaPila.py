from collections import deque 
class ColaConUnaPila:
    def __init__(self): ##Funcion para una lista vacía
        self.lista_vacia = []
    def enqueue(self, elemento):##Se pone la cola
        self.lista_vacia.append(elemento)
    def dequeue(self):## Se saca la cola
        if not self.cola_vacia():
            return self.lista_vacia.pop(0) 
        else:
            return None 
    def front(self):##Se ve el primer elemento de la cola sin eliminarlo
        if not self.cola_vacia():
            return self.lista_vacia[0] ##Devuelve el primer elemento de la cola
        else:
            return None 
    def cola_vacia(self):
        return len(self.lista_vacia) == 0 
def atencion_fila(elementos):
    fila = ColaConUnaPila() ##Es la instancia de la clase 
    for elemento in elementos: ##Agrega elementos a la fila
        fila.enqueue(elemento)
    print("Proceso en la fila: ")
    while not fila.cola_vacia():
        nextelemento = fila.dequeue()
        print(f"Atendiendo: {nextelemento}")
    if fila.cola_vacia():
        print("Todos los clientes han sido satisfactoriamente atentidos")
elementos = ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4", "Cliente 5", "Cliente 6", "Cliente 7"]
atencion_fila(elementos)