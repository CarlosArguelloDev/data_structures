class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None 

    def esta_vacia(self):
        return self.cabeza == None

    def agregar_inicio(self, dato):
        temp = Nodo(dato)
        temp.siguiente = self.cabeza
        self.cabeza = temp

    def recorrido_seguro(self):
        actual = self.cabeza
        while actual is not None:
            print(f"[{actual.dato}] -> ", end="")
            actual = actual.siguiente
        print("None")

