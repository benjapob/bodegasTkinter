import traceback, sys, os

if __name__ == "__main__":
    sys.path.insert(1, os.path.join(os.path.dirname(sys.path[0]), ""))
    sys.path.insert(1, os.path.join(os.path.dirname(sys.path[0]), "modelo"))
    from detalleMovimiento import DetalleMovimiento
    from conex import conn
else:
    from conex import conn
    from modelo.detalleMovimiento import DetalleMovimiento


class DaoDetalle:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "proyectoInventario")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn

    def listDetalle(self, detalle):
        c = self.getConex()
        lista = {}
        cantidad = 0
        e = DetalleMovimiento(numeroProducto=detalle.getNumeroProducto())

        try:
            cursor = c.getConex().cursor()
            cursor.execute(
                f"""select pro.numeroProducto, pro.nombreProducto, det.cantidadProducto,
                    ed.nombreEditorial, cat.nombreCategoria, bod.numeroBodega, tipo.nombreTipo, reg.bodegaOrigenDestino
                    from detalle_movimiento det, registro_movimiento reg, bodega bod, producto pro, editorial ed, categoria cat, tipo_movimiento tipo
                    where det.idRegistro = reg.idRegistro 
                    and det.idProducto = pro.idProducto 
                    and reg.idBodega = bod.idBodega  
                    and pro.idEditorial = ed.idEditorial  
                    and pro.idCategoria = cat.idCategoria 
                    and reg.idTipo = tipo.idTipo
                    and (bod.numeroBodega = {detalle.getNumeroBodega()} or reg.bodegaOrigenDestino = {detalle.getNumeroBodega()})
                    order by det.idDetalle;"""
            )
            resultado = cursor.fetchall()
            c.getConex().commit()
            if resultado is not None:
                for a in resultado:
                    if e.getNumeroProducto() != a[0]:
                        cantidad = 0

                    match a[6].capitalize():
                        case "Entrada":
                            cantidad += a[2]
                        case "Salida":
                            cantidad -= a[2]
                        case "Traslado":
                            if str(a[5]) == detalle.getNumeroBodega():
                                cantidad += a[2]
                            if str(a[7]) == detalle.getNumeroBodega():
                                cantidad -= a[2]
                    e = DetalleMovimiento(
                        numeroProducto=a[0],
                        nombreProducto=a[1].capitalize(),
                        cantidadProducto=cantidad,
                        nombreEditorial=a[3].capitalize(),
                        nombreCategoria=a[4].capitalize(),
                        numeroBodega=a[5],
                        nombreTipo=a[6].capitalize(),
                    )
                    lista[a[0]] = e
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return lista
