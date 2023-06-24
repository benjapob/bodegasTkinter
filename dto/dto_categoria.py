from modelo.categoria import Categoria
from dao.dao_categoria import DaoCategoria


class CategoriaDTO:
    def listCategoria(self):
        daoCategoria = DaoCategoria()
        resu = daoCategoria.listCategoria()
        return resu

    def findCategoria(self, nombre):
        daoCategoria = DaoCategoria()
        resultado = daoCategoria.findCategoria(Categoria(nombre=nombre.upper()))
        return resultado.getId() if resultado is not None else None
