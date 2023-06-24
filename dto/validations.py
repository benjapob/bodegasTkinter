from dto.dto_tr import TrDTO

# Validaciones y utilidades


def volver():
    input("Presione enter para volver...\n")


def continuar():
    input("Presione enter para continuar...\n")


def validarCorreo():
    try:
        correo = input(f"Ingresar correo: ")
        if "@" in correo:
            return correo
        else:
            print("Debe ingresar un correo válido")
            return validarCorreo()
    except:
        print("Debe ingresar un correo válido")
        return validarCorreo()


def validarRut():
    try:
        rut = input(f"Ingresar rut (sin puntos y con guión): ")
        if len(rut) >= 9 and len(rut) <= 10:
            return rut
        else:
            print("Debe ingresar un rut válido")
            return validarRut()
    except:
        print("Debe ingresar un rut válido")
        return validarRut()


def validarInt(cadena):
    try:
        numero = int(input(f"Ingresar {cadena} (sólo números): "))
        if numero > 0:
            return numero
        else:
            print("Debe ingresar un número válido")
            return validarInt(cadena)
    except:
        print("Debe ingresar un número válido")
        return validarInt(cadena)


def validarFloat(cadena):
    try:
        numero = float(input(f"Ingresar {cadena} (sólo números): "))
        if numero > 0:
            return numero
        else:
            print("Debe ingresar un número válido")
            return validarFloat(cadena)
    except:
        print("Debe ingresar un número válido")
        return validarFloat(cadena)


def validarStr(cadena):
    try:
        string = input(f"Ingresar {cadena}: ")
        if len(string) > 0:
            return string.upper()
        else:
            print("El campo no puede estar vacío")
            return validarStr(cadena)
    except:
        print("El campo no puede estar vacío")
        return validarStr(cadena)


def validarLogin(correo, contraseña):
    resultado = TrDTO().validarLogin(correo, contraseña)
    return resultado


"""
#Funciones CRUD Comuna

def validaListarComunas():
    ComunaDTO().listarComunas();

def validaAgregarComuna():
    resultado = ComunaDTO().agregarComuna(validarInt('numero de la comuna'), validarStr('nombre de la comuna'));
    print(resultado);

def validaActualizarComuna():
    ComunaDTO().listarComunas();
    resultado = ComunaDTO().actualizarComuna(validarInt('numero de la comuna a editar'), input('Ingresar nuevo nombre de la comuna (Si no desea modificarlo, presione enter): '));
    print(resultado);

def validaEliminarComuna():
    ComunaDTO().listarComunas();
    resultado = ComunaDTO().eliminarComuna(validarInt('numero de la comuna a eliminar'))
    print(resultado)

#Funciones CRUD Cargo

def validaListarCargos():
    CargoDTO().listarCargos();

def validaAgregarCargo():
    resultado = CargoDTO().agregarCargo(validarInt('numero del cargo'), validarStr('nombre del cargo'));
    print(resultado);

def validaActualizarCargo():
    CargoDTO().listarCargos();
    resultado = CargoDTO().actualizarCargo(validarInt('numero del cargo a editar'), input('Ingresar nuevo nombre del cargo (Si no desea modificarlo, presione enter): '));
    print(resultado);

def validaEliminarCargo():
    CargoDTO().listarCargos();
    resultado = CargoDTO().eliminarCargo(validarInt('numero del cargo a eliminar'))
    print(resultado)

#Funciones CRUD Empleado

def validaEliminarEmpleado():
    EmpDTO().listarEmpleados();
    resultado = EmpDTO().eliminarEmpleado(validarStr('rut del empleado a eliminar'))
    print (resultado)

def validaActualizarEmpleado():
    EmpDTO().listarEmpleados();
    resultado = EmpDTO().actualizarEmpleado(validarStr('rut del empleado a modificar'), input('Ingresar nuevo nombre del empleado (Si no desea modificarlo, presione enter): '),input('Ingresar nuevo apellido del empleado (Si no desea modificarlo, presione enter): '), input('Ingresar nombre del cargo nuevo del empleado (Si no desea modificarlo, presione enter): '),input('Ingresar nueva dirección del empleado (Si no desea modificarlo, presione enter): '), input('Ingresar nombre de la comuna nueva del empleado (Si no desea modificarlo, presione enter): '))
    print(resultado)

def validaAgregarEmpleado():
    resultado = EmpDTO().agregarEmpleado(validarRut(), validarStr('nombre del empleado'),validarStr('apellido del empleado'), validarStr('nombre del cargo del empleado'),validarStr('dirección del empleado'), validarStr('clave del empleado'), validarCorreo(), validarStr('nombre de la comuna del empleado'));
    print(resultado);

def validaBuscarEmpleadoCargo():
    CargoDTO().listarCargos();
    lista = EmpDTO().buscarEmpleadoCargo(validarStr('nombre del cargo'))
    if lista is not None:
        if len(lista) != 0:
            for a in lista:
                print(a)
                print("")
        else:
            print('No hay empleados que tengan el cargo ingresado')
    else:
        print('El cargo ingresado no existe')

def validaBuscarEmpleadoComuna():
    ComunaDTO().listarComunas();
    lista = EmpDTO().buscarEmpleadoComuna(validarStr('nombre de la comuna'))
    if lista is not None:
        if len(lista) != 0:
            for a in lista:
                print(a)
                print("")
        else:
            print('No hay empleados que vivan en la comuna ingresada')
    else:
        print('La comuna ingresada no existe')
"""
