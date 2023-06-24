class Editorial:
    # Constructor
    def __init__(self, id="", numero="", nombre=""):
        self.__id = id
        self.__numero = numero
        self.__nombre = nombre

    # Funcion str para hacer print al objeto

    def __str__(self) -> str:
        return f"{self.__id} {self.__numero}{self.__nombre}"

    # Getters
    def getId(self):
        return self.__id

    def getNombre(self):
        return self.__nombre

    def getNumero(self):
        return self.__numero

    # Setters
    def setId(self, id):
        self.__id = id

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setNumero(self, numero):
        self.__numero = numero
