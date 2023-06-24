from conex import conn
from modelo.producto import Producto
import traceback


class DaoProducto:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "proyectoInventario")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    def addProducto(self, producto):
        sql = "insert into producto values (null,%s, %s, %s, %s, %s, %s)"
        numero = producto.getNumero()
        nombre = producto.getNombre()
        descripcion = producto.getDescripcion()
        autor = producto.getAutor()
        editorial = producto.getEditorial().getNumero()
        categoria = producto.getCategoria().getId()
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(
                sql,
                (
                    numero,
                    nombre,
                    descripcion,
                    autor,
                    categoria,
                    editorial,
                ),
            )
            c.getConex().commit()
            filas = cursor.rowcount

            if filas > 0:
                mensaje = f"Producto Creado:\nId: {numero}\nNombre: {nombre.capitalize()}\nAutor: {autor.capitalize()}"
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

    def listProducto(self):
        c = self.getConex()
        lista = {}
        try:
            cursor = c.getConex().cursor()
            cursor.execute(
                """select pro.numeroProducto, pro.nombreProducto, 
                                pro.autorProducto, ed.nombreEditorial, cat.nombreCategoria
                                from producto pro, editorial ed, categoria cat
                                where pro.idEditorial = ed.idEditorial and 
                                pro.idCategoria = cat.idCategoria
                                order by pro.idProducto; """
            )
            resultado = cursor.fetchall()
            if resultado is not None:
                for a in resultado:
                    e = Producto(
                        numero=a[0],
                        nombre=a[1].capitalize(),
                        autor=a[2].capitalize(),
                        editorial=a[3].capitalize(),
                        categoria=a[4].capitalize(),
                    )
                    lista[a[0]] = e
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return lista

    def deleteProducto(self, producto):
        sql = "delete from producto where numeroproducto = %s"
        mensaje = ""
        c = self.getConex()

        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (producto.getNumero(),))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = f"Producto Eliminado:\nId: {producto.getNumero()}"
            else:
                mensaje = "No se realizaron cambios"

        except Exception as ex:
            print(traceback.print_exc())
            ex = str(ex)
            if ex.startswith("1451"):
                mensaje = "El producto está en uso\nNo se realizaron cambios"
            else:
                mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

    def findProducto(self, producto):
        c = self.getConex()
        resultado = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(
                f"""select pro.numeroProducto, pro.nombreProducto, 
                                pro.autorProducto, ed.nombreEditorial, cat.nombreCategoria
                                from producto pro, editorial ed, categoria cat
                                where pro.idEditorial = ed.idEditorial and 
                                pro.idCategoria = cat.idCategoria
                                and pro.numeroProducto = {producto.getNumero()}
                                order by pro.idProducto; """
            )
            resultado = cursor.fetchall()
            if resultado is not None:
                for a in resultado:
                    resultado = producto(
                        a[0],
                        a[1].capitalize(),
                        a[2].capitalize(),
                        a[3].capitalize(),
                        a[4].capitalize(),
                    )
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
