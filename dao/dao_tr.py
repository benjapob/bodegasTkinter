from conex import conn
import traceback
from modelo.trabajador import Trabajador


class TrDAO:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "proyectoInventario")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    def validarLogin(self, tr):
        sql = "select nombreTrabajador, apellidoTrabajador, nombreRol, terminos, idTrabajador from trabajador tr join rol r on tr.idRol = r.idRol where correo = %s and contraseña = %s;"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (tr.getCorreo(), tr.getContraseña()))
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()

        return resultado

    def aceptaTerminos(self, tr):
        sql = f"update trabajador set terminos = 1 where idTrabajador = {tr.getId()}"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(
                sql,
            )
            c.getConex().commit()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()

        return resultado

    def listTrabajador(self):
        c = self.getConex()
        lista = {}
        try:
            cursor = c.getConex().cursor()
            cursor.execute("select rutTrabajador from trabajador")
            resultado = cursor.fetchall()
            if resultado is not None:
                for a in resultado:
                    e = Trabajador(rut=a[0])
                    lista[a[0]] = e
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return lista

    def findTrabajador(self, trabajador):
        c = self.getConex()
        resultado = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(
                f"select idTrabajador from trabajador where rutTrabajador = '{trabajador.getRut()}'"
            )
            resu = cursor.fetchone()
            if resu is not None:
                resultado = Trabajador(id=resu[0])
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
