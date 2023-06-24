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

    def validarLogin(self, emp):
        sql = "select nombreTrabajador, apellidoTrabajador, nombreRol from trabajador tr join rol r on tr.idRol = r.idRol where correo = %s and contraseña = %s;"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql,(emp.getCorreo(), emp.getContraseña()))
            resultado = cursor.fetchone()

        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()

        return resultado
    
