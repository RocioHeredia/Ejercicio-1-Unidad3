import csv
from ClassFacultad import Faculdad

class ManejadorFacultad:

    def __init__(self):
        self.__Facultades = []

    def cargar_Archivo(self):
        archivo = open('facultades.csv', encoding='utf-8-sig')
        reader = csv.reader(archivo, delimiter=',')
        cod = 0
        facultad = True
        for linea in reader:
            if facultad:
                unaFacu = Faculdad(int(linea[0]), linea[1], linea[2], linea[3], linea[4])
                self.__Facultades.append(unaFacu)
                cod = int(linea[0])
                facultad = False
            elif cod == int(linea[0]):
                unaFacu.agregar_carrera(int(linea[1]), linea[2], linea[6], linea[4], linea[3])
            else:
                unaFacu = Faculdad(int(linea[0]), linea[1], linea[2], linea[3], linea[4])
                self.__Facultades.append(unaFacu)
                cod = int(linea[0])

    def mostrar(self):
        for facultad in self.__Facultades:
            print(facultad)
            for carrera in facultad.get_carreras():
                print(carrera)

    def buscar_facultad(self, cod):
        i = 0
        while cod != int(self.__Facultades[i].get_cod()) and i < len(self.__Facultades):
            i += 1
        if cod == self.__Facultades[i].get_cod():
            print(f'La {self.__Facultades[i].get_nom()}')
            for carrera in self.__Facultades[i].get_carreras():
                print(f'Carrera: {carrera.get_nombre()} Duracion: {carrera.get_duracion()}')


    def buscar_carrera(self, nom):
        i = 0
        encontrado = False
        facultad = self.__Facultades

        while i < len(facultad) and encontrado == False:
            carrera = facultad[i].get_carreras()
            j = 0
            while j < len(carrera):
                unaC = carrera[j]
                if nom == str(unaC.get_nombre()):
                    print(f'Facultad:{facultad[i].get_nom()}')
                    print(f'Codigo de la Facultad: {facultad[i].get_cod()}')
                    print(f'Codigo de la Carrera: {unaC.get_codigo()}')
                    print(f'Localidad: {facultad[i].get_localidad()}')
                    encontrado = True
                j += 1
            i += 1
        if not encontrado:
            print(f'No se encontró la carrera {nom} en ninguna facultad.')

