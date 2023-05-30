class Carrera:

    def __init__(self, codigo, nombre, fecha_inicio, duracion, titulo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__duracion = duracion
        self.__titulo = titulo

    def __str__(self):
        return f'Codigo: {self.__codigo}, Nombre: {self.__nombre}, Fecha de Inicio: {self.__fecha_inicio}, Duracion: {self.__duracion}, Titulo: {self.__titulo}'

    def get_nombre(self):
        return self.__nombre

    def get_duracion(self):
        return self.__duracion

    def get_codigo(self):
        return self.__codigo