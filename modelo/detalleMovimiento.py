class DetalleMovimiento:
    # Constructor
    def __init__(
        self,
        id="",
        numeroProducto="",
        nombreProducto="",
        cantidadProducto="",
        nombreEditorial="",
        nombreCategoria="",
        numeroBodega="",
        nombreTipo="",
        registro="",
    ):
        self.__id = id
        self.__numeroProducto = numeroProducto
        self.__nombreProducto = nombreProducto
        self.__cantidadProducto = cantidadProducto
        self.__nombreEditorial = nombreEditorial
        self.__nombreCategoria = nombreCategoria
        self.__numeroBodega = numeroBodega
        self.__nombreTipo = nombreTipo
        self.__registro = registro

    # Funcion str para hacer print al objeto

    def __str__(self) -> str:
        return f"{self.__id}"

    # Getters
    def getId(self):
        return self.__id

    def getNumeroProducto(self):
        return self.__numeroProducto

    def getNombreProducto(self):
        return self.__nombreProducto

    def getCantidadProducto(self):
        return self.__cantidadProducto

    def getNombreEditorial(self):
        return self.__nombreEditorial

    def getNombreCategoria(self):
        return self.__nombreCategoria

    def getNumeroBodega(self):
        return self.__numeroBodega

    def getNombreTipo(self):
        return self.__nombreTipo

    def getRegistro(self):
        return self.__registro

    # Setterr
    def setId(self, id):
        self.__id = id

    def setNumeroProducto(self, numeroProducto):
        self.__numeroProducto = numeroProducto

    def setNombreProducto(self, nombreProducto):
        self.__nombreProducto = nombreProducto

    def setCantidadProducto(self, cantidadProducto):
        self.__cantidadProducto = cantidadProducto

    def setNombreEditorial(self, nombreEditorial):
        self.__nombreEditorial = nombreEditorial

    def setNombreCategoria(self, nombreCategoria):
        self.__nombreCategoria = nombreCategoria

    def setNumeroBodega(self, numeroBodega):
        self.__numeroBodega = numeroBodega

    def setNombreTipo(self, nombreTipo):
        self.__nombreTipo = nombreTipo

    def setRegistro(self, registro):
        self.__registro = registro
