from modelo.trabajador import Trabajador
from dao.dao_tr import TrDAO


class TrDTO:
    def validarLogin(self, correo, contraseña):
        daoTr = TrDAO()
        resultado = daoTr.validarLogin(Trabajador(correo=correo, contraseña=contraseña))
        return (
            Trabajador(
                nombre=resultado[0],
                apellido=resultado[1],
                rol=resultado[2],
                terminos=resultado[3],
                id=resultado[4],
            )
            if resultado is not None
            else None
        )

    def aceptaTerminos(self, id):
        daoTr = TrDAO()
        daoTr.aceptaTerminos(Trabajador(id=id))
