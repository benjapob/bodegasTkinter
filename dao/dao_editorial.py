from conex import conn
from modelo.editorial import Editorial
import traceback


class DaoEditorial:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "proyectoInventario")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    def addEditorial(self, editorial):
        sql = "insert into editorial values (null,%s, %s)"
        nombre = editorial.getNombre()
        numero = editorial.getNumero()
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(
                sql,
                (
                    numero,
                    nombre,
                ),
            )
            c.getConex().commit()
            filas = cursor.rowcount

            if filas > 0:
                mensaje = f"Editorial Creada:\nNumero: {numero.capitalize()}\nNombre: {nombre.capitalize()}"
            else:
                mensaje = "No se realizaron cambios"

        except Exception as ex:
            # print(traceback.print_exc())
            ex = str(ex)

            if ex.startswith("1062"):
                mensaje = "Dato duplicado\nPor favor, ingresa un valor distinto"
            else:
                mensaje = "Problemas con la base de datos\nVuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

    def eliminarEditorial(self, Editorial):
        sql = "delete from Editorial where numeroEditorial = %s"
        mensaje = ""
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (Editorial.getIdenticaEditorial(),))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Mensaje"
            else:
                mensaje = "No se realizaron cambios"

        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

    def listarEditorial(self):
        c = self.getConex()
        lista = {}
        try:
            cursor = c.getConex().cursor()
            cursor.execute("select numeroEditorial, nombreEditorial from editorial")
            resultado = cursor.fetchall()
            if resultado is not None:
                for a in resultado:
                    e = Editorial(numero=a[0], nombre=a[1])
                    lista[a[0]] = e
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return lista
