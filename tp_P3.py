import tkinter as tk
import csv
from tp2_P1 import crear_usuario, crear_clave, registro
from tp_P1 import cifrado_cesar, descifrado_cesar
from tp_P2 import cifrado_atbash

def ventana_bienvenida():
    ventana_bienvenida = tk.Tk()
    ventana_bienvenida.resizable(0, 0)
    ventana_bienvenida.title("TP Grupal Parte 1 - Grupo: BIT")
    ventana_bienvenida.iconbitmap('icono.ico')
    ventana_bienvenida.config(bg="light sky blue")

    mensaje_bienvenida = tk.Label(ventana_bienvenida, text="Bienvenido a la aplicación de mensajes \nsecretos del grupo BIT. Para continuar,\n presione Continuar, de lo contrario \ncierre la ventana" ,font=("Comic sans MS",14))
    mensaje_bienvenida.config(bg="light sky blue")
    mensaje_bienvenida.pack()

    integrantes_grupo = ['Eduardo Villagomez', 'Francisco Albinati', 'Cindy Calderón', 'Francisca Gaillard']

    lista_integrantes = tk.Label(ventana_bienvenida, text="Construída por:")
    lista_integrantes.config(bg="light sky blue")
    lista_integrantes.pack()

    for integrante in integrantes_grupo:
        label_integrante = tk.Label(ventana_bienvenida, text=integrante)
        label_integrante.config(bg="light sky blue")
        label_integrante.pack()

    boton_crear_usuario = tk.Button(ventana_bienvenida, text="Crear Usuario", command=ventana_crear_usuario)
    boton_crear_usuario.config(bg="deep sky blue")
    boton_crear_usuario.pack(padx=10,pady=15)

    boton_ingreso_usuario = tk.Button(ventana_bienvenida, text="Ingreso Usuario", command=ventana_iniciar_sesion)
    boton_ingreso_usuario.config(bg="deep sky blue")
    boton_ingreso_usuario.pack(padx=10,pady=15)

    ventana_bienvenida.mainloop()

def ventana_iniciar_sesion():
    valores = []
    with open('registro.csv', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            valores.extend(fila[:2])
    print(valores)
    ventana_iniciar_sesion = tk.Tk()
    ventana_iniciar_sesion.geometry("300x300")
    ventana_iniciar_sesion.title("Iniciar Sesion")
    ventana_iniciar_sesion.config(bg="navajo white")

def ventana_crear_usuario():
    def registrarse():
        usuario = entrada_usuario.get()
        clave = entrada_clave.get()
        respuesta = entrada_respuesta.get()
        pregunta = var.get()
        registro_creado = registro(usuario,clave, respuesta, pregunta)
        label_resultado.config(text=registro_creado)

    preguntas = []
    with open('preguntas.csv', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            preguntas.append(fila[1])

    ventana_crear_usuario = tk.Tk()
    ventana_crear_usuario.geometry("300x300")
    ventana_crear_usuario.title("Register")
    ventana_crear_usuario.config(bg="navajo white")
    
    label_usuario = tk.Label(ventana_crear_usuario, text="Ingrese su nombre de usuario:")
    label_usuario.config(bg="navajo white")
    label_usuario.pack()
    entrada_usuario = tk.Entry(ventana_crear_usuario)
    entrada_usuario.pack()
    
    label_clave = tk.Label(ventana_crear_usuario, text="Ingrese una clave")
    label_clave.config(bg="navajo white")
    label_clave.pack()
    entrada_clave = tk.Entry(ventana_crear_usuario)
    entrada_clave.pack()

    label_pregunta = tk.Label(ventana_crear_usuario, text="Elija una pregunta de respaldo")
    label_pregunta.config(bg="navajo white")
    label_pregunta.pack()
    var = tk.StringVar(ventana_crear_usuario)
    var.set('Elija una Opción')
    opcion = tk.OptionMenu(ventana_crear_usuario,var,*preguntas)
    opcion.config(bg="navajo white")
    opcion.pack()
    label_pregunta = tk.Label(ventana_crear_usuario, text="Respuesta")
    label_pregunta.config(bg="navajo white")
    label_pregunta.pack()
    entrada_respuesta = tk.Entry(ventana_crear_usuario)
    entrada_respuesta.pack()

    boton_crear_usuario = tk.Button(ventana_crear_usuario, text="Regitrarse", command=registrarse)
    boton_crear_usuario.config(bg="orange")
    boton_crear_usuario.pack(padx=5,pady=10)

    label_resultado = tk.Label(ventana_crear_usuario, text="")
    label_resultado.config(bg="navajo white")
    label_resultado.pack()
    
def ventana_mensajes():
    def decifrar_cesar():
        mensaje = entrada_mensaje.get()
        clave = int(entrada_clave.get())
        mensaje_cifrado = descifrado_cesar(mensaje, clave)
        label_resultado.config(text=mensaje_cifrado)

    def cifrar_cesar():
        mensaje = entrada_mensaje.get()
        clave = int(entrada_clave.get())
        mensaje_cifrado = cifrado_cesar(mensaje, clave)
        label_resultado.config(text=mensaje_cifrado)

    def cifrar_atbash():
        mensaje = entrada_mensaje.get()
        mensaje_cifrado = cifrado_atbash(mensaje)
        label_resultado.config(text=mensaje_cifrado)

    ventana_mensajes = tk.Tk()
    ventana_mensajes.resizable(0, 0)
    ventana_mensajes.title("TP Grupal Parte 1 - Grupo: BIT")
    ventana_mensajes.config(bg="navajo white")

    label_mensaje = tk.Label(ventana_mensajes, text="Ingrese el mensaje:")
    label_mensaje.config(bg="navajo white")
    label_mensaje.pack()

    entrada_mensaje = tk.Entry(ventana_mensajes)
    entrada_mensaje.pack()

    label_clave = tk.Label(ventana_mensajes, text="Ingrese la clave (solo para Cifrado César):")
    label_clave.config(bg="navajo white")
    label_clave.pack()

    entrada_clave = tk.Entry(ventana_mensajes)
    entrada_clave.pack()

    boton_cifrar_cesar = tk.Button(ventana_mensajes, text="Cifrar mensaje César", command=cifrar_cesar)
    boton_cifrar_cesar.config(bg="orange")
    boton_cifrar_cesar.pack(padx=5,pady=10)

    boton_cifrar_atbash = tk.Button(ventana_mensajes, text="Cifrar mensaje Atbash", command=cifrar_atbash)
    boton_cifrar_atbash.config(bg="orange")
    boton_cifrar_atbash.pack(padx=5,pady=5)

    boton_descifrar_cesar = tk.Button(ventana_mensajes, text="Descifrar mensaje César", command=decifrar_cesar)
    boton_descifrar_cesar.config(bg="orange")
    boton_descifrar_cesar.pack(padx=5,pady=10)

    boton_descifrar_atbash = tk.Button(ventana_mensajes, text="Descifrar mensaje Atbash", command=cifrar_atbash)
    boton_descifrar_atbash.config(bg="orange")
    boton_descifrar_atbash.pack(padx=5,pady=10)

    label_resultado = tk.Label(ventana_mensajes, text="")
    label_resultado.config(bg="navajo white")
    label_resultado.pack()

    ventana_mensajes.mainloop()

ventana_bienvenida()