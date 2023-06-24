from modelo.editorial import Editorial
from dao.dao_editorial import DaoEditorial


class EditorialDTO:
    def listEditorial(self):
        daoEditorial = DaoEditorial()
        resu = daoEditorial.listEditorial()
        return resu

    def createEditorial(self, numero, nombre):
        daoEditorial = DaoEditorial()
        resultado = daoEditorial.addEditorial(
            Editorial(nombre=nombre.upper(), numero=numero)
        )
        return resultado

    def deleteEditorial(self, numero):
        daoEditorial = DaoEditorial()
        resultado = daoEditorial.deleteEditorial(Editorial(numero=numero))
        return resultado

    def findEditorial(self, numero):
        daoEditorial = DaoEditorial()
        resultado = daoEditorial.findEditorial(Editorial(numero=numero))
        return resultado if resultado is not None else None
