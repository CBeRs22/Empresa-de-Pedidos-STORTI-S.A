import tkinter as tk
from tkinter import messagebox

credenciales = {"usuario": "contrasena"}

def verificar_credenciales():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if usuario in credenciales and credenciales[usuario] == contrasena:
        ventana_inicio.destroy()
        iniciar_aplicacion()
    else:
        messagebox.showerror("Error de inicio de sesión", "Credenciales incorrectas")

def iniciar_aplicacion():
    app = tk.Tk()

ventana_inicio = tk.Tk()
ventana_inicio.title("Inicio de Sesión")

label_usuario = tk.Label(ventana_inicio, text="Usuario:")
entry_usuario = tk.Entry(ventana_inicio)
label_contrasena = tk.Label(ventana_inicio, text="Contraseña:")
entry_contrasena = tk.Entry(ventana_inicio, show="*")

btn_iniciar_sesion = tk.Button(ventana_inicio, text="Iniciar Sesión", command=verificar_credenciales)

label_usuario.pack()
entry_usuario.pack()
label_contrasena.pack()
entry_contrasena.pack()
btn_iniciar_sesion.pack()

ventana_inicio.mainloop()
