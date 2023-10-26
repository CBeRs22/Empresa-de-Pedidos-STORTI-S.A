import tkinter
from tkinter import ttk
import sqlite3

conexion = sqlite3.connect('Logistica.db')
datos = conexion.cursor()

# Crea la ventana.

ventana = tkinter.Tk()
ventana.title("Gestión de Pedidos") # Nombre de la ventana.
ventana.geometry('640x480') # Tamaño de la ventana.

# Crea las pestañas.

pestania = ttk.Notebook(ventana)
pestaclient = ttk.Frame(pestania, width = 640, height = 480)
pestaprodu = ttk.Frame(pestania, width = 640, height = 480)
pestapedido = ttk.Frame(pestania, width = 640, height = 480)
pestania.add(pestaclient, text = "Clientes")
pestania.add(pestaprodu, text = "Productos")
pestania.add(pestapedido, text = "Pedidos")
pestania.pack()

# Formulario para agregar clientes.

etiqueta2 = tkinter.Label(pestaclient, text = "Nombre:")
etiqueta2.grid(row = 0, column = 0)
entrada2 = tkinter.Entry(pestaclient)
entrada2.grid(row = 0, column = 1)
etiqueta3 = tkinter.Label(pestaclient, text = "Dirección:")
etiqueta3.grid(row = 1, column = 0)
entrada3 = tkinter.Entry(pestaclient)
entrada3.grid(row = 1, column =1 )
etiqueta4 = tkinter.Label(pestaclient, text = "Teléfono:")
etiqueta4.grid(row = 2, column = 0)
entrada4 = tkinter.Entry(pestaclient)
entrada4.grid(row = 2, column = 1)
etiqueta5 = tkinter.Label(pestaclient, text = "Email:")
etiqueta5.grid(row = 3, column = 0)
entrada5 = tkinter.Entry(pestaclient)
entrada5.grid(row = 3, column = 1)

def agregarclient():
    nombre = entrada2.get()
    direccion = entrada3.get()
    telefono = entrada4.get()
    email = entrada5.get()
    datos.execute("INSERT INTO Clientes (NOMBRE, DIRECCIÓN, TELEFONO, EMAIL) VALUES (?, ?, ?, ?)", (nombre, direccion, telefono, email))
    conexion.commit()
    entrada2.delete(0, tkinter.END)
    entrada3.delete(0, tkinter.END)
    entrada4.delete(0, tkinter.END)
    entrada5.delete(0, tkinter.END)

boton2 = tkinter.Button(pestaclient, text = "Agregar Cliente", command = agregarclient)
boton2.grid(row = 4, columnspan = 2)

# Formulario para agregar productos.

etiqueta6 = tkinter.Label(pestaprodu, text = "Nombre del Producto:")
etiqueta6.grid(row = 0, column = 0)
entrada6 = tkinter.Entry(pestaprodu)
entrada6.grid(row = 0, column = 1)
etiqueta7 = tkinter.Label(pestaprodu, text = "Descripción:")
etiqueta7.grid(row = 1, column = 0)
entrada7 = tkinter.Entry(pestaprodu)
entrada7.grid(row = 1, column = 1)
etiqueta8 = tkinter.Label(pestaprodu, text = "Precio Unitario:")
etiqueta8.grid(row = 2, column = 0)
entrada8 = tkinter.Entry(pestaprodu)
entrada8.grid(row = 2, column = 1)

def agregarprodu():
    nombre = entrada6.get()
    descripcion = entrada7.get()
    precio = entrada8.get()
    datos.execute("INSERT INTO Productos (NOMBRE, DESCRIPCION, PRECIOUNITARIO) VALUES (?, ?, ?)", (nombre, descripcion, precio))
    conexion.commit()
    entrada6.delete(0, tkinter.END)
    entrada7.delete(0, tkinter.END)
    entrada8.delete(0, tkinter.END)

boton3 = tkinter.Button(pestaprodu, text = "Agregar Producto", command = agregarprodu)
boton3.grid(row = 3, columnspan = 2)

# Formulario para buscar clientes.

etiqueta0 = tkinter.Label(pestapedido, text = "ID del Cliente:")
etiqueta0.grid(row = 0, column = 0)
entrada0 = tkinter.Entry(pestapedido)
entrada0.grid(row = 0, column = 1)
resultado0 = tkinter.Label(pestapedido, text = "")
resultado0.grid(row = 2, columnspan = 2)

def buscarclientes():
    infocli = entrada0.get()
    datos.execute("SELECT * FROM Clientes WHERE IDCliente = ? ", (infocli))
    cliente = datos.fetchone()   
    if cliente:
        resultado0.config(text = f"ID: {cliente[0]}\nNombre: {cliente[1]}\nDirección: {cliente[2]}\nTeléfono: {cliente[3]}\nEmail: {cliente[4]}\nFecha de Registro: {cliente[5]}\nNotas: {cliente[6]}")
    else:
        resultado0.config(text = "Cliente no encontrado.")

boton0 = tkinter.Button(pestapedido, text = "Buscar Cliente", command = buscarclientes)
boton0.grid(row = 1, columnspan = 2)

# Formulario para buscar productos.

etiqueta9 = tkinter.Label(pestapedido, text = "ID del Producto:")
etiqueta9.grid(row = 3, column = 0)
entrada9 = tkinter.Entry(pestapedido)
entrada9.grid(row = 3, column = 1)
etiqueta10 = tkinter.Label(pestapedido, text = "")
etiqueta10.grid(row = 5, columnspan = 2)

def buscarprodu():
    infoprodu = entrada9.get()
    datos.execute("SELECT * FROM Productos WHERE IDProducto = ? ",(infoprodu))
    producto = datos.fetchone()
    if producto:
        etiqueta10.config(text = f"ID: {producto[0]}\nNombre: {producto[1]}\nDescripción: {producto[2]}\nPrecio Unitario: {producto[3]}\nStock Inicial: {producto[4]}\nStock Mínimo: {producto[5]}\nFecha de Creación: {producto[6]}")
    else:
        etiqueta10.config(text = "Producto no encontrado.")

boton4 = tkinter.Button(pestapedido, text = "Buscar Producto", command = buscarprodu)
boton4.grid(row = 4, columnspan = 2)

# Formulario para crear un nuevo pedido

etiqueta11 = tkinter.Label(pestapedido, text = "ID del Cliente:")
etiqueta11.grid(row = 6, column = 0)
entrada10 = tkinter.Entry(pestapedido)
entrada10.grid(row= 6 , column = 1)
etiqueta12 = tkinter.Label(pestapedido, text = "ID del Vendedor:")
etiqueta12.grid(row = 7, column = 0)
entrada11 = tkinter.Entry(pestapedido)
entrada11.grid(row = 7, column = 1)
etiqueta13 = tkinter.Label(pestapedido, text = "ID de la Zona:")
etiqueta13.grid(row = 8, column = 0)
entrada12 = tkinter.Entry(pestapedido)
entrada12.grid(row = 8, column = 1)
etiqueta14 = tkinter.Label(pestapedido, text = "Estado del Pedido:")
etiqueta14.grid(row = 9, column = 0)
entrada13 = tkinter.Entry(pestapedido)
entrada13.grid(row = 9, column = 1)
etiqueta15 = tkinter.Label(pestapedido, text = "Notas:")
etiqueta15.grid(row = 10, column = 0)
entrada14 = tkinter.Entry(pestapedido)
entrada14.grid(row = 10, column = 1)

def crearpedido():
    infocli = entrada10.get()
    infovend = entrada11.get()
    infozona = entrada12.get()
    infopedi = entrada13.get()
    notas = entrada14.get()
    datos.execute("INSERT INTO Pedidos (FECHAS, IDCliente, IDVendedor, IDZona, ESTADOPEDIDO, NOTAS) VALUES (datetime('now'), ?, ?, ?, ?, ?)", (infocli, infovend, infozona, infopedi, notas))
    conexion.commit()
    entrada10.delete(0, tkinter.END)
    entrada11.delete(0, tkinter.END)
    entrada12.delete(0, tkinter.END)
    entrada13.delete(0, tkinter.END)
    entrada14.delete(0, tkinter.END)

boton5 = tkinter.Button(pestapedido, text = "Crear Pedido", command = crearpedido)
boton5.grid(row = 11, columnspan = 2)

# Función para cerrar la conexión con la base de datos y salir de la ventana.

def salir():
    conexion.close()
    ventana.destroy()

boton1 = tkinter.Button(ventana, text = "Salir", command = salir)
boton1.pack()

ventana.mainloop()
