class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.arriba = None
        self.abajo = None
        self.centro = None

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        self.valor = valor

    def get_arriba(self):
        return self.arriba

    def set_arriba(self, nodo):
        self.arriba = nodo

    def get_abajo(self):
        return self.abajo

    def set_abajo(self, nodo):
        self.abajo = nodo

    def get_centro(self):
        return self.centro

    def set_centro(self, nodo):
        self.centro = nodo


# Asignamos el valor de los nodos y creamos sus objetos

head = Nodo(20)
nodo1 = Nodo(23)
nodo2 = Nodo(19)
nodo3 = Nodo(57)
nodo4 = Nodo(67)
nodo5 = Nodo(99)

# LLenar la branch de arriba

head.set_arriba(nodo1)
nodo1.set_centro(nodo3)

# LLenar la branch de abajo

head.set_centro(nodo2)
nodo2.set_abajo(nodo4)
nodo4.set_centro(nodo5)

print("---------- OBTENER EL 99 -----------")
print(head.get_centro().get_abajo().get_centro().get_valor())

print("---------- OBTENER EL 57 -----------")
print(head.get_arriba().get_centro().get_valor())

