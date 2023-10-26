import tkinter
from tkinter import messagebox
from tkinter import ttk

credenciales = {"ProfeStorti": "isft232"}
 
# Crea la ventana.

ventana = tkinter.Tk()
ventana.title("Inicio de Sesión")
ventana.geometry('440x280')

# Formulario para iniciar sesión.

etiqueta1 = tkinter.Label(ventana, text = "Usuario:")
entrada1 = tkinter.Entry(ventana)
etiqueta2 = tkinter.Label(ventana, text = "Contraseña:")
entrada2 = tkinter.Entry(ventana, show = "*")
check1 = ttk.Checkbutton(ventana, text = "Recordarme")

def verificacion():
    usuario = entrada1.get()
    contrasena = entrada2.get()
    if credenciales.get(usuario) == contrasena:
        ventana.destroy()
        exec(open("Logistica.py").read())
    else:
        messagebox.showerror("Error de inicio de sesión", "Credenciales incorrectas")

boton1 = tkinter.Button(ventana, text = "Iniciar Sesión", command = verificacion)

etiqueta1.pack()
entrada1.pack()
etiqueta2.pack()
entrada2.pack()
boton1.pack()
check1.pack()

ventana.mainloop()
