class Producto:
    # Constructor
    def __init__(
        self,
        id="",
        numero="",
        nombre="",
        descripcion="",
        autor="",
        editorial="",
        categoria="",
    ):
        self.__id = id
        self.__numero = numero
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__autor = autor
        self.__editorial = editorial
        self.__categoria = categoria

    # Funcion str para hacer print al objeto

    def __str__(self) -> str:
        return f"{self.__id} {self.__numero} {self.__nombre} {self.__descripcion} {self.__autor} {self.__editorial} {self.__categoria}"

    # Getters
    def getId(self):
        return self.__id

    def getNumero(self):
        return self.__numero

    def getNombre(self):
        return self.__nombre

    def getDescripcion(self):
        return self.__descripcion

    def getAutor(self):
        return self.__autor

    def getEditorial(self):
        return self.__editorial

    def getCategoria(self):
        return self.__categoria

    # Setters
    def setId(self, id):
        self.__id = id

    def setNumero(self, numero):
        self.__numero = numero

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion

    def setAutor(self, autor):
        self.__autor = autor

    def setEditorial(self, editorail):
        self.__editorial = editorail

    def setCategoria(self, categoria):
        self.__categoria = categoria
