from conex import conn
from modelo.bodega import Bodega
import traceback


class DaoBodega:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "proyectoInventario")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    def addBodega(self, bodega):
        sql = "insert into bodega values (null,%s, %s, 1)"
        numero = bodega.getNumero()
        capacidad = bodega.getCapacidad()
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(
                sql,
                (
                    capacidad,
                    numero,
                ),
            )
            c.getConex().commit()
            filas = cursor.rowcount

            if filas > 0:
                mensaje = f"Bodega Creada:\nId: {numero}"
            else:
                mensaje = "No se realizaron cambios"

        except Exception as ex:
            print(traceback.print_exc())
            ex = str(ex)

            if ex.startswith("1062"):
                mensaje = "Dato duplicado\nPor favor, ingresa un valor distinto"
            else:
                mensaje = "Problemas con la base de datos\nVuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

    def listBodega(self):
        c = self.getConex()
        lista = {}
        try:
            cursor = c.getConex().cursor()
            cursor.execute("select numerobodega, capacidadBodega from bodega")
            resultado = cursor.fetchall()
            if resultado is not None:
                for a in resultado:
                    e = Bodega(numero=a[0], capacidad=a[1])
                    lista[a[0]] = e
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return lista

    def deleteBodega(self, bodega):
        sql = "delete from bodega where numerobodega = %s"
        mensaje = ""
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (bodega.getNumero(),))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = f"Bodega Eliminada:\nId: {bodega.getNumero()}"
            else:
                mensaje = "No se realizaron cambios"

        except Exception as ex:
            print(traceback.print_exc())
            ex = str(ex)
            if ex.startswith("1451"):
                mensaje = "La bodega está en uso\nNo se realizaron cambios"
            else:
                mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

    def findBodega(self, bodega):
        c = self.getConex()
        resultado = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(
                f"select numerobodega, capacidadbodega from bodega where numerobodega = {bodega.getNumero()}"
            )
            resultado = cursor.fetchall()
            if resultado is not None:
                for a in resultado:
                    resultado = Bodega(numero=a[0], capacidad=a[1])
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
