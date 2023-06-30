class RegistroMovimiento:
    # Constructor
    def __init__(
        self,
        id="",
        fecha="",
        tiendaDestino="",
        proveedor="",
        bodegaOrigen="",
        tipo="",
        bodega="",
        trabajador="",
    ):
        self.__id = id
        self.__fecha = fecha
        self.__tiendaDestino = tiendaDestino
        self.__proveedor = proveedor
        self.__bodegaOrigen = bodegaOrigen
        self.__tipo = tipo
        self.__bodega = bodega
        self.__trabajador = trabajador

    # Funcion str para hacer print al objeto

    def __str__(self) -> str:
        return f"{self.__id} {self.__fecha} {self.__tiendaDestino} {self.__proveedor} {self.__bodegaOrigen} {self.__tipo} {self.__bodega} {self.__trabajador}"

    # Getters
    def getId(self):
        return self.__id

    def getFecha(self):
        return self.__fecha

    def getTiendaDestino(self):
        return self.__tiendaDestino

    def getProveedor(self):
        return self.__proveedor

    def getbodegaOrigen(self):
        return self.__bodegaOrigen

    def getTipo(self):
        return self.__tipo

    def getBodega(self):
        return self.__bodega

    def getTrabajador(self):
        return self.__trabajador

    # Setterr
    def setId(self, id):
        self.__id = id

    def setFecha(self, fecha):
        self.__fecha = fecha
        self.__id = id

    def setTiendaDestino(self, tiendaDestino):
        self.__tiendaDestino = tiendaDestino
        self.__id = id

    def setProveedor(self, proveedor):
        self.__proveedor = proveedor
        self.__id = id

    def setbodegaOrigen(self, bodegaOrigen):
        self.__bodegaOrigen = bodegaOrigen

    def setTipo(self, tipo):
        self.__tipo = tipo

    def setBodega(self, bodega):
        self.__bodega = bodega

    def setTrabajador(self, trabajador):
        self.__trabajador = trabajador
