import tkinter as tk
from tkinter import ttk
import sqlite3

iniciar_aplicacion()

# Conectar a la base de datos
conn = sqlite3.connect('Logistica.db')
cursor = conn.cursor()

# Crear una ventana
app = tk.Tk()
app.title("Gestión de Pedidos")
app.geometry('540x380')

# Crear pestañas
notebook = ttk.Notebook(app)
tab_clientes = ttk.Frame(notebook)
tab_productos = ttk.Frame(notebook)
tab_pedidos = ttk.Frame(notebook)
notebook.add(tab_clientes, text="Clientes")
notebook.add(tab_productos, text="Productos")
notebook.add(tab_pedidos, text="Pedidos")
notebook.pack()

# Función para buscar un cliente por ID y mostrar su información
def buscar_cliente():
    id_cliente = entry_id_cliente.get()
    cursor.execute("SELECT * FROM Clientes WHERE IDCliente=?", (id_cliente,))
    cliente = cursor.fetchone()
    if cliente:
        resultado_cliente.config(text=f"ID: {cliente[0]}\nNombre: {cliente[1]}\nDirección: {cliente[2]}\nTeléfono: {cliente[3]}\nEmail: {cliente[4]}\nFecha de Registro: {cliente[5]}\nNotas: {cliente[6]}")
    else:
        resultado_cliente.config(text="Cliente no encontrado.")

# Función para buscar un producto por ID y mostrar su información
def buscar_producto():
    id_producto = entry_id_producto.get()
    cursor.execute("SELECT * FROM Productos WHERE IDProducto=?", (id_producto,))
    producto = cursor.fetchone()
    if producto:
        resultado_producto.config(text=f"ID: {producto[0]}\nNombre: {producto[1]}\nDescripción: {producto[2]}\nPrecio Unitario: {producto[3]}\nStock Inicial: {producto[4]}\nStock Mínimo: {producto[5]}\nFecha de Creación: {producto[6]}")
    else:
        resultado_producto.config(text="Producto no encontrado.")

# Función para crear un nuevo pedido
def crear_pedido():
    id_cliente = entry_id_cliente_pedido.get()
    id_vendedor = entry_id_vendedor_pedido.get()
    id_zona = entry_id_zona_pedido.get()
    estado_pedido = entry_estado_pedido.get()
    notas = entry_notas_pedido.get()
    cursor.execute("INSERT INTO Pedidos (FechaPedido, IDCliente, IDVendedor, IDZona, EstadoPedido, Notas) VALUES (datetime('now'), ?, ?, ?, ?, ?)", (id_cliente, id_vendedor, id_zona, estado_pedido, notas))
    conn.commit()
    entry_id_cliente_pedido.delete(0, tk.END)
    entry_id_vendedor_pedido.delete(0, tk.END)
    entry_id_zona_pedido.delete(0, tk.END)
    entry_estado_pedido.delete(0, tk.END)
    entry_notas_pedido.delete(0, tk.END)

# Crear pestaña de Pedidos
tab_pedidos = ttk.Frame(notebook)
notebook.add(tab_pedidos, text="Pedidos")

# Formulario para buscar clientes
label_id_cliente = tk.Label(tab_pedidos, text="ID del Cliente:")
entry_id_cliente = tk.Entry(tab_pedidos)
btn_buscar_cliente = tk.Button(tab_pedidos, text="Buscar Cliente", command=buscar_cliente)
resultado_cliente = tk.Label(tab_pedidos, text="")
label_id_cliente.grid(row=0, column=0)
entry_id_cliente.grid(row=0, column=1)
btn_buscar_cliente.grid(row=1, columnspan=2)
resultado_cliente.grid(row=2, columnspan=2)

# Formulario para buscar productos
label_id_producto = tk.Label(tab_pedidos, text="ID del Producto:")
entry_id_producto = tk.Entry(tab_pedidos)
btn_buscar_producto = tk.Button(tab_pedidos, text="Buscar Producto", command=buscar_producto)
resultado_producto = tk.Label(tab_pedidos, text="")
label_id_producto.grid(row=3, column=0)
entry_id_producto.grid(row=3, column=1)
btn_buscar_producto.grid(row=4, columnspan=2)
resultado_producto.grid(row=5, columnspan=2)

# Formulario para crear un nuevo pedido
label_id_cliente_pedido = tk.Label(tab_pedidos, text="ID del Cliente:")
entry_id_cliente_pedido = tk.Entry(tab_pedidos)
label_id_vendedor_pedido = tk.Label(tab_pedidos, text="ID del Vendedor:")
entry_id_vendedor_pedido = tk.Entry(tab_pedidos)
label_id_zona_pedido = tk.Label(tab_pedidos, text="ID de la Zona:")
entry_id_zona_pedido = tk.Entry(tab_pedidos)
label_estado_pedido = tk.Label(tab_pedidos, text="Estado del Pedido:")
entry_estado_pedido = tk.Entry(tab_pedidos)
label_notas_pedido = tk.Label(tab_pedidos, text="Notas:")
entry_notas_pedido = tk.Entry(tab_pedidos)
btn_crear_pedido = tk.Button(tab_pedidos, text="Crear Pedido", command=crear_pedido)
label_id_cliente_pedido.grid(row=6, column=0)
entry_id_cliente_pedido.grid(row=6, column=1)
label_id_vendedor_pedido.grid(row=7, column=0)
entry_id_vendedor_pedido.grid(row=7, column=1)
label_id_zona_pedido.grid(row=8, column=0)
entry_id_zona_pedido.grid(row=8, column=1)
label_estado_pedido.grid(row=9, column=0)
entry_estado_pedido.grid(row=9, column=1)
label_notas_pedido.grid(row=10, column=0)
entry_notas_pedido.grid(row=10, column=1)
btn_crear_pedido.grid(row=11, columnspan=2)


# Función para agregar un cliente a la base de datos
def agregar_cliente():
    nombre = entry_nombre.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    email = entry_email.get()
    cursor.execute("INSERT INTO Clientes (NombreCliente, DireccionCliente, TelefonoCliente, EmailCliente) VALUES (?, ?, ?, ?)", (nombre, direccion, telefono, email))
    conn.commit()
    entry_nombre.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Crear formulario para agregar clientes
label_nombre = tk.Label(tab_clientes, text="Nombre:")
entry_nombre = tk.Entry(tab_clientes)
label_direccion = tk.Label(tab_clientes, text="Dirección:")
entry_direccion = tk.Entry(tab_clientes)
label_telefono = tk.Label(tab_clientes, text="Teléfono:")
entry_telefono = tk.Entry(tab_clientes)
label_email = tk.Label(tab_clientes, text="Email:")
entry_email = tk.Entry(tab_clientes)
btn_agregar_cliente = tk.Button(tab_clientes, text="Agregar Cliente", command=agregar_cliente)

label_nombre.grid(row=0, column=0)
entry_nombre.grid(row=0, column=1)
label_direccion.grid(row=1, column=0)
entry_direccion.grid(row=1, column=1)
label_telefono.grid(row=2, column=0)
entry_telefono.grid(row=2, column=1)
label_email.grid(row=3, column=0)
entry_email.grid(row=3, column=1)
btn_agregar_cliente.grid(row=4, columnspan=2)

# Función para agregar un producto a la base de datos
def agregar_producto():
    nombre = entry_nombre_producto.get()
    descripcion = entry_descripcion.get()
    precio = entry_precio.get()
    cursor.execute("INSERT INTO Productos (NombreProducto, Descripcion, PrecioUnitario) VALUES (?, ?, ?)", (nombre, descripcion, precio))
    conn.commit()
    entry_nombre_producto.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)
    entry_precio.delete(0, tk.END)

# Crear formulario para agregar productos
label_nombre_producto = tk.Label(tab_productos, text="Nombre del Producto:")
entry_nombre_producto = tk.Entry(tab_productos)
label_descripcion = tk.Label(tab_productos, text="Descripción:")
entry_descripcion = tk.Entry(tab_productos)
label_precio = tk.Label(tab_productos, text="Precio Unitario:")
entry_precio = tk.Entry(tab_productos)
btn_agregar_producto = tk.Button(tab_productos, text="Agregar Producto", command=agregar_producto)

label_nombre_producto.grid(row=0, column=0)
entry_nombre_producto.grid(row=0, column=1)
label_descripcion.grid(row=1, column=0)
entry_descripcion.grid(row=1, column=1)
label_precio.grid(row=2, column=0)
entry_precio.grid(row=2, column=1)
btn_agregar_producto.grid(row=3, columnspan=2)

# Función para cerrar la conexión con la base de datos y salir
def salir():
    conn.close()
    app.destroy()

btn_salir = tk.Button(app, text="Salir", command=salir)
btn_salir.pack()

app.mainloop()
