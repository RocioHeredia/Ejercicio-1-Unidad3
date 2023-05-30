from ClassCarreras import Carrera
class Faculdad:

    def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__Carreras = []

    def agregar_carrera(self, cod, nom, fecha, duracion, titulo):
        self.__Carreras.append(Carrera(cod, nom, fecha, duracion, titulo))

    def __str__(self):
        return f'{self.__nombre} {self.__direccion} {self.__localidad} {self.__telefono}'

    def get_cod(self):
        return self.__codigo

    def get_nom(self):
        return self.__nombre

    def get_carreras(self):
        return self.__Carreras

    def get_localidad(self):
        return self.__localidad
