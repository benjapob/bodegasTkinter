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
                id=id, proveedor=proveedor, bodega=bodega, trabajador=trabajador
            )
        )
        return resultado
