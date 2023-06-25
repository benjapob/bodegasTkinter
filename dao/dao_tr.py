from conex import conn
import traceback


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
