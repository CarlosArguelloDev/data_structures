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
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def agregar_final(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            return
        
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevo

    def recorrido_seguro(self):
        actual = self.cabeza
        while actual is not None:
            print(f"[{actual.dato}] -> ", end="")
            actual = actual.siguiente
        print("None")

