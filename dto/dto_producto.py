from modelo.producto import Producto
from modelo.editorial import Editorial
from modelo.categoria import Categoria
from dao.dao_producto import DaoProducto


class ProductoDTO:
    def listProducto(self):
        daoProducto = DaoProducto()
        resu = daoProducto.listProducto()
        return resu

    def createProducto(self, numero, nombre, desc, autor, editorial, categoria):
        daoProducto = DaoProducto()
        resultado = daoProducto.addProducto(
            Producto(
                numero=numero,
                nombre=nombre.upper(),
                descripcion=desc.upper(),
                autor=autor.upper(),
                editorial=Editorial(numero=editorial),
                categoria=Categoria(id=categoria),
            )
        )
        return resultado

    def updateProducto(self, numero, desc, autor, editorial):
        daoProducto = DaoProducto()
        resultado = daoProducto.updateProducto(
            Producto(
                numero=numero,
                descripcion=desc.upper(),
                autor=autor.upper(),
                editorial=Editorial(numero=editorial),
            )
        )
        return resultado

    def deleteProducto(self, numero):
        daoProducto = DaoProducto()
        resultado = daoProducto.deleteProducto(Producto(numero=numero))
        return resultado

    def findProducto(self, numero):
        daoProducto = DaoProducto()
        resultado = daoProducto.findProducto(Producto(numero=numero))
        return resultado if resultado is not None else None

    def findProductoNum(self, nombre):
        daoProducto = DaoProducto()
        resultado = daoProducto.findProductoNum(Producto(nombre=nombre.upper()))
        return resultado if resultado is not None else None
