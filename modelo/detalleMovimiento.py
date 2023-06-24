class DetalleMovimiento:
    # Constructor
    def __init__(
        self,
        id="",
        cantidad="",
        producto="",
        registro="",
    ):
        self.__id = id
        self.__cantidad = cantidad
        self.__producto = producto
        self.__registro = registro

    # Funcion str para hacer print al objeto

    def __str__(self) -> str:
        return f"{self.__id} {self.__cantidad} {self.__producto} {self.__registro}"

    # Getters
    def getId(self):
        return self.__id

    def getCantidad(self):
        return self.__cantidad

    def getProducto(self):
        return self.__producto

    def getRegistro(self):
        return self.__registro

    # Setterr
    def setId(self, id):
        self.__id = id

    def setCantidad(self, cantidad):
        self.__cantidad = cantidad

    def setProducto(self, producto):
        self.__producto = producto

    def setRegistro(self, registro):
        self.__registro = registro
