from ManejadorFacultades import ManejadorFacultad
def mostrar_menu():
    print("---- Menú ----")
    print("1. Buscar facultad por código")
    print("2. Buscar carrera por nombre")
    print("0. Salir")

def item1(manejador):
    cod = int(input('Ingrese código de la facultad: '))
    manejador.buscar_facultad(cod)

def item2(manejador):
    NomCarrera = str(input('Ingrese nombre de la carrera: '))
    manejador.buscar_carrera(NomCarrera)


if __name__ == '__main__':
    manejador = ManejadorFacultad()
    manejador.cargar_Archivo()

    opcion = None

    while opcion != 0:
        mostrar_menu()
        opcion = int(input('Ingrese una opción: '))
        if opcion == 1:
            item1(manejador)
        elif opcion == 2:
            item2(manejador)
        elif opcion == 0:
            print("Saliendo...")
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")
