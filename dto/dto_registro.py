from modelo.registroMovimiento import RegistroMovimiento
from dao.dao_registro import DaoRegistro


class RegistroDTO:
    def listRegistro(self):
        daoRegistro = DaoRegistro()
        resu = daoRegistro.listRegistro()
        return resu
