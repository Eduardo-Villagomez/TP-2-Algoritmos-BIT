import tkinter as tk
import csv
from tp2_P1 import crear_usuario, crear_clave, registro, comparar_inicio_sesion, recuperar_clave
from tp_P1 import cifrado_cesar, descifrado_cesar
from tp_P2 import cifrado_atbash

ventana_actual = None
intentos_recuperacion = {}

def cerrar_ventana_actual():
    global ventana_actual
    if ventana_actual:
        ventana_actual.withdraw()
        ventana_actual.destroy()  

def ventana_bienvenida():
    global ventana_actual
    cerrar_ventana_actual()
    ventana_actual = tk.Tk()
    ventana_actual.resizable(0, 0)
    ventana_actual.title("TP Grupal Parte 1 - Grupo: BIT")
    ventana_actual.iconbitmap('icono.ico')
    ventana_actual.config(bg="light sky blue")

    mensaje_bienvenida = tk.Label(ventana_actual, text="Bienvenido a la aplicación de mensajes \nsecretos del grupo BIT. Para continuar,\n presione Continuar, de lo contrario \ncierre la ventana" ,font=("Comic sans MS",14))
    mensaje_bienvenida.config(bg="light sky blue")
    mensaje_bienvenida.pack()

    integrantes_grupo = ['Eduardo Villagomez', 'Francisco Albinati', 'Cindy Calderón', 'Francisca Gaillard']

    lista_integrantes = tk.Label(ventana_actual, text="Construída por:")
    lista_integrantes.config(bg="light sky blue")
    lista_integrantes.pack()

    for integrante in integrantes_grupo:
        label_integrante = tk.Label(ventana_actual, text=integrante)
        label_integrante.config(bg="light sky blue")
        label_integrante.pack()

    boton_crear_usuario = tk.Button(ventana_actual, text="Crear Usuario", command=ventana_crear_usuario)
    boton_crear_usuario.config(bg="deep sky blue")
    boton_crear_usuario.pack(padx=10,pady=15)

    boton_ingreso_usuario = tk.Button(ventana_actual, text="Ingreso Usuario", command=ventana_iniciar_sesion)
    boton_ingreso_usuario.config(bg="deep sky blue")
    boton_ingreso_usuario.pack(padx=10,pady=15)

    ventana_actual.mainloop()

def ventana_iniciar_sesion():
    global ventana_actual
    cerrar_ventana_actual()
    def iniciar_sesion():
        usuario = entrada_usuario.get()
        clave = entrada_clave.get()
        usuario_comparado = comparar_inicio_sesion(usuario,clave)
        label_resultado.config(text=usuario_comparado)

    ventana_actual = tk.Tk()
    ventana_actual.geometry("400x400")
    ventana_actual.title("Identificación para acceso")
    ventana_actual.config(bg="navajo white")

    label_usuario = tk.Label(ventana_actual, text="Usuario:")
    label_usuario.config(bg="navajo white")
    label_usuario.pack()
    entrada_usuario = tk.Entry(ventana_actual)
    entrada_usuario.pack()

    label_clave = tk.Label(ventana_actual, text="Clave:")
    label_clave.config(bg="navajo white")
    label_clave.pack()
    entrada_clave = tk.Entry(ventana_actual)
    entrada_clave.pack()

    boton_iniciar_sesion = tk.Button(ventana_actual, text="Iniciar Sesion", command=iniciar_sesion)
    boton_iniciar_sesion.config(bg="orange")
    boton_iniciar_sesion.pack(padx=5,pady=10)
    
    boton_recuperar_clave = tk.Button(ventana_actual, text="Recuperar Clave", command=ventana_recuperar_clave)
    boton_recuperar_clave.config(bg="orange")
    boton_recuperar_clave.pack(padx=5,pady=10)

    label_resultado = tk.Label(ventana_actual, text="")
    label_resultado.config(bg="navajo white")
    label_resultado.pack()

def ventana_recuperar_clave(usuario):
    var_usuario=usuario.get()
    ventana_actual = tk.Tk()
    ventana_actual.geometry("300x300")
    ventana_actual.title("Recuperación Clave")
    ventana_actual.config(bg="navajo white")

    label_pregunta = tk.Label(ventana_actual, text=f"Pregunta: {var_usuario}")
    label_pregunta.config(bg="navajo white")
    label_pregunta.pack()

    label_respuesta = tk.Label(ventana_actual, text="Ingrese la respuesta:")
    label_respuesta.config(bg="navajo white")
    label_respuesta.pack()

    entrada_respuesta = tk.Entry(ventana_actual)
    entrada_respuesta.pack()

    boton_verificar_respuesta = tk.Button(ventana_actual, text="Verificar Respuesta")
    boton_verificar_respuesta.config(bg="orange")
    boton_verificar_respuesta.pack(padx=5, pady=10)

    label_resultado = tk.Label(ventana_actual, text="")
    label_resultado.config(bg="navajo white")
    label_resultado.pack()

def ventana_crear_usuario():
    global ventana_actual
    cerrar_ventana_actual()
    def registrarse():
        usuario = entrada_usuario.get()
        clave = entrada_clave.get()
        respuesta = entrada_respuesta.get()
        pregunta = var.get()
        if not pregunta or pregunta == 'Elija una Opción':
            label_resultado.config(text="¡Por favor, elija una pregunta!")
            return
        indice = int(pregunta.split('.')[0])
        registro_creado = registro(usuario,clave, respuesta, pregunta)
        label_resultado.config(text=registro_creado)

    preguntas = []
    with open('preguntas.csv', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            preguntas.append(fila[1])

    ventana_actual = tk.Tk()
    ventana_actual.geometry("300x300")
    ventana_actual.title("Register")
    ventana_actual.config(bg="navajo white")
    
    label_usuario = tk.Label(ventana_actual, text="Ingrese su nombre de usuario:")
    label_usuario.config(bg="navajo white")
    label_usuario.pack()
    entrada_usuario = tk.Entry(ventana_actual)
    entrada_usuario.pack()
    
    label_clave = tk.Label(ventana_actual, text="Ingrese una clave")
    label_clave.config(bg="navajo white")
    label_clave.pack()
    entrada_clave = tk.Entry(ventana_actual)
    entrada_clave.pack()

    label_pregunta = tk.Label(ventana_actual, text="Elija una pregunta de respaldo")
    label_pregunta.config(bg="navajo white")
    label_pregunta.pack()
    var = tk.StringVar(ventana_actual)
    var.set('Elija una Opción')
    opcion = tk.OptionMenu(ventana_actual,var,*['{}. {}'.format(i + 1, pregunta) for i, pregunta in enumerate(preguntas)]    )
    opcion.config(bg="navajo white")
    opcion.pack()
    label_pregunta = tk.Label(ventana_actual, text="Respuesta")
    label_pregunta.config(bg="navajo white")
    label_pregunta.pack()
    entrada_respuesta = tk.Entry(ventana_actual)
    entrada_respuesta.pack()

    boton_crear_usuario = tk.Button(ventana_actual, text="Regitrarse", command=registrarse)
    boton_crear_usuario.config(bg="orange")
    boton_crear_usuario.pack(padx=5,pady=10)

    label_resultado = tk.Label(ventana_actual, text="")
    label_resultado.config(bg="navajo white")
    label_resultado.pack()
    
def ventana_mensajes():
    global ventana_actual
    cerrar_ventana_actual()
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

    ventana_actual = tk.Tk()
    ventana_actual.resizable(0, 0)
    ventana_actual.title("TP Grupal Parte 1 - Grupo: BIT")
    ventana_actual.config(bg="navajo white")

    label_mensaje = tk.Label(ventana_actual, text="Ingrese el mensaje:")
    label_mensaje.config(bg="navajo white")
    label_mensaje.pack()

    entrada_mensaje = tk.Entry(ventana_actual)
    entrada_mensaje.pack()

    label_clave = tk.Label(ventana_actual, text="Ingrese la clave (solo para Cifrado César):")
    label_clave.config(bg="navajo white")
    label_clave.pack()

    entrada_clave = tk.Entry(ventana_actual)
    entrada_clave.pack()

    boton_cifrar_cesar = tk.Button(ventana_actual, text="Cifrar mensaje César", command=cifrar_cesar)
    boton_cifrar_cesar.config(bg="orange")
    boton_cifrar_cesar.pack(padx=5,pady=10)

    boton_cifrar_atbash = tk.Button(ventana_actual, text="Cifrar mensaje Atbash", command=cifrar_atbash)
    boton_cifrar_atbash.config(bg="orange")
    boton_cifrar_atbash.pack(padx=5,pady=5)

    boton_descifrar_cesar = tk.Button(ventana_actual, text="Descifrar mensaje César", command=decifrar_cesar)
    boton_descifrar_cesar.config(bg="orange")
    boton_descifrar_cesar.pack(padx=5,pady=10)

    boton_descifrar_atbash = tk.Button(ventana_actual, text="Descifrar mensaje Atbash", command=cifrar_atbash)
    boton_descifrar_atbash.config(bg="orange")
    boton_descifrar_atbash.pack(padx=5,pady=10)

    label_resultado = tk.Label(ventana_actual, text="")
    label_resultado.config(bg="navajo white")
    label_resultado.pack()

    ventana_mensajes.mainloop()

ventana_bienvenida()