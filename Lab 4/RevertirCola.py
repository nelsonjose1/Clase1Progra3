from collections import deque
def revertirMitadCola(cola):
    pila = []
    longitud = len(cola)
    Mitad = longitud // 2
    for _ in range(Mitad): ##Se transfiere la mitad de la cola a la pila y pasa lo mismo pero en alrevés en el otro for
        pila.append(cola.popleft())
    for _ in range(Mitad):
        pila.append(cola.pop())
    if longitud % 2 != 0: ##La longitud de la cola es impar así que se omite el elemento de en medio
        cola.append(pila.pop())
    while pila: ##Se vuelve a poner los elementos en el orden bueno
        cola.appendleft(pila.pop())
    return cola
en_cola = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Cola original:", en_cola)
en_cola = revertirMitadCola(en_cola)
print("Cola con la mitad revertida:", en_cola)