from modelo.editorial import Editorial
from dao.dao_editorial import DaoEditorial


class EditorialDTO:
    def listarEditorial(self):
        daoEditorial = DaoEditorial()
        resu = daoEditorial.listarEditorial()
        return resu

    def createEditorial(self, id, nombre):
        daoEditorial = DaoEditorial()
        resultado = daoEditorial.addEditorial(
            Editorial(nombre=nombre.upper(), numero=id.upper())
        )
        return resultado

    """ def eliminarEditorial(self, numero):
        existe = self.buscarEditorial(numero)
        activo = self.activoEditorial(numero)
        if existe is not None and len(activo) == 0:
            conf = input(
                f"¿Estás seguro que quieres eliminar el Editorial {existe.getDescripcionEditorial()}? (Escribe s para confirmar): "
            )
            if conf == "s":
                daoEditorial = daoEditorial()
                resultado = daoEditorial.eliminarEditorial(Editorial(numero))
                return resultado
            else:
                resultado = "No se realizaron cambios"
                return resultado
        else:
            resultado = "Editorial no existe o está en uso"
            return resultado """
