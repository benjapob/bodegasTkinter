from modelo.registroMovimiento import RegistroMovimiento
from dao.dao_registro import DaoRegistro


class RegistroDTO:
    def listRegistro(self):
        daoRegistro = DaoRegistro()
        resu = daoRegistro.listRegistro()
        return resu

    def createEntrada(self, id, proveedor, bodega, trabajador):
        daoRegistro = DaoRegistro()
        resultado = daoRegistro.addEntrada(
            RegistroMovimiento(
                id=id, proveedor=proveedor.upper(), bodega=bodega, trabajador=trabajador
            )
        )
        return resultado

    def createSalida(self, id, tienda, bodega, trabajador):
        daoRegistro = DaoRegistro()
        resultado = daoRegistro.addSalida(
            RegistroMovimiento(
                id=id,
                tiendaDestino=tienda.upper(),
                bodega=bodega,
                trabajador=trabajador,
            )
        )
        return resultado

    def createTraslado(self, id, bodegaOrigen, bodegaDestino, trabajador):
        daoRegistro = DaoRegistro()
        resultado = daoRegistro.addTraslado(
            RegistroMovimiento(
                id=id,
                bodegaOrigen=bodegaOrigen,
                bodega=bodegaDestino,
                trabajador=trabajador,
            )
        )
        return resultado
