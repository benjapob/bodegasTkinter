from conex import conn
from modelo.registroMovimiento import RegistroMovimiento
from modelo.trabajador import Trabajador
import traceback


class DaoRegistro:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "proyectoInventario")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    def listRegistro(self):
        c = self.getConex()
        lista = {}
        try:
            cursor = c.getConex().cursor()
            cursor.execute(
                """select reg.idRegistro, reg.fechaCreacion, reg.tiendaDestino, reg.proveedor, 
                    reg.bodegaOrigen, tipo.nombreTipo, bod.numeroBodega, tr.nombreTrabajador, tr.apellidoTrabajador 
                    from registroMovimiento reg, tipoMovimiento tipo, bodega bod, trabajador tr 
                    where reg.idTipo = tipo.idTipo 
                    and reg.idBodega = bod.idBodega 
                    and reg.idTrabajador = tr.idTrabajador 
                    order by reg.idRegistro"""
            )
            resultado = cursor.fetchall()
            if resultado is not None:
                for a in resultado:
                    e = RegistroMovimiento(
                        id=a[0],
                        fecha=a[1],
                        tiendaDestino=a[2].capitalize(),
                        proveedor=a[3].capitalize(),
                        bodegaOrigen=a[4],
                        tipo=a[5].capitalize(),
                        bodega=a[6],
                        trabajador=Trabajador(
                            nombre=a[7].capitalize(), apellido=a[8].capitalize()
                        ),
                    )
                    lista[a[0]] = e
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return lista

    def addEntrada(self, registroMovimiento):
        sql = """insert into registroMovimiento 
        (`idRegistro`, `tiendaDestino`, `proveedor`, `bodegaOrigen`, `idTipo`, `idBodega`, `idTrabajador`)  
        values (%s,'', %s, '', 1, %s, %s)"""
        id = registroMovimiento.getId()
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(
                sql,
                (
                    id,
                    registroMovimiento.getProveedor(),
                    registroMovimiento.getBodega(),
                    registroMovimiento.getTrabajador(),
                ),
            )
            c.getConex().commit()
            filas = cursor.rowcount

            if filas > 0:
                mensaje = id
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

    def addSalida(self, registroMovimiento):
        sql = """insert into registroMovimiento 
        (`idRegistro`, `tiendaDestino`, `proveedor`, `bodegaOrigen`, `idTipo`, `idBodega`, `idTrabajador`)  
        values (%s,%s,'', '', 2, %s, %s)"""
        id = registroMovimiento.getId()
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(
                sql,
                (
                    id,
                    registroMovimiento.getTiendaDestino(),
                    registroMovimiento.getBodega(),
                    registroMovimiento.getTrabajador(),
                ),
            )
            c.getConex().commit()
            filas = cursor.rowcount

            if filas > 0:
                mensaje = id
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

    def addTraslado(self, registroMovimiento):
        sql = """insert into registroMovimiento 
        (`idRegistro`, `tiendaDestino`, `proveedor`, `bodegaOrigen`, `idTipo`, `idBodega`, `idTrabajador`)  
        values (%s,'','', %s, 3, %s, %s)"""
        id = registroMovimiento.getId()
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(
                sql,
                (
                    id,
                    registroMovimiento.getbodegaOrigen(),
                    registroMovimiento.getBodega(),
                    registroMovimiento.getTrabajador(),
                ),
            )
            c.getConex().commit()
            filas = cursor.rowcount

            if filas > 0:
                mensaje = id
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
