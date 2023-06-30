from conex import conn
from modelo.categoria import Categoria
import traceback


class DaoCategoria:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "proyectoInventario")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    def listCategoria(self):
        c = self.getConex()
        lista = {}
        try:
            cursor = c.getConex().cursor()
            cursor.execute("select nombrecategoria from categoria")
            resultado = cursor.fetchall()
            if resultado is not None:
                for a in resultado:
                    e = Categoria(nombre=a[0].capitalize())
                    lista[a[0]] = e
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return lista

    def findCategoria(self, categoria):
        c = self.getConex()
        resultado = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(
                f"select idcategoria from categoria where nombrecategoria = '{categoria.getNombre()}' "
            )
            resu = cursor.fetchone()
            if resu is not None:
                resultado = Categoria(id=resu[0])
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
