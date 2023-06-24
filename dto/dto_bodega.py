from modelo.bodega import Bodega
from dao.dao_bodega import DaoBodega


class BodegaDTO:
    def listBodega(self):
        daoBodega = DaoBodega()
        resu = daoBodega.listBodega()
        return resu

    def createBodega(self, numero, capacidad):
        daoBodega = DaoBodega()
        resultado = daoBodega.addBodega(Bodega(numero=numero, capacidad=capacidad))
        return resultado

    def deleteBodega(self, numero):
        daoBodega = DaoBodega()
        resultado = daoBodega.deleteBodega(Bodega(numero=numero))
        return resultado

    def findBodega(self, numero):
        daoBodega = DaoBodega()
        resultado = daoBodega.findBodega(Bodega(numero=numero))
        return resultado if resultado is not None else None
