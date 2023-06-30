from modelo.trabajador import Trabajador
from dao.dao_tr import TrDAO


class TrDTO:
    def listTrabajador(self):
        daoTrabajador = TrDAO()
        resu = daoTrabajador.listTrabajador()
        return resu

    def validarLogin(self, correo, contraseña):
        daoTr = TrDAO()
        resultado = daoTr.validarLogin(
            Trabajador(correo=correo.upper(), contraseña=contraseña.upper())
        )
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

    def findTrabajador(self, rut):
        daoTrabajador = TrDAO()
        resultado = daoTrabajador.findTrabajador(Trabajador(rut=rut.upper()))
        return resultado if resultado is not None else None
