from Alumno import Alumno


class Nodo:
    izquierdo = None
    derecho = None

    def __init__(self, alumno):
        self.izquierda = None
        self.derecha = None
        self.alumno = alumno


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, alumno):
        if self.raiz is None:
            self.raiz = Nodo(alumno)
        else:
            self._insertar_recursivo(self.raiz, alumno)

    def _insertar_recursivo(self, nodo_actual, alumno):
        if alumno.num_cuenta < nodo_actual.alumno.num_cuenta:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(alumno)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, alumno)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(alumno)
            else:
                self._insertar_recursivo(nodo_actual.derecha, alumno)

    def buscar(self,raiz,num_cuenta):
        if raiz is None:
            print("No existe ese alumno")
        else:
            if num_cuenta == raiz.alumno.num_cuenta:
                print(f"Nombre: {raiz.alumno.nombre},\n"
                      f"Materias: {raiz.alumno.materias},\n"
                      f"Promedio: {raiz.alumno.promedio}")
            elif num_cuenta < raiz.alumno.num_cuenta:
                return self.buscar(raiz.izquierda,num_cuenta)
            else:
                return self.buscar(raiz.derecha,num_cuenta)

    def visualizar(self, raiz, nivel=0):
        if raiz is not None:
            self.visualizar(raiz.derecha, nivel + 1)
            print(' ' * 4 * nivel + '->', raiz.alumno.num_cuenta)
            self.visualizar(raiz.izquierda, nivel + 1)
