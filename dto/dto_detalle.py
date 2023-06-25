from modelo.detalleMovimiento import DetalleMovimiento
from dao.dao_detalle import DaoDetalle


class DetalleDTO:
    def listDetalle(self, bodega, numeroProducto):
        daoDetalle = DaoDetalle()
        resu = daoDetalle.listDetalle(
            DetalleMovimiento(numeroBodega=bodega, numeroProducto=numeroProducto)
        )
        return resu
