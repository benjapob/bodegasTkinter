class Bodega:
    # Constructor
    def __init__(self, id="", capacidad="", num="", trabajador=""):
        self.__id = id
        self.__capacidad = capacidad
        self.__num = num

        self.__trabajador = trabajador

    # Funcion str para hacer print al objeto

    def __str__(self) -> str:
        return f"{self.__id} {self.__capacidad} {self.__num}{self.__trabajador}"

    # Getters
    def getId(self):
        return self.__id

    def getCapacidad(self):
        return self.__capacidad

    def getNum(self):
        return self.__num

    def getTrabajador(self):
        return self.__trabajador

    # Setterr
    def setId(self, id):
        self.__id = id

    def setCapacidad(self, capacidad):
        self.__capacidad = capacidad

    def setNum(self, num):
        self.__num = num

    def setTrabajador(self, trabajador):
        self.__trabajador = trabajador
