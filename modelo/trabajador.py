# Importar funcion para encriptar contraseña
import sys, os

if __name__ == "__main__":
    sys.path.insert(1, os.path.join(os.path.dirname(sys.path[0]), "utils"))
    from encoder import Encoder
else:
    from utils.encoder import Encoder


class Trabajador:
    # Constructor
    def __init__(
        self,
        id="",
        nombre="",
        apellido="",
        rut="",
        correo="",
        contraseña="",
        rol="",
        terminos="",
    ):
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__rut = rut
        self.__correo = correo
        self.__contraseña = Encoder().encode(contraseña)
        self.__rol = rol
        self.__terminos = terminos

    # Funcion str para hacer print al objeto
    def __str__(self) -> str:
        return (
            f"{self.__id} {self.__nombre} {self.__apellido} {self.__rut} {self.__rol}"
        )

    # Getters
    def getId(self):
        return self.__id

    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getRut(self):
        return self.__rut

    def getCorreo(self):
        return self.__correo

    def getContraseña(self):
        return self.__contraseña

    def getRol(self):
        return self.__rol

    def getTerminos(self):
        return self.__terminos

    # Setters
    def setId(self, id):
        self.__id = id

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellido(self, apellido):
        self.__apellido = apellido

    def setRut(self, rut):
        self.__rut = rut

    def setCorreo(self, correo):
        self.__correo = correo

    def setContraseña(self, contraseña):
        self.__contraseña = Encoder().encode(contraseña)

    def setRol(self, rol):
        self.__rol = rol

    def setTerminos(self, terminos):
        self.__terminos = terminos
