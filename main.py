# Import tkinter
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Import DTO
from dto.dto_tr import TrDTO
from dto.dto_editorial import EditorialDTO
from dto.dto_bodega import BodegaDTO
from dto.dto_producto import ProductoDTO
from dto.dto_categoria import CategoriaDTO
from dto.dto_registro import RegistroDTO
from dto.dto_detalle import DetalleDTO

import re


# Funciones tkinter
def defaultFont():
    "Establece el tamaño de la fuente"
    default_font = tk.font.nametofont("TkDefaultFont")
    default_font.configure(size=12)


def place_window_center(self):
    """Posiciona la ventana en el centro de la pantalla.
    No toma en cuenta el titulo"""

    self.update_idletasks()
    w_height = self.winfo_height()
    w_width = self.winfo_width()
    s_height = self.winfo_screenheight()
    s_width = self.winfo_screenwidth()
    xpos = (s_width - w_width) // 3
    ypos = (s_height - w_height) // 3
    self.geometry(f"+{xpos}+{ypos}")


# Validaciones entries
def validarStr(x) -> bool:
    # Valida que el input no esté vacío
    if x == "":
        return False

    else:
        return True


def validarCorreo(x) -> bool:
    # Valida que el input sea un mail
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    if re.fullmatch(regex, x):
        return True
    else:
        return False


def validarInt(x) -> bool:
    # Valida que el entero no sea menor a cero y que no esté vacío
    try:
        if int(x) > 0:
            return True
        else:
            return False
    except:
        return False


# Advertencias
def datosValidos(self):
    # Muestra una alerta con el siguiente texto
    ttk.dialogs.Messagebox.show_warning(
        f"Por favor, ingresa datos válidos", "Advertencia", alert=True, parent=self
    )


def submit(self, mensaje):
    ttk.dialogs.Messagebox.show_info(
        title="Aviso",
        message=mensaje,
        parent=self,
    )


def pregunta(self, mensaje):
    resp = ttk.dialogs.Messagebox.show_question(
        title="Pregunta", message=mensaje, parent=self, buttons=["No", "Si"]
    )
    return resp


# Funciones DTO-DAO Trabajador
def validarLogin(correo, contraseña):
    """Valida el login con un correo y contraseña,
    después irá a la base de datos y buscará un usuario"""

    resultado = TrDTO().validarLogin(correo, contraseña)
    return resultado


def listTrabajador():
    resultado = TrDTO().listTrabajador()
    return resultado


def findTrabajador(rut):
    "Busca una Trabajador por su rut"
    resultado = TrDTO().findTrabajador(rut)
    return resultado


def aceptaTerminos(id):
    TrDTO().aceptaTerminos(id)


# Funciones DTO-DAO Editorial
def createEditorial(numero, nombre):
    """Este método debe permitir ingresar los datos de un editorial nueva en la tabla Editorial de la base de datos ProyectoInventario.
    La base de datos tiene como valores únicos el número y el nombre,
    si se ingresa un valor duplicado se enviará mensaje respectivo y no permitir el ingreso.

    Retorna un str"""

    resultado = EditorialDTO().createEditorial(numero, nombre)
    return resultado


def listEditorial():
    """

    Se retorna una lista"""
    resultado = EditorialDTO().listEditorial()
    return resultado


def deleteEditorial(numero):
    "Elimina una editorial por su numero"
    resultado = EditorialDTO().deleteEditorial(numero)
    return resultado


def findEditorial(numero):
    "Busca una editorial por su numero"
    resultado = EditorialDTO().findEditorial(numero)
    return resultado


def findEditorialId(nombre):
    "Busca un Editorial por su nombre"
    resultado = EditorialDTO().findEditorialId(nombre)
    return resultado


# Funciones DTO-DAO Bodega
def createBodega(numero, capacidad):
    """Crea una Bodega con un numero y una capacidad
    después irá a la base de datos y creara la Bodega"""

    resultado = BodegaDTO().createBodega(numero, capacidad)
    return resultado


def listBodega():
    resultado = BodegaDTO().listBodega()
    return resultado


def deleteBodega(numero):
    "Elimina una Bodega por su numero"
    resultado = BodegaDTO().deleteBodega(numero)
    return resultado


def findBodega(numero):
    "Busca una Bodega por su numero"
    resultado = BodegaDTO().findBodega(numero)
    return resultado


# Funciones DTO-DAO Producto
def createProducto(numero, nombre, desc, autor, editorial, categoria):
    """Crea un Producto con un numero y una capacidad
    después irá a la base de datos y creara la Producto"""

    resultado = ProductoDTO().createProducto(
        numero, nombre, desc, autor, editorial, categoria
    )
    return resultado


def updateProducto(numero, desc, autor, editorial):
    """Edita un Producto con un numero y una capacidad
    después irá a la base de datos y edita el Producto"""

    resultado = ProductoDTO().updateProducto(numero, desc, autor, editorial)
    return resultado


def listProducto():
    resultado = ProductoDTO().listProducto()
    return resultado


def deleteProducto(numero):
    "Elimina un Producto por su numero"
    resultado = ProductoDTO().deleteProducto(numero)
    return resultado


def findProducto(numero):
    "Busca un Producto por su numero"
    resultado = ProductoDTO().findProducto(numero)
    return resultado


def findProductoNum(nombre):
    "Busca un Producto por su nombre"
    resultado = ProductoDTO().findProductoNum(nombre)
    return resultado


# Funciones DTO-DAO Categoria


def listCategoria():
    resultado = CategoriaDTO().listCategoria()
    return resultado


def findCategoriaId(nombre):
    "Busca un Categoria por su nombre"
    resultado = CategoriaDTO().findCategoria(nombre)
    return resultado


# Funciones DTO-DAO Registro


def listRegistro():
    resultado = RegistroDTO().listRegistro()
    return resultado


def createEntrada(id, proveedor, bodega, trabajador):
    """Crea un Entrada con un numero y una capacidad
    después irá a la base de datos y creara la Entrada"""

    resultado = RegistroDTO().createEntrada(id, proveedor, bodega, trabajador)
    return resultado


def createSalida(id, tienda, bodega, trabajador):
    """Crea un Salida con un numero y una capacidad
    después irá a la base de datos y creara la Salida"""

    resultado = RegistroDTO().createSalida(id, tienda, bodega, trabajador)
    return resultado


def createTraslado(id, bodegaOrigen, bodegaDestino, trabajador):
    """Crea un Traslado con un numero y una capacidad
    después irá a la base de datos y creara la Traslado"""

    resultado = RegistroDTO().createTraslado(
        id, bodegaOrigen, bodegaDestino, trabajador
    )
    return resultado


# Funciones DTO-DAO Detalle


def createDetalle(listaProducto, registro):
    """Crea un Detalle con un numero y una capacidad
    después irá a la base de datos y creara la Detalle"""

    resultado = DetalleDTO().createDetalle(listaProducto, registro)
    return resultado


def listDetalle(bodega, numeroProducto):
    resultado = DetalleDTO().listDetalle(bodega, numeroProducto)
    return resultado


# Ventanas de la aplicación
def main():
    login = ttk.Window("Librería el Gran Poeta", "superhero", resizable=(False, False))

    place_window_center(login)
    Login(login)
    login.mainloop()


class Login(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)
        self.intentos = 0
        defaultFont()

        # form variables
        self.correo = ttk.StringVar(value="")
        self.pw = ttk.StringVar(value="")

        # form header
        hdr_txt = "Ingresa un usuario y contraseña"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form entries
        self.crearFormEntry("Correo", self.correo, validarCorreo, "")
        self.crearFormEntry("Contraseña", self.pw, validarStr, "*")
        self.crearBotones()

    def crearFormEntry(self, label, entry, val, hide):
        # Crear input
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label, width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(
            master=container,
            textvariable=entry,
            validate="focus",
            show=hide,
            validatecommand=(self.register(val), "%P"),
        )
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def crearBotones(self):
        # Crear los botones
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        self.sub_btn = ttk.Button(
            master=container,
            text="Login",
            command=self.onSubmit,
            bootstyle=SUCCESS,
            width=6,
            state=NORMAL,
        )
        self.sub_btn.pack(side=RIGHT, padx=5)

        cnl_btn = ttk.Button(
            master=container,
            text="Salir",
            command=self.onCancel,
            bootstyle=DANGER,
            width=6,
        )
        cnl_btn.pack(side=LEFT, padx=5)

    def onSubmit(self):
        # Valida los datos y llama la funcion validarLogin
        if validarCorreo(self.correo.get()) and validarStr(self.pw.get()):
            try:
                resu = validarLogin(self.correo.get(), self.pw.get())
                if resu is not None:
                    if resu.getTerminos() == 0:
                        mensajeResp = f"""Términos y Condiciones de Uso\nEstos Términos y Condiciones de Uso regulan las reglas a que se sujeta la utilización de la  APP Inventario de Bodegas (en adelante, la APP), que puede descargarse desde el dominio https://www.inacap.cl \nLa descarga o utilización de la APP atribuye la condición de  Usuario a quien lo haga e implica la aceptación de todas las condiciones incluidas en este  documento y en la Política de Privacidad y el Aviso Legal de dicha página Web. \nEl Usuario debería leer estas condiciones cada vez que utilice la APP, ya que podrían ser  modificadas en lo sucesivo. \n¿Deseas aceptar los Términos y condiciones?"""
                        resp = pregunta(self, mensajeResp)
                        if resp == "No" or resp is None:
                            self.quit()
                        elif resp == "Si":
                            aceptaTerminos(resu.getId())
                    """Switch roles"""
                    match resu.getRol().lower():
                        case "jefe de bodega":
                            # Abre una nueva ventana con el menú para el jefe
                            window = MenuJefe(self, resu)
                            place_window_center(window)
                            window.grab_set()

                        case "bodeguero":
                            # Abre una nueva ventana con el menú para el bodeguero
                            window = MenuBodeguero(self, resu)
                            place_window_center(window)
                            window.grab_set()
                else:
                    self.intentos += 1
                    if self.intentos == 4:
                        ttk.dialogs.Messagebox.show_error(
                            f"Demasiados intentos fallidos", "Error", alert=True
                        )
                        # Cierra la aplicación
                        self.quit()
                    else:
                        ttk.dialogs.Messagebox.show_warning(
                            f"Correo o contraseña incorrecta, intentos restantes: {4 - self.intentos}",
                            "Advertencia",
                            alert=True,
                        )

            except Exception as es:
                print(es)
                ttk.dialogs.Messagebox.show_error(
                    f"Intentar nuevamente", "Error", alert=True
                )
        else:
            datosValidos(self)

    def onCancel(self):
        # Cierra la aplicación
        self.quit()


class MenuJefe(tk.Toplevel):
    def __init__(self, parent, resu):
        super().__init__(parent, padx=20, pady=10)

        # form header
        hdr_txt = f"Bienvenido Sr/Sra {resu.getNombre().capitalize()} {resu.getApellido().capitalize()}"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # Contenedor menú row 1
        containerRow1 = ttk.Frame(self)
        containerRow1.pack(fill=X, expand=YES, pady=(15, 10))

        self.create_buttonbox(
            containerRow1, "Crear \nProducto", self.createProducto, "add"
        )
        self.create_buttonbox(containerRow1, "Crear \nBodega", self.createBodega, "add")
        self.create_buttonbox(
            containerRow1, "Crear \nEditorial", self.createEditorial, "add"
        )

        # Contenedor menú row 2
        containerRow2 = ttk.Frame(self)
        containerRow2.pack(fill=X, expand=YES, pady=(15, 10))

        self.create_buttonbox(
            containerRow2, "Eliminar\nProducto", self.delProducto, "del"
        )
        self.create_buttonbox(containerRow2, "Eliminar\nBodega", self.delBodega, "del")
        self.create_buttonbox(
            containerRow2, "Eliminar\nEditorial", self.delEditorial, "del"
        )

        # Contenedor menú row 2
        containerRow3 = ttk.Frame(self)
        containerRow3.pack(fill=X, expand=YES, pady=(15, 10))

        self.create_buttonbox(
            containerRow3, "Editar\nProducto", self.updateProducto, "edit"
        )
        self.create_buttonbox(
            containerRow3, "Generar\nInforme\nGeneral", self.searchInfGeneral, "inf"
        )

        self.create_buttonbox(
            containerRow3, "Generar\nInforme\nBodega", self.searchInfBodega, "inf"
        )

        # Contenedor boton
        containerBtn = ttk.Frame(self)
        containerBtn.pack(fill=X, expand=YES, pady=(15, 10))

        self.create_buttonCancel(containerBtn, "Salir", self.on_cancel)

    def create_buttonbox(self, container, title, command, img):
        # Crear los botones
        button = tk.PhotoImage(file=f"img/{img}.png")
        # button = button.subsample(2, 2)
        menuBtn = ttk.Button(
            master=container,
            text=title,
            command=command,
            bootstyle=PRIMARY,
            padding=10,
            image=button,
            compound=LEFT,
        )
        menuBtn.image = button  # keep a reference!
        menuBtn.pack(side=LEFT, padx=15)

    def create_buttonCancel(self, container, title, command):
        cnl_btn = ttk.Button(
            master=container,
            text=title,
            command=command,
            bootstyle=DANGER,
            width=6,
        )
        cnl_btn.pack(side=LEFT, padx=15)

    def createProducto(self):
        window = CreateProducto(self)
        place_window_center(window)
        window.grab_set()

    def createBodega(self):
        window = CreateBodega(self)
        place_window_center(window)
        window.grab_set()

    def createEditorial(self):
        window = CreateEditorial(self)
        place_window_center(window)
        window.grab_set()

    def delProducto(self):
        window = DelProducto(self)
        place_window_center(window)
        window.grab_set()

    def delBodega(self):
        window = DelBodega(self)
        place_window_center(window)
        window.grab_set()

    def delEditorial(self):
        window = DelEditorial(self)
        place_window_center(window)
        window.grab_set()

    def updateProducto(self):
        window = UpdateProducto(self)
        place_window_center(window)
        window.grab_set()

    def searchInfBodega(self):
        window = SearchInfBodega(self)
        place_window_center(window)
        window.grab_set()

    def searchInfGeneral(self):
        window = SearchInfGeneral(self)
        place_window_center(window)
        window.grab_set()

    def on_cancel(self):
        """Cancel and close the application."""
        self.quit()


class CreateProducto(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, padx=20, pady=10)

        listaEditorial = []
        for a in listEditorial().values():
            listaEditorial.append(a.getNombre())

        if len(listaEditorial) == 0:
            ttk.dialogs.Messagebox.show_warning(
                message="No hay editoriales ingresadas\nPor favor, ingresa una editorial",
                parent=self,
            )
            self.destroy()
        else:
            listaCategoria = []
            for a in listCategoria().values():
                listaCategoria.append(a.getNombre())

            # form variables
            self.id = ttk.StringVar(value="")
            self.nombre = ttk.StringVar(value="")
            self.desc = ttk.StringVar(value="")
            self.autor = ttk.StringVar(value="")
            self.editorial = ttk.StringVar(value="")
            self.categoria = ttk.StringVar(value="")

            # header and labelframe option container
            option_text = "Ingresa los datos del producto a crear"
            self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
            self.option_lf.pack(fill=X, expand=YES, anchor=N)

            # form entries
            self.idEntry = self.create_form_entry("id", self.id, validarInt)
            self.nombreEntry = self.create_form_entry("nombre", self.nombre, validarStr)
            self.descEntry = self.create_form_entry(
                "descripcion", self.desc, validarStr
            )
            self.autorEntry = self.create_form_entry("autor", self.autor, validarStr)
            self.editorialEntry = self.create_form_entry_combo(
                "categoria", self.categoria, validarStr, listaCategoria
            )
            self.categoriaEntry = self.create_form_entry_combo(
                "editorial", self.editorial, validarStr, listaEditorial
            )
            self.create_buttonbox()

            # form header
            hdr_txt = "Lista de Productos"
            hdr = ttk.Label(master=self, text=hdr_txt, width=50)
            hdr.pack(fill=X, pady=10)

            self.create_results_view()
            self.update_results_view()

    def create_form_entry(self, label, variable, val):
        # Crear una entrada
        container = ttk.Frame(self.option_lf)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(
            master=container,
            textvariable=variable,
            validate="focus",
            validatecommand=(self.register(val), "%P"),
        )
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

        return ent

    def create_form_entry_combo(self, label, variable, val, list):
        # Crear una entrada

        container = ttk.Frame(self.option_lf)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Combobox(
            master=container,
            textvariable=variable,
            validate="focus",
            validatecommand=(self.register(val), "%P"),
            values=list,
            state=READONLY,
        )
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

        return ent

    def create_buttonbox(self):
        # Crear los botones
        container = ttk.Frame(self.option_lf)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Crear",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)

    def create_results_view(self):
        """Add result treeview to labelframe"""
        self.resultview = ttk.Treeview(
            master=self, bootstyle=INFO, columns=[0, 1, 2, 3, 4], show=HEADINGS
        )
        self.resultview.pack(fill=BOTH, expand=YES, pady=10)

        # setup columns and use `scale_size` to adjust for resolution
        self.resultview.heading(0, text="Id", anchor=W)
        self.resultview.heading(1, text="Producto", anchor=W)
        self.resultview.heading(2, text="Autor", anchor=W)
        self.resultview.heading(3, text="Editorial", anchor=W)
        self.resultview.heading(4, text="Categoría", anchor=W)
        self.resultview.column(column=0, anchor=W)
        self.resultview.column(column=1, anchor=W)
        self.resultview.column(column=2, anchor=W)
        self.resultview.column(column=3, anchor=W)
        self.resultview.column(column=4, anchor=W)

    def update_results_view(self):
        for item in self.resultview.get_children():
            self.resultview.delete(item)
        for a in listProducto().values():
            iid = self.resultview.insert(
                parent="",
                index=END,
            )

            self.resultview.item(
                iid,
                open=True,
                values=[
                    a.getNumero(),
                    a.getNombre(),
                    a.getAutor(),
                    a.getEditorial(),
                    a.getCategoria(),
                ],
            )

    def on_submit(self):
        # Valida las entradas y llama la función createProducto()
        id = self.id.get()
        nombre = self.nombre.get()
        desc = self.desc.get()
        autor = self.autor.get()
        categoria = self.categoria.get()
        editorial = self.editorial.get()
        if (
            validarInt(id)
            and validarStr(nombre)
            and validarStr(desc)
            and validarStr(autor)
            and validarStr(categoria)
            and validarStr(editorial)
        ):
            categoria = findCategoriaId(categoria)
            editorial = findEditorialId(editorial)
            mensaje = createProducto(id, nombre, desc, autor, categoria, editorial)
            self.update_results_view()

            submit(self, mensaje)
            self.idEntry.delete(0, END)
            self.nombreEntry.delete(0, END)
            self.descEntry.delete(0, END)
            self.autorEntry.delete(0, END)
            self.editorialEntry.set("")
            self.categoriaEntry.set("")

        else:
            datosValidos(self)


class CreateBodega(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, padx=20, pady=10)

        # form variables
        self.numero = ttk.StringVar(value="")
        self.capacidad = ttk.StringVar(value="")

        # header and labelframe option container
        option_text = "Ingresa los datos de la bodega a crear"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)
        # form entries
        self.numeroEntry = self.create_form_entry("id", self.numero, validarInt)
        self.capacidadEntry = self.create_form_entry(
            "capacidad", self.capacidad, validarInt
        )
        self.create_buttonbox()

        # form header
        hdr_txt = "Lista de Bodegas"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        self.create_results_view()
        self.update_results_view()

    def create_form_entry(self, label, variable, val):
        # Crear una entrada
        container = ttk.Frame(self.option_lf)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(
            master=container,
            textvariable=variable,
            validate="focus",
            validatecommand=(self.register(val), "%P"),
        )
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

        return ent

    def create_buttonbox(self):
        # Crear los botones
        container = ttk.Frame(self.option_lf)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Crear",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)

    def create_results_view(self):
        """Add result treeview to labelframe"""
        self.resultview = ttk.Treeview(
            master=self, bootstyle=INFO, columns=[0, 1], show=HEADINGS
        )
        self.resultview.pack(fill=BOTH, expand=YES, pady=10)

        # setup columns and use `scale_size` to adjust for resolution
        self.resultview.heading(0, text="Numero", anchor=W)
        self.resultview.heading(1, text="Capacidad", anchor=W)
        self.resultview.column(column=0, anchor=W)
        self.resultview.column(column=1, anchor=W)

    def update_results_view(self):
        for item in self.resultview.get_children():
            self.resultview.delete(item)
        for a in listBodega().values():
            iid = self.resultview.insert(
                parent="",
                index=END,
            )

            self.resultview.item(
                iid, open=True, values=[a.getNumero(), a.getCapacidad()]
            )

    def on_submit(self):
        # Valida las entradas y llama la función createBodega()
        numero = self.numero.get()
        capacidad = self.capacidad.get()

        if validarInt(numero) and validarInt(capacidad):
            mensaje = createBodega(numero, capacidad)
            self.update_results_view()

            submit(self, mensaje)
            self.numeroEntry.delete(0, END)
            self.capacidadEntry.delete(0, END)

        else:
            datosValidos(self)


class CreateEditorial(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, padx=20, pady=10)

        # form variables
        self.numero = ttk.StringVar(value="")
        self.nombre = ttk.StringVar(value="")

        # header and labelframe option container
        option_text = "Ingresa los datos de la editorial a crear"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)

        # form entries
        self.numeroEntry = self.create_form_entry("numero", self.numero, validarInt)
        self.nombreEntry = self.create_form_entry("nombre", self.nombre, validarStr)
        self.create_buttonbox()

        # form header
        hdr_txt = "Lista de Editoriales"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        self.create_results_view()
        self.update_results_view()

    def create_form_entry(self, label, variable, val):
        # Crear una entrada
        container = ttk.Frame(self.option_lf)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(
            master=container,
            textvariable=variable,
            validate="focus",
            validatecommand=(self.register(val), "%P"),
        )
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

        return ent

    def create_buttonbox(self):
        # Crear los botones
        container = ttk.Frame(self.option_lf)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Crear",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)

    def create_results_view(self):
        """Add result treeview to labelframe"""
        self.resultview = ttk.Treeview(
            master=self, bootstyle=INFO, columns=[0, 1], show=HEADINGS
        )
        self.resultview.pack(fill=BOTH, expand=YES, pady=10)

        # setup columns and use `scale_size` to adjust for resolution
        self.resultview.heading(0, text="Id", anchor=W)
        self.resultview.heading(1, text="Nombre", anchor=W)
        self.resultview.column(column=0, anchor=W)
        self.resultview.column(column=1, anchor=W)

    def update_results_view(self):
        for item in self.resultview.get_children():
            self.resultview.delete(item)
        for a in listEditorial().values():
            iid = self.resultview.insert(
                parent="",
                index=END,
            )

            self.resultview.item(
                iid, open=True, values=[a.getNumero(), a.getNombre().capitalize()]
            )

    def on_submit(self):
        # Valida las entradas y llama la función createEditorial()
        numero = self.numero.get()
        nombre = self.nombre.get()

        if validarInt(numero) and validarStr(nombre):
            mensaje = createEditorial(numero, nombre)
            self.update_results_view()

            submit(self, mensaje)
            self.numeroEntry.delete(0, END)
            self.nombreEntry.delete(0, END)

        else:
            datosValidos(self)


class DelProducto(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, padx=20, pady=10)

        # form variables
        self.id = ttk.StringVar(value="")

        # header and labelframe option container
        option_text = "Eliminar Producto por Id"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)

        self.idEntry = self.create_term_row()

        # form header
        hdr_txt = "Lista de Productos"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        self.create_results_view()
        self.update_results_view()

    def create_term_row(self):
        """Add term row to labelframe"""
        term_row = ttk.Frame(self.option_lf)
        term_row.pack(fill=X, expand=YES, pady=15)
        term_lbl = ttk.Label(term_row, text="Id", width=18)
        term_lbl.pack(side=LEFT, padx=(15, 0))
        term_ent = ttk.Entry(
            term_row,
            textvariable=self.id,
            validate="focus",
            validatecommand=(self.register(validarInt), "%P"),
        )
        term_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        search_btn = ttk.Button(
            master=term_row,
            text="Eliminar",
            command=self.on_submit,
            bootstyle=DANGER,
            width=8,
        )
        search_btn.pack(side=LEFT, padx=5)
        return term_ent

    def create_results_view(self):
        """Add result treeview to labelframe"""
        self.resultview = ttk.Treeview(
            master=self, bootstyle=INFO, columns=[0, 1, 2, 3, 4], show=HEADINGS
        )
        self.resultview.pack(fill=BOTH, expand=YES, pady=10)

        # setup columns and use `scale_size` to adjust for resolution
        self.resultview.heading(0, text="Id", anchor=W)
        self.resultview.heading(1, text="Producto", anchor=W)
        self.resultview.heading(2, text="Autor", anchor=W)
        self.resultview.heading(3, text="Editorial", anchor=W)
        self.resultview.heading(4, text="Categoría", anchor=W)
        self.resultview.column(column=0, anchor=W)
        self.resultview.column(column=1, anchor=W)
        self.resultview.column(column=2, anchor=W)
        self.resultview.column(column=3, anchor=W)
        self.resultview.column(column=4, anchor=W)

    def update_results_view(self):
        for item in self.resultview.get_children():
            self.resultview.delete(item)
        for a in listProducto().values():
            iid = self.resultview.insert(
                parent="",
                index=END,
            )

            self.resultview.item(
                iid,
                open=True,
                values=[
                    a.getNumero(),
                    a.getNombre(),
                    a.getAutor(),
                    a.getEditorial(),
                    a.getCategoria(),
                ],
            )

    def on_submit(self):
        # Valida las entradas y llama la función delProducto()
        if validarInt(self.id.get()):
            buscar = findProducto(self.id.get())
            if buscar:
                mensajeResp = f"Estás a punto de eliminar el Producto:\nId: {buscar.getNumero()}\nNombre: {buscar.getNombre()}\n ¿Estás seguro?"
                resp = pregunta(self, mensajeResp)
                if resp == "Si":
                    mensaje = deleteProducto(self.id.get())
                    self.update_results_view()
                elif resp == "No" or resp is None:
                    mensaje = "No se realizaron cambios"
            else:
                mensaje = f"No se pudo encontrar el Producto"

            submit(self, mensaje)
            self.idEntry.delete(0, END)
        else:
            datosValidos(self)


class DelBodega(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, padx=20, pady=10)

        # form variables
        self.id = ttk.StringVar(value="")

        # header and labelframe option container
        option_text = "Eliminar Bodega por Id"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)

        self.idEntry = self.create_term_row()

        # form header
        hdr_txt = "Lista de Bodegas"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        self.create_results_view()
        self.update_results_view()

    def create_term_row(self):
        """Add term row to labelframe"""
        term_row = ttk.Frame(self.option_lf)
        term_row.pack(fill=X, expand=YES, pady=15)
        term_lbl = ttk.Label(term_row, text="Id", width=18)
        term_lbl.pack(side=LEFT, padx=(15, 0))
        term_ent = ttk.Entry(
            term_row,
            textvariable=self.id,
            validate="focus",
            validatecommand=(self.register(validarInt), "%P"),
        )
        term_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        search_btn = ttk.Button(
            master=term_row,
            text="Eliminar",
            command=self.on_submit,
            bootstyle=DANGER,
            width=8,
        )
        search_btn.pack(side=LEFT, padx=5)

        return term_ent

    def create_results_view(self):
        """Add result treeview to labelframe"""
        self.resultview = ttk.Treeview(
            master=self, bootstyle=INFO, columns=[0, 1, 2], show=HEADINGS
        )
        self.resultview.pack(fill=BOTH, expand=YES, pady=10)

        # setup columns and use `scale_size` to adjust for resolution
        self.resultview.heading(0, text="Id", anchor=W)
        self.resultview.heading(1, text="Numero", anchor=W)
        self.resultview.heading(2, text="Capacidad", anchor=W)
        self.resultview.column(column=0, anchor=W)
        self.resultview.column(column=1, anchor=W)
        self.resultview.column(column=2, anchor=W)

        # insert falso

        iid = self.resultview.insert(
            parent="",
            index=END,
        )

        self.resultview.item(iid, open=True, values=[1, 2, 300])

    def update_results_view(self):
        for item in self.resultview.get_children():
            self.resultview.delete(item)
        for a in listBodega().values():
            iid = self.resultview.insert(
                parent="",
                index=END,
            )

            self.resultview.item(
                iid, open=True, values=[a.getNumero(), a.getCapacidad()]
            )

    def on_submit(self):
        # Valida las entradas y llama la función delBodega()
        if validarInt(self.id.get()):
            buscar = findBodega(self.id.get())
            if buscar:
                mensajeResp = f"Estás a punto de eliminar la Bodega:\nId: {buscar.getNumero()}\nCapacidad: {buscar.getCapacidad()}\n ¿Estás seguro?"
                resp = pregunta(self, mensajeResp)
                if resp == "Si":
                    mensaje = deleteBodega(self.id.get())
                    self.update_results_view()
                elif resp == "No" or resp is None:
                    mensaje = "No se realizaron cambios"
            else:
                mensaje = f"No se pudo encontrar la Bodega"

            submit(self, mensaje)
            self.idEntry.delete(0, END)
        else:
            datosValidos(self)


class DelEditorial(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, padx=20, pady=10)

        # form variables
        self.id = ttk.StringVar(value="")

        # header and labelframe option container
        option_text = "Eliminar Editorial por Id"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)

        self.idEntry = self.create_term_row()

        # form header
        hdr_txt = "Lista de Editoriales"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        self.create_results_view()
        self.update_results_view()

    def create_term_row(self):
        """Add term row to labelframe"""
        term_row = ttk.Frame(self.option_lf)
        term_row.pack(fill=X, expand=YES, pady=15)
        term_lbl = ttk.Label(term_row, text="Id", width=18)
        term_lbl.pack(side=LEFT, padx=(15, 0))
        term_ent = ttk.Entry(
            term_row,
            textvariable=self.id,
            validate="focus",
            validatecommand=(self.register(validarInt), "%P"),
        )
        term_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        search_btn = ttk.Button(
            master=term_row,
            text="Eliminar",
            command=self.on_submit,
            bootstyle=DANGER,
            width=8,
        )
        search_btn.pack(side=LEFT, padx=5)
        return term_ent

    def create_results_view(self):
        """Add result treeview to labelframe"""
        self.resultview = ttk.Treeview(
            master=self, bootstyle=INFO, columns=[0, 1], show=HEADINGS
        )
        self.resultview.pack(fill=BOTH, expand=YES, pady=10)

        # setup columns and use `scale_size` to adjust for resolution
        self.resultview.heading(0, text="Id", anchor=W)
        self.resultview.heading(1, text="Nombre", anchor=W)
        self.resultview.column(column=0, anchor=W)
        self.resultview.column(column=1, anchor=W)

    def update_results_view(self):
        for item in self.resultview.get_children():
            self.resultview.delete(item)
        for a in listEditorial().values():
            iid = self.resultview.insert(
                parent="",
                index=END,
            )

            self.resultview.item(
                iid, open=True, values=[a.getNumero(), a.getNombre().capitalize()]
            )

    def on_submit(self):
        # Valida las entradas y llama la función deleteEditorial()
        if validarInt(self.id.get()):
            buscar = findEditorial(self.id.get())
            if buscar:
                mensaje = f"Estás a punto de eliminar la editorial:\nId: {buscar.getNumero()}\nNombre: {buscar.getNombre()}\n ¿Estás seguro?"
                resp = pregunta(self, mensaje)
                if resp == "Si":
                    mensaje = deleteEditorial(self.id.get())
                    self.update_results_view()
                    submit(self, mensaje)
                elif resp == "No" or resp is None:
                    mensaje = "No se realizaron cambios"
                    submit(self, mensaje)
            else:
                mensaje = f"No se pudo encontrar la editorial"
                submit(self, mensaje)
            self.idEntry.delete(0, END)
        else:
            datosValidos(self)


class UpdateProducto(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, padx=20, pady=10)

        listaEditorial = []
        for a in listEditorial().values():
            listaEditorial.append(a.getNombre())

        if len(listaEditorial) == 0:
            ttk.dialogs.Messagebox.show_warning(
                message="No hay editoriales ingresadas\nPor favor, ingresa una editorial",
                parent=self,
            )
            self.destroy()
        else:
            # form variables
            self.id = ttk.StringVar(value="")
            self.desc = ttk.StringVar(value="")
            self.autor = ttk.StringVar(value="")
            self.editorial = ttk.StringVar(value="")

            # header and labelframe option container
            option_text2 = "Ingresa la Id del Producto a Editar"
            self.option_lf2 = ttk.Labelframe(self, text=option_text2, padding=15)
            self.option_lf2.pack(fill=X, expand=YES, anchor=N)

            # header and labelframe option container
            option_text = "Ingresa los Nuevos Datos"
            self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
            self.option_lf.pack(fill=X, expand=YES, anchor=N, pady=10)

            # form entries
            self.idEntry = self.create_form_entry2("id", self.id, validarInt)
            self.descEntry = self.create_form_entry(
                "descripcion", self.desc, validarStr
            )
            self.autorEntry = self.create_form_entry("autor", self.autor, validarStr)
            self.editorialEntry = self.create_form_entry_combo(
                "editorial", self.editorial, validarStr, listaEditorial
            )

            # form header
            hdr_txt = "Lista de Productos"
            hdr = ttk.Label(master=self, text=hdr_txt, width=50)
            hdr.pack(fill=X, pady=10)

            self.create_results_view()
            self.create_buttonbox()
            self.update_results_view()

    def create_form_entry2(self, label, variable, val):
        # Crear una entrada
        container = ttk.Frame(self.option_lf2)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(
            master=container,
            textvariable=variable,
            validate="focus",
            validatecommand=(self.register(val), "%P"),
        )
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        return ent

    def create_form_entry(self, label, variable, val):
        # Crear una entrada
        container = ttk.Frame(self.option_lf)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(
            master=container,
            textvariable=variable,
        )
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        return ent

    def create_form_entry_combo(self, label, variable, val, list):
        # Crear una entrada
        container = ttk.Frame(self.option_lf)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Combobox(
            master=container,
            textvariable=variable,
            values=list,
            state=READONLY,
        )
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)
        return ent

    def create_buttonbox(self):
        # Crear los botones
        container = ttk.Frame(self.option_lf)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Editar",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)

    def create_results_view(self):
        """Add result treeview to labelframe"""
        self.resultview = ttk.Treeview(
            master=self, bootstyle=INFO, columns=[0, 1, 2, 3, 4], show=HEADINGS
        )
        self.resultview.pack(fill=BOTH, expand=YES, pady=10)
        # setup columns and use `scale_size` to adjust for resolution
        self.resultview.heading(0, text="Id", anchor=W)
        self.resultview.heading(1, text="Producto", anchor=W)
        self.resultview.heading(2, text="Autor", anchor=W)
        self.resultview.heading(3, text="Editorial", anchor=W)
        self.resultview.heading(4, text="Categoría", anchor=W)
        self.resultview.column(column=0, anchor=W)
        self.resultview.column(column=1, anchor=W)
        self.resultview.column(column=2, anchor=W)
        self.resultview.column(column=3, anchor=W)
        self.resultview.column(column=4, anchor=W)

    def update_results_view(self):
        for item in self.resultview.get_children():
            self.resultview.delete(item)
        for a in listProducto().values():
            iid = self.resultview.insert(
                parent="",
                index=END,
            )

            self.resultview.item(
                iid,
                open=True,
                values=[
                    a.getNumero(),
                    a.getNombre(),
                    a.getAutor(),
                    a.getEditorial(),
                    a.getCategoria(),
                ],
            )

    def on_submit(self):
        # Valida las entradas y llama la función createProducto()
        if validarInt(self.id.get()):
            buscar = findProducto(self.id.get())
            if buscar:
                mensaje = updateProducto(
                    self.id.get(),
                    self.desc.get(),
                    self.autor.get(),
                    self.editorial.get(),
                )
                self.update_results_view()

            else:
                mensaje = f"No se pudo encontrar el Producto"

            submit(self, mensaje)
            self.idEntry.delete(0, END)
            self.descEntry.delete(0, END)
            self.autorEntry.delete(0, END)
            self.editorialEntry.set("")
        else:
            datosValidos(self)


class SearchInfGeneral(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master, padx=20, pady=10)

        # form header
        hdr_txt = "Informe de Movimientos"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        self.create_results_view()
        self.update_results_view()

    def create_results_view(self):
        """Add result treeview to labelframe"""
        self.resultview = ttk.Treeview(
            master=self, bootstyle=INFO, columns=[0, 1, 2, 3, 4, 5], show=HEADINGS
        )
        self.resultview.pack(fill=BOTH, expand=YES, pady=10)

        # setup columns and use `scale_size` to adjust for resolution
        self.resultview.heading(0, text="Id", anchor=W)
        self.resultview.heading(1, text="Fecha", anchor=W)
        self.resultview.heading(2, text="Origen", anchor=W)
        self.resultview.heading(3, text="Destino", anchor=W)
        self.resultview.heading(4, text="Tipo", anchor=W)
        self.resultview.heading(5, text="Empleado encargado", anchor=W)
        self.resultview.column(column=0, anchor=W)
        self.resultview.column(column=1, anchor=W)
        self.resultview.column(column=2, anchor=W)
        self.resultview.column(column=3, anchor=W)
        self.resultview.column(column=4, anchor=W)
        self.resultview.column(column=5, anchor=W)

    def update_results_view(self):
        for item in self.resultview.get_children():
            self.resultview.delete(item)
        for a in listRegistro().values():
            iid = self.resultview.insert(
                parent="",
                index=END,
            )
            match a.getTipo():
                case "Entrada":
                    origen = f"Proveedor: {a.getProveedor()}"
                    destino = f"Bodega: {a.getBodega()}"
                case "Salida":
                    origen = f"Bodega: {a.getBodega()}"
                    destino = f"Tienda: {a.getTiendaDestino()}"
                case "Traslado":
                    origen = f"Bodega: {a.getbodegaOrigen()}"
                    destino = f"Bodega: {a.getBodega()}"

            self.resultview.item(
                iid,
                open=True,
                values=[
                    a.getId(),
                    a.getFecha(),
                    origen,
                    destino,
                    a.getTipo(),
                    f"{a.getTrabajador().getNombre()} {a.getTrabajador().getApellido()}",
                ],
            )


class SearchInfBodega(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, padx=20, pady=10)

        # form variables
        self.numero = ttk.StringVar(value="")

        # form header
        hdr_txt = "Ingresa el número de la bodega a buscar"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form entries
        self.create_form_entry("numero", self.numero, validarInt)
        self.create_buttonbox()

    def create_form_entry(self, label, variable, val):
        # Crear una entrada
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=10)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(
            master=container,
            textvariable=variable,
            validate="focus",
            validatecommand=(self.register(val), "%P"),
        )
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def create_buttonbox(self):
        # Crear los botones
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        sub_btn = ttk.Button(
            master=container,
            text="Buscar",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)

    def on_submit(self):
        # Valida las entradas y abre el informe()
        if validarInt(self.numero.get()):
            try:
                numeroProducto = next(iter(listProducto()))
                resultado = listDetalle(self.numero.get(), numeroProducto)
                if resultado:
                    window = SearchInfBodegaCont(self, resultado)
                    place_window_center(window)
                    window.grab_set()
                else:
                    submit(
                        self,
                        "No se pudo encontrar la bodega o no tiene productos asociados",
                    )
            except:
                submit(self, "Por favor, ingresa un movimiento")
        else:
            datosValidos(self)


class SearchInfBodegaCont(tk.Toplevel):
    def __init__(self, master, resultado):
        super().__init__(master, padx=20, pady=10)

        self.resultado = resultado

        # application variables
        self.filtro = ttk.StringVar(value="")

        # header and labelframe option container
        option_text = "Movimientos por Bodega"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)

        self.filtroEntry = self.create_term_row()
        self.create_results_view()
        self.update_results_view(resultado)

    def create_term_row(self):
        """Add term row to labelframe"""
        term_row = ttk.Frame(self.option_lf)
        term_row.pack(fill=X, expand=YES, pady=15)
        term_lbl = ttk.Label(term_row, text="Filtrar por Editorial", width=18)
        term_lbl.pack(side=LEFT, padx=(15, 0))
        term_ent = ttk.Entry(
            term_row,
            textvariable=self.filtro,
            validate="focus",
            validatecommand=(self.register(validarStr), "%P"),
        )
        term_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        search_btn = ttk.Button(
            master=term_row,
            text="Filtrar",
            command=self.on_search,
            bootstyle=OUTLINE,
            width=8,
        )
        search_btn.pack(side=LEFT, padx=5)
        return term_ent

    def create_results_view(self):
        """Add result treeview to labelframe"""
        self.resultview = ttk.Treeview(
            master=self, bootstyle=INFO, columns=[0, 1, 2, 3, 4], show=HEADINGS
        )
        self.resultview.pack(fill=BOTH, expand=YES, pady=10)

        # setup columns and use `scale_size` to adjust for resolution
        self.resultview.heading(0, text="Id", anchor=W)
        self.resultview.heading(1, text="Producto", anchor=W)
        self.resultview.heading(2, text="Cantidad", anchor=W)
        self.resultview.heading(3, text="Categoría", anchor=W)
        self.resultview.heading(4, text="Editorial", anchor=W)
        self.resultview.column(column=0, anchor=W)
        self.resultview.column(column=1, anchor=W)
        self.resultview.column(column=2, anchor=W)
        self.resultview.column(column=3, anchor=W)
        self.resultview.column(column=4)

    def update_results_view(self, resultado):
        for item in self.resultview.get_children():
            self.resultview.delete(item)

        for a in resultado.values():
            iid = self.resultview.insert(
                parent="",
                index=END,
            )

            self.resultview.item(
                iid,
                open=True,
                values=[
                    a.getNumeroProducto(),
                    a.getNombreProducto(),
                    a.getCantidadProducto(),
                    a.getNombreCategoria(),
                    a.getNombreEditorial(),
                ],
            )

    def filter_results_view(self, resultado, filtro):
        for item in self.resultview.get_children():
            self.resultview.delete(item)
        for a in resultado.values():
            if a.getNombreEditorial() == filtro:
                iid = self.resultview.insert(
                    parent="",
                    index=END,
                )

                self.resultview.item(
                    iid,
                    open=True,
                    values=[
                        a.getNumeroProducto(),
                        a.getNombreProducto(),
                        a.getCantidadProducto(),
                        a.getNombreCategoria(),
                        a.getNombreEditorial(),
                    ],
                )

    def on_search(self):
        if self.filtro.get() == "":
            self.update_results_view(self.resultado)
        else:
            self.filter_results_view(self.resultado, self.filtro.get().capitalize())
            self.filtroEntry.delete(0, END)


class MenuBodeguero(tk.Toplevel):
    def __init__(self, parent, resu):
        super().__init__(parent, padx=20, pady=10)

        # form header
        hdr_txt = f"Bienvenido Sr/Sra {resu.getNombre().capitalize()} {resu.getApellido().capitalize()}"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # Contenedor menú row 1
        containerRow1 = ttk.Frame(self)
        containerRow1.pack(fill=X, expand=YES, pady=(15, 10))

        self.create_buttonbox(
            containerRow1, "Movimiento\nEntrada", self.movEntrada, "mov"
        )
        self.create_buttonbox(
            containerRow1, "Movimiento\nSalida", self.movSalida, "mov"
        )
        self.create_buttonbox(
            containerRow1, "Movimiento\nTraslado", self.movTraslado, "mov"
        )

        # Contenedor boton
        containerBtn = ttk.Frame(self)
        containerBtn.pack(fill=X, expand=YES, pady=(15, 10))

        self.create_buttonCancel(containerBtn, "Salir", self.on_cancel)

    def create_buttonbox(self, container, title, command, img):
        # Crear los botones
        button = tk.PhotoImage(file=f"img/{img}.png")
        # button = button.subsample(2, 2)
        menuBtn = ttk.Button(
            master=container,
            text=title,
            command=command,
            bootstyle=PRIMARY,
            padding=10,
            image=button,
            compound=LEFT,
        )
        menuBtn.image = button  # keep a reference!
        menuBtn.pack(side=LEFT, padx=15)

    def create_buttonCancel(self, container, title, command):
        cnl_btn = ttk.Button(
            master=container,
            text=title,
            command=command,
            bootstyle=DANGER,
            width=6,
        )
        cnl_btn.pack(side=LEFT, padx=15)

    def movEntrada(self):
        window = MovEntrada(self)
        place_window_center(window)
        window.grab_set()

    def movSalida(self):
        window = MovSalida(self)
        place_window_center(window)
        window.grab_set()

    def movTraslado(self):
        window = MovTraslado(self)
        place_window_center(window)
        window.grab_set()

    def on_cancel(self):
        """Cancel and close the application."""
        self.quit()


class MovEntrada(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, padx=20, pady=10)

        listaRegistro = []
        for a in listRegistro().values():
            listaRegistro.append(a.getId())

        listaTrabajador = []
        for a in listTrabajador().values():
            listaTrabajador.append(a.getRut())

        self.listaProducto = []
        for a in listProducto().values():
            self.listaProducto.append(a.getNombre())

        listaBodega = []
        for a in listBodega().values():
            listaBodega.append(a.getNumero())

        # form variables
        self.trabajador = ttk.StringVar(value="")
        self.bodega = ttk.StringVar(value="")
        self.proveedor = ttk.StringVar(value="")
        self.cantidad = ttk.StringVar(value="")
        self.producto = ttk.StringVar(value="")
        self.listaDetalle = []
        if len(listaRegistro) == 0:
            self.idRegistro = 1
        else:
            self.idRegistro = listaRegistro[-1] + 1

        # header and labelframe option container
        option_text = "Ingresa los Datos del Movimiento de Entrada"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)

        # form entries
        self.trabajadorEntry = self.create_form_entry_combo(
            "trabajador\nencargado (rut)",
            self.trabajador,
            validarStr,
            listaTrabajador,
            self.option_lf,
        )
        self.proveedorEntry = self.create_form_entry(
            "proveedor", self.proveedor, validarStr, self.option_lf
        )
        self.bodegaEntry = self.create_form_entry_combo(
            "nº bodega\ndestino", self.bodega, validarStr, listaBodega, self.option_lf
        )

        # header and labelframe option container
        option_text2 = "Ingresa los Productos"
        self.option_lf2 = ttk.Labelframe(self.option_lf, text=option_text2, padding=15)
        self.option_lf2.pack(fill=X, expand=YES, anchor=N, pady=10)

        self.productoEntry = self.create_form_entry_combo(
            "producto", self.producto, validarStr, self.listaProducto, self.option_lf2
        )
        self.cantidadEntry = self.create_form_entry(
            "cantidad", self.cantidad, validarInt, self.option_lf2
        )

        self.create_buttonbox(self.option_lf2, "+", self.on_add, (3))

        # header and labelframe option container
        hdr_txt = "Lista de Productos"
        hdr = ttk.Label(master=self.option_lf2, text=hdr_txt, width=50)
        hdr.pack(fill=X)

        self.create_buttonbox(self.option_lf, "Crear", self.on_submit, (15, 10))
        self.mensajeProducto = ""
        self.create_results_view()

    def create_form_entry(self, label, variable, val, parent):
        # Crear una entrada
        container = ttk.Frame(parent)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=15)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(
            master=container,
            textvariable=variable,
            validate="focus",
            validatecommand=(self.register(val), "%P"),
            width=100,
        )
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

        return ent

    def create_form_entry_combo(self, label, variable, val, list, parent):
        # Crear una entrada

        container = ttk.Frame(parent)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=15)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Combobox(
            master=container,
            textvariable=variable,
            validate="focus",
            validatecommand=(self.register(val), "%P"),
            values=list,
            state=READONLY,
        )
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

        return ent

    def create_buttonbox(self, parent, label, command, pad):
        # Crear los botones
        container = ttk.Frame(parent)
        container.pack(fill=X, expand=YES, pady=pad)

        sub_btn = ttk.Button(
            master=container,
            text=label,
            command=command,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)

    def create_results_view(self):
        """Add result treeview to labelframe"""
        self.resultview = ttk.Treeview(
            master=self.option_lf2, bootstyle=INFO, columns=[0, 1], show=HEADINGS
        )
        self.resultview.pack(fill=BOTH, expand=YES, pady=10)

        # setup columns and use `scale_size` to adjust for resolution
        self.resultview.heading(0, text="Producto", anchor=W)
        self.resultview.heading(1, text="Cantidad", anchor=W)
        self.resultview.column(column=0, anchor=W)
        self.resultview.column(column=1, anchor=W)

    def update_results_view(self):
        for item in self.resultview.get_children():
            self.resultview.delete(item)
        for a in self.listaDetalle:
            iid = self.resultview.insert(
                parent="",
                index=END,
            )

            self.resultview.item(
                iid,
                open=True,
                values=[
                    a["numeroProducto"],
                    a["cantidadProducto"],
                ],
            )

    def on_submit(self):
        # Valida las entradas y llama la función createEntrada()

        if (
            validarStr(self.proveedor.get())
            and validarStr(self.bodega.get())
            and validarStr(self.trabajador.get())
            and len(self.listaDetalle) != 0
        ):
            confirmar = pregunta(
                self,
                f"""Movimiento de Entrada\nId: {self.idRegistro}\nProveedor: {self.proveedor.get()}\nBodega destino: {self.bodega.get()}\nTrabajador encargado: {self.trabajador.get()}\nProductos: \n{self.mensajeProducto}¿Están bien éstos datos?""",
            )
            if confirmar == "Si":
                trabajador = findTrabajador(self.trabajador.get()).getId()
                bodega = findBodega(self.bodega.get()).getNumero()
                id = createEntrada(
                    self.idRegistro,
                    self.proveedor.get(),
                    bodega,
                    trabajador,
                )

                if id:
                    mensaje = createDetalle(self.listaDetalle, id)
            elif confirmar == "No" or confirmar is None:
                mensaje = "No se realizó el movimiento"
            submit(self, mensaje)
            self.destroy()

        else:
            datosValidos(self)

    def on_add(self):
        if validarStr(self.producto.get()) and validarInt(self.cantidad.get()):
            producto = findProductoNum(self.producto.get()).getNumero()
            self.listaDetalle.append(
                {"numeroProducto": producto, "cantidadProducto": self.cantidad.get()}
            )

            self.mensajeProducto += (
                f"Nombre: {self.producto.get()} - Cantidad: {self.cantidad.get()}\n"
            )

            self.cantidadEntry.delete(0, END)
            self.productoEntry.set("")

            submit(self, "Producto añadido correctamente")

            self.update_results_view()

        else:
            datosValidos(self)


class MovSalida(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, padx=20, pady=10)

        listaRegistro = []
        for a in listRegistro().values():
            listaRegistro.append(a.getId())

        listaTrabajador = []
        for a in listTrabajador().values():
            listaTrabajador.append(a.getRut())

        self.listaProducto = []
        for a in listProducto().values():
            self.listaProducto.append(a.getNombre())

        listaBodega = []
        for a in listBodega().values():
            listaBodega.append(a.getNumero())

        # form variables
        self.trabajador = ttk.StringVar(value="")
        self.bodega = ttk.StringVar(value="")
        self.tienda = ttk.StringVar(value="")
        self.cantidad = ttk.StringVar(value="")
        self.producto = ttk.StringVar(value="")
        self.listaDetalle = []
        if len(listaRegistro) == 0:
            self.idRegistro = 1
        else:
            self.idRegistro = listaRegistro[-1] + 1

        # header and labelframe option container
        option_text = "Ingresa los Datos del Movimiento de Salida"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)

        # form entries
        self.trabajadorEntry = self.create_form_entry_combo(
            "trabajador\nencargado (rut)",
            self.trabajador,
            validarStr,
            listaTrabajador,
            self.option_lf,
        )
        self.bodegaEntry = self.create_form_entry_combo(
            "nº bodega\norigen", self.bodega, validarStr, listaBodega, self.option_lf
        )
        self.tiendaEntry = self.create_form_entry(
            "tienda destino", self.tienda, validarStr, self.option_lf
        )

        # header and labelframe option container
        option_text2 = "Ingresa los Productos"
        self.option_lf2 = ttk.Labelframe(self.option_lf, text=option_text2, padding=15)
        self.option_lf2.pack(fill=X, expand=YES, anchor=N, pady=10)
        self.productoEntry = self.create_form_entry_combo(
            "producto", self.producto, validarStr, self.listaProducto, self.option_lf2
        )
        self.cantidadEntry = self.create_form_entry(
            "cantidad", self.cantidad, validarInt, self.option_lf2
        )

        self.create_buttonbox(self.option_lf2, "+", self.on_add, (3))

        # header and labelframe option container
        hdr_txt = "Lista de Productos"
        hdr = ttk.Label(master=self.option_lf2, text=hdr_txt, width=50)
        hdr.pack(fill=X)

        self.create_buttonbox(self.option_lf, "Crear", self.on_submit, (15, 10))
        self.mensajeProducto = ""
        self.create_results_view()

    def create_form_entry(self, label, variable, val, parent):
        # Crear una entrada
        container = ttk.Frame(parent)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=15)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(
            master=container,
            textvariable=variable,
            validate="focus",
            validatecommand=(self.register(val), "%P"),
            width=100,
        )
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

        return ent

    def create_form_entry_combo(self, label, variable, val, list, parent):
        # Crear una entrada

        container = ttk.Frame(parent)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=15)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Combobox(
            master=container,
            textvariable=variable,
            validate="focus",
            validatecommand=(self.register(val), "%P"),
            values=list,
            state=READONLY,
        )
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

        return ent

    def create_buttonbox(self, parent, label, command, pad):
        # Crear los botones
        container = ttk.Frame(parent)
        container.pack(fill=X, expand=YES, pady=pad)

        sub_btn = ttk.Button(
            master=container,
            text=label,
            command=command,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)

    def create_results_view(self):
        """Add result treeview to labelframe"""
        self.resultview = ttk.Treeview(
            master=self.option_lf2, bootstyle=INFO, columns=[0, 1], show=HEADINGS
        )
        self.resultview.pack(fill=BOTH, expand=YES, pady=10)

        # setup columns and use `scale_size` to adjust for resolution
        self.resultview.heading(0, text="Producto", anchor=W)
        self.resultview.heading(1, text="Cantidad", anchor=W)
        self.resultview.column(column=0, anchor=W)
        self.resultview.column(column=1, anchor=W)

    def update_results_view(self):
        for item in self.resultview.get_children():
            self.resultview.delete(item)
        for a in self.listaDetalle:
            iid = self.resultview.insert(
                parent="",
                index=END,
            )

            self.resultview.item(
                iid,
                open=True,
                values=[
                    a["numeroProducto"],
                    a["cantidadProducto"],
                ],
            )

    def on_submit(self):
        # Valida las entradas y llama la función createSalida()

        if (
            validarStr(self.tienda.get())
            and validarStr(self.bodega.get())
            and validarStr(self.trabajador.get())
            and len(self.listaDetalle) != 0
        ):
            confirmar = pregunta(
                self,
                f"""Movimiento de Salida\nId: {self.idRegistro}\nBodega Origen: {self.bodega.get()}\nTienda Destino: {self.tienda.get()}\nTrabajador encargado: {self.trabajador.get()}\nProductos: \n{self.mensajeProducto}¿Están bien éstos datos?""",
            )
            if confirmar == "Si":
                bodega = findBodega(self.bodega.get()).getNumero()
                trabajador = findTrabajador(self.trabajador.get()).getId()
                id = createSalida(
                    self.idRegistro,
                    self.tienda.get(),
                    bodega,
                    trabajador,
                )

                if id:
                    mensaje = createDetalle(self.listaDetalle, id)
            elif confirmar == "No" or confirmar is None:
                mensaje = "No se realizó el movimiento"
            submit(self, mensaje)
            self.destroy()

        else:
            datosValidos(self)

    def on_add(self):
        if validarStr(self.producto.get()) and validarInt(self.cantidad.get()):
            producto = findProductoNum(self.producto.get()).getNumero()
            self.listaDetalle.append(
                {"numeroProducto": producto, "cantidadProducto": self.cantidad.get()}
            )

            self.mensajeProducto += (
                f"Nombre: {self.producto.get()} - Cantidad: {self.cantidad.get()}\n"
            )

            self.cantidadEntry.delete(0, END)
            self.productoEntry.set("")

            submit(self, "Producto añadido correctamente")
            self.update_results_view()
        else:
            datosValidos(self)


class MovTraslado(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, padx=20, pady=10)

        listaRegistro = []
        for a in listRegistro().values():
            listaRegistro.append(a.getId())

        listaTrabajador = []
        for a in listTrabajador().values():
            listaTrabajador.append(a.getRut())

        self.listaProducto = []
        for a in listProducto().values():
            self.listaProducto.append(a.getNombre())

        listaBodega = []
        for a in listBodega().values():
            listaBodega.append(a.getNumero())

        # form variables
        self.trabajador = ttk.StringVar(value="")
        self.bodega = ttk.StringVar(value="")
        self.bodegaOrigen = ttk.StringVar(value="")
        self.cantidad = ttk.StringVar(value="")
        self.producto = ttk.StringVar(value="")
        self.listaDetalle = []
        if len(listaRegistro) == 0:
            self.idRegistro = 1
        else:
            self.idRegistro = listaRegistro[-1] + 1

        # header and labelframe option container
        option_text = "Ingresa los Datos del Movimiento de Traslado"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)

        # form entries
        self.trabajadorEntry = self.create_form_entry_combo(
            "trabajador\nencargado (rut)",
            self.trabajador,
            validarStr,
            listaTrabajador,
            self.option_lf,
        )
        self.bodegaOrigenEntry = self.create_form_entry(
            "nº bodega\norigen", self.bodegaOrigen, validarInt, self.option_lf
        )
        self.bodegaEntry = self.create_form_entry_combo(
            "nº bodega\ndestino", self.bodega, validarStr, listaBodega, self.option_lf
        )

        # header and labelframe option container
        option_text2 = "Ingresa los Productos"
        self.option_lf2 = ttk.Labelframe(self.option_lf, text=option_text2, padding=15)
        self.option_lf2.pack(fill=X, expand=YES, anchor=N, pady=10)
        self.productoEntry = self.create_form_entry_combo(
            "producto", self.producto, validarStr, self.listaProducto, self.option_lf2
        )
        self.cantidadEntry = self.create_form_entry(
            "cantidad", self.cantidad, validarInt, self.option_lf2
        )

        self.create_buttonbox(self.option_lf2, "+", self.on_add, (3))

        # header and labelframe option container
        hdr_txt = "Lista de Productos"
        hdr = ttk.Label(master=self.option_lf2, text=hdr_txt, width=50)
        hdr.pack(fill=X)

        self.create_buttonbox(self.option_lf, "Crear", self.on_submit, (15, 10))
        self.mensajeProducto = ""
        self.create_results_view()

    def create_form_entry(self, label, variable, val, parent):
        # Crear una entrada
        container = ttk.Frame(parent)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=15)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Entry(
            master=container,
            textvariable=variable,
            validate="focus",
            validatecommand=(self.register(val), "%P"),
            width=100,
        )
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

        return ent

    def create_form_entry_combo(self, label, variable, val, list, parent):
        # Crear una entrada

        container = ttk.Frame(parent)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label.title(), width=15)
        lbl.pack(side=LEFT, padx=5)

        ent = ttk.Combobox(
            master=container,
            textvariable=variable,
            validate="focus",
            validatecommand=(self.register(val), "%P"),
            values=list,
            state=READONLY,
        )
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

        return ent

    def create_buttonbox(self, parent, label, command, pad):
        # Crear los botones
        container = ttk.Frame(parent)
        container.pack(fill=X, expand=YES, pady=pad)

        sub_btn = ttk.Button(
            master=container,
            text=label,
            command=command,
            bootstyle=SUCCESS,
            width=6,
        )
        sub_btn.pack(side=RIGHT, padx=5)

    def create_results_view(self):
        """Add result treeview to labelframe"""
        self.resultview = ttk.Treeview(
            master=self.option_lf2, bootstyle=INFO, columns=[0, 1], show=HEADINGS
        )
        self.resultview.pack(fill=BOTH, expand=YES, pady=10)

        # setup columns and use `scale_size` to adjust for resolution
        self.resultview.heading(0, text="Producto", anchor=W)
        self.resultview.heading(1, text="Cantidad", anchor=W)
        self.resultview.column(column=0, anchor=W)
        self.resultview.column(column=1, anchor=W)

    def update_results_view(self):
        for item in self.resultview.get_children():
            self.resultview.delete(item)
        for a in self.listaDetalle:
            iid = self.resultview.insert(
                parent="",
                index=END,
            )

            self.resultview.item(
                iid,
                open=True,
                values=[
                    a["numeroProducto"],
                    a["cantidadProducto"],
                ],
            )

    def on_submit(self):
        # Valida las entradas y llama la función createSalida()

        if (
            validarStr(self.trabajador.get())
            and validarStr(self.bodega.get())
            and validarInt(self.bodegaOrigen.get())
            and len(self.listaDetalle) != 0
        ):
            confirmar = pregunta(
                self,
                f"""Movimiento de Traslado\nId: {self.idRegistro}\nBodega Origen: {self.bodegaOrigen.get()}\nBodega Destino: {self.bodega.get()}\nTrabajador encargado: {self.trabajador.get()}\nProductos: \n{self.mensajeProducto}¿Están bien éstos datos?""",
            )
            if confirmar == "Si":
                bodegaDestino = findBodega(self.bodega.get()).getNumero()
                bodegaOrigen = findBodega(self.bodegaOrigen.get())
                if bodegaOrigen is None:
                    mensaje = "Bodega no encontrada. Por favor, realizar otra vez el movimiento"
                elif bodegaOrigen.getNumero() == bodegaDestino:
                    mensaje = "Bodega de origen no puede ser igual a la bodega de destino.\nPor favor, realizar otra vez el movimiento"
                else:
                    bodegaOrigen = bodegaOrigen.getNumero()
                    trabajador = findTrabajador(self.trabajador.get()).getId()
                    id = createTraslado(
                        self.idRegistro,
                        bodegaOrigen,
                        bodegaDestino,
                        trabajador,
                    )

                    if id:
                        mensaje = createDetalle(self.listaDetalle, id)
            elif confirmar == "No" or confirmar is None:
                mensaje = "No se realizó el movimiento"
            submit(self, mensaje)
            self.destroy()

        else:
            datosValidos(self)

    def on_add(self):
        if validarStr(self.producto.get()) and validarInt(self.cantidad.get()):
            producto = findProductoNum(self.producto.get()).getNumero()
            self.listaDetalle.append(
                {"numeroProducto": producto, "cantidadProducto": self.cantidad.get()}
            )

            self.mensajeProducto += (
                f"Nombre: {self.producto.get()} - Cantidad: {self.cantidad.get()}\n"
            )

            self.cantidadEntry.delete(0, END)
            self.productoEntry.set("")

            submit(self, "Producto añadido correctamente")
            self.update_results_view()

        else:
            datosValidos(self)


if __name__ == "__main__":
    main()
