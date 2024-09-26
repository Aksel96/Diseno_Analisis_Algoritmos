from database import data_split
from Alumno import *
from database_materias import gen_materias
from generadores import *
from ArbolBinarioBusqueda import *
from utils import *


def crear_alumnos_basedatos(data):
    rango = len(data)
    alumnos = []
    for i in range(rango):
        promedio = gen_promedio()
        edad = gen_edad()
        semestre = gen_semestre()
        materias = gen_materias()
        num_cuenta = gen_numero_cuenta()
        nombre, app, apm, correo = data[i]
        alumno = Alumno(num_cuenta, nombre, app, apm, edad, correo, semestre, materias, promedio)
        alumnos.append(alumno)
    return alumnos


def pintar_menu():
    print("##################################################################")
    print("-#-              Arbol Binario de busqueda")
    print("-#-          Base de datos de alumnos de ICO")
    print("###################################################################")
    print("-#-                      MENU")
    print("-#-    1)   Ingresar un nuevo alumno")
    print("-#-    2)   Consultar un alumno existente")
    print("-#-    3)   Visualizar el arbol")
    print("-#-    4)   Salir del Programa")
    print("###################################################################\n")


def verificar_opcion(opcion):
    while True:
        match opcion:
            case "1":
                return 1
            case "2":
                return 2
            case "3":
                return 3
            case "4":
                return 4
            case _:
                print("Opcion No Valida")
                opcion = input("Introduce nuevamente la opcion: ")


def main():
    salir = "n"

    alumnos = crear_alumnos_basedatos(data_split)

    arbol = ArbolBinarioBusqueda()

    for alumno in alumnos:
        arbol.insertar(alumno)

    while salir != "s":
        pintar_menu()

        opcion = input("-#-    Ingrese su opcion: ")

        menu_opcion = verificar_opcion(opcion)

        match menu_opcion:
            case 1:
                print("###################################################################")
                print("-#-    Ingresar alumnos a la Base de Datos")
                print("-#-    Recuerda que los datos son los siguientes:")
                print("###################################################################")
                print("-#-    ->Nombre")
                print("-#-    ->Apellido Paterno")
                print("-#-    ->Apellido Materno")
                print("-#-    ->Numero de cuenta")
                print("-#-    ->Edad")
                print("-#-    ->Correo")
                print("-#-    ->Semestre")
                print("-#-    ->Promedio")
                print("-#-    ->Materias")
                print("###################################################################\n")
                nombre = input("-#-    Ingrese el nombre: ")
                app = input("-#-    Ingrese el Apellido Paterno: ")
                apm = input("-#-    Ingrese el Apellido Materno: ")
                num_de_cuenta = ingresar_num_cuenta()
                edad = ingresar_edad()
                correo = input("-#-    Ingrese el correo: ")
                semestre = ingresar_semestre()
                promedio = ingresar_promedio()
                materias = ingresar_materias()

                alumno_nuevo = Alumno(num_de_cuenta, nombre, app, apm, edad, correo, semestre, materias, promedio)
                arbol.insertar(alumno_nuevo)
                print("-#-    Alumno Insertado:")
                print(alumno_nuevo.__str__())

            case 2:
                print("###################################################################")
                print("-#-    Buscador de alumnos por numero de cuenta")
                print("-#-    Recuerde que el numero de cuenta es numerico de longitud 9")
                print("-#-    Y esta entre el rango de 314000000 a 324999999")
                print("###################################################################\n")
                num_buscar = input("-#-    Ingrese el numero de cuenta: ")
                while not verificar_numero_cuenta(num_buscar):
                    num_buscar = input("-#-    Ingrese nuevamente el numero de cuenta: ")
                arbol.buscar(arbol.raiz, int(num_buscar))
            case 3:
                arbol.visualizar(arbol.raiz)
            case 4:
                salir = "s"


if __name__ == '__main__':
    main()
