import tkinter as tk
import csv
from tp2_P1 import crear_usuario, crear_clave, registro, obtener_clave_byrespuesta, comparar_inicio_sesion, recuperar_clave, usuario_global, obtener_usuario,obtener_pregunta_byid
from tp2_P2 import leer,leer_usuario,verificar_usuario,elegir_receptor
from tp2_P3 import leer,usuarios_registrados,armar_diccionario
from tkinter import messagebox
from tp_P1 import cifrado_cesar, descifrado_cesar
from tp_P2 import cifrado_atbash

ventana_actual = None
intentos_recuperacion = {}
datos_mensajes = []
destinatario = []
lectura_msj = {}

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
    ventana_actual.iconbitmap('mensaje.ico')
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

    def ventana_recuperar_clave():
        def verificar_respuesta():
            respuesta = entrada_respuesta.get()
            clave_encontrada = obtener_clave_byrespuesta(respuesta_login=respuesta)
            label_pregunta.config(text=clave_encontrada)
        usuario = entrada_usuario.get()
        clave = entrada_clave.get()
        obtener_usuario(usuario_login=usuario,clave_login=clave)
        
        if usuario_global['estado_login'] != 'recuperar':
            return
        
        pregunta_id = usuario_global["id_pregunta"]
        pregunta_encontrada = obtener_pregunta_byid(pregunta_id)

        ventana_actual = tk.Tk()
        ventana_actual.geometry("300x300")
        ventana_actual.title("Recuperación Clave")
        ventana_actual.config(bg="navajo white")

        label_pregunta = tk.Label(ventana_actual, text=f"Pregunta: {pregunta_encontrada}")
        label_pregunta.config(bg="navajo white")
        label_pregunta.pack()

        label_respuesta = tk.Label(ventana_actual, text="Ingrese la respuesta:")
        label_respuesta.config(bg="navajo white")
        label_respuesta.pack()
        entrada_respuesta = tk.Entry(ventana_actual)
        entrada_respuesta.pack()

        boton_verificar_respuesta = tk.Button(ventana_actual, text="Verificar Respuesta", command=verificar_respuesta)
        boton_verificar_respuesta.config(bg="orange")
        boton_verificar_respuesta.pack(padx=5, pady=10)

        label_pregunta = tk.Label(ventana_actual, text=f"Contraseña: ")
        label_pregunta.config(bg="navajo white")
        label_pregunta.pack()

        label_resultado = tk.Label(ventana_actual, text="")
        label_resultado.config(bg="navajo white")
        label_resultado.pack()

    def iniciar_sesion():
        usuario = entrada_usuario.get()
        clave = entrada_clave.get()
        usuario_comparado = comparar_inicio_sesion(usuario,clave)
        if "Inicio de sesión exitoso" == comparar_inicio_sesion(usuario,clave):
            ventana_mensajes()
            datos_mensajes.append(usuario)
            destinatario.append(usuario)
            lectura_msj = armar_diccionario(destinatario)
        else:
            comparar_inicio_sesion(usuario,clave)

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

    boton_volver = tk.Button(ventana_actual, text="Volver", command=ventana_bienvenida)
    boton_volver.config(bg="orange")
    boton_volver.pack(padx=5,pady=10)

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
        cant_intentos = 0
        pregunta = var.get()
        if not pregunta or pregunta == 'Elija una Opción':
            label_resultado.config(text="¡Por favor, elija una pregunta!")
            return
        indice = int(pregunta.split('.')[0])
        registro_creado = registro(usuario,clave, respuesta, indice, cant_intentos)
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
    opcion = tk.OptionMenu(ventana_actual,var,*['{}. {}'.format(i + 1, pregunta) for i, pregunta in enumerate(preguntas)])
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

    boton_volver = tk.Button(ventana_actual, text="Volver", command=ventana_bienvenida)
    boton_volver.config(bg="orange")
    boton_volver.pack(padx=5,pady=10)

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
        cifrado = f"C{clave}"
        datos_mensajes.append(cifrado)
        datos_mensajes.append(mensaje_cifrado)
        
    def cifrar_atbash():
        mensaje = entrada_mensaje.get()
        mensaje_cifrado = cifrado_atbash(mensaje)
        label_resultado.config(text=mensaje_cifrado)
        datos_mensajes.append("A")
        datos_mensajes.append(mensaje_cifrado)

    ventana_actual = tk.Tk()
    ventana_actual.title("Cifrado y envio de mensajes")
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
    boton_cifrar_cesar.pack(padx=5,pady=5)

    boton_cifrar_atbash = tk.Button(ventana_actual, text="Cifrar mensaje Atbash", command=cifrar_atbash)
    boton_cifrar_atbash.config(bg="orange")
    boton_cifrar_atbash.pack(padx=5,pady=5)

    boton_descifrar_cesar = tk.Button(ventana_actual, text="Descifrar mensaje César", command=decifrar_cesar)
    boton_descifrar_cesar.config(bg="orange")
    boton_descifrar_cesar.pack(padx=5,pady=5)

    boton_descifrar_atbash = tk.Button(ventana_actual, text="Descifrar mensaje Atbash", command=cifrar_atbash)
    boton_descifrar_atbash.config(bg="orange")
    boton_descifrar_atbash.pack(padx=5,pady=5)

    boton_enviar_Cesar = tk.Button(ventana_actual, text="Enviar mensaje cifrado César",command=ventana_EnvioMensajes)
    boton_enviar_Cesar.config(bg="orange")
    boton_enviar_Cesar.pack(padx=5,pady=5)

    boton_enviar_Atbash = tk.Button(ventana_actual, text="Enviar mensaje cifrado Atbash",command=ventana_EnvioMensajes)
    boton_enviar_Atbash.config(bg="orange")
    boton_enviar_Atbash.pack(padx=5,pady=5)
     
    boton_consultar = tk.Button(ventana_actual, text="Consultar mensajes recibidos",command=ventanaMensajes_propios)
    boton_consultar.config(bg="orange")
    boton_consultar.pack(padx=5,pady=5)

    label_resultado = tk.Label(ventana_actual, text="")
    label_resultado.config(bg="navajo white")
    label_resultado.pack()

def ordenar_mensajes():
    global destinatario
    lectura_msj = armar_diccionario(destinatario)
    cantidad = usuarios_registrados()
    lista_anidada = []
    for valor in lectura_msj.values():
        if valor[0] == cantidad:
            remitente = '#' + valor[2]
            if valor[3] != "A":
                nro_clave = int(valor[3][1:])
                mensaje_oculto = descifrado_cesar(valor[4],nro_clave)
            else:
                mensaje_oculto = cifrado_atbash(valor[4])
            lista_anidada.append([remitente,mensaje_oculto])
        elif valor[0] < cantidad and destinatario[0] == valor[1]:
            remitente = valor[2]
            if valor[3] != "A":
                nro_clave = int(valor[3][1:])
                mensaje_oculto = descifrado_cesar(valor[4],nro_clave)
            else:
                mensaje_oculto = cifrado_atbash(valor[4])
            lista_anidada.append([remitente,mensaje_oculto])
    return sorted(lista_anidada, key=lambda x:('#' not in x[0], x[0]))
    
def ventanaMensajes_propios():
    lista = ordenar_mensajes()
    global ventana_actual
    cerrar_ventana_actual()

    ventana_actual = tk.Tk()
    ventana_actual.geometry("350x300")
    ventana_actual.config(bg="thistle1")
    ventana_actual.title("Mensajes Recibidos")
    label_leer = tk.Label(ventana_actual,text="Lista de Mensajes: \n")
    label_leer.config(bg="thistle1")
    label_leer.pack()
    contador = 0
    for indice in lista:
        label_mensaje = tk.Label(ventana_actual,text=f"{indice[0]}: {indice[1]}")
        label_mensaje.config(bg="thistle1")
        contador += 1
        label_mensaje.pack()
    
    label_contador = tk.Label(ventana_actual,text=f"Total mensajes: {contador}")
    label_contador.config(bg="thistle1")
    label_contador.pack()
    destinatario.clear()
    lectura_msj.clear()  
    
def ventana_EnvioMensajes():
    global ventana_actual
    cerrar_ventana_actual()

    ventana_actual = tk.Tk()
    ventana_actual.title("Envio de Mensajes")
    ventana_actual.geometry("370x220")
    ventana_actual.config(bg="navajo white")

    def usuario_receptor():
        global datos_mensajes
        receptor = entrada_receptor.get()
        verificar = verificar_usuario(receptor)
        lista_grupo = elegir_receptor(receptor)
        if verificar and len(lista_grupo) > 0 and len(datos_mensajes) == 3:
            with open('mensajes.csv','a',encoding='utf-8') as archivo:
                i = 0
                while i < len(lista_grupo):
                    archivo.write(f"{lista_grupo[i]},{datos_mensajes[0]},{datos_mensajes[1]},{datos_mensajes[2]}\n")
                    i += 1
                messagebox.showinfo("","Mensaje Enviado")
        datos_mensajes.clear()

    label_receptor = tk.Label(ventana_actual,text="Ingrese destinatario,\n (si el destinatario son todos los usuarios ingrese '*'): ",font=("Comic sans MS",10))
    label_receptor.config(bg="navajo white")
    label_receptor.pack()

    entrada_receptor = tk.Entry(ventana_actual)
    entrada_receptor.pack()

    boton_enviar_receptor = tk.Button(ventana_actual,text="Confirmar",command=usuario_receptor)
    boton_enviar_receptor.config(bg="orange")
    boton_enviar_receptor.pack(padx=5,pady=5)

    boton_volver = tk.Button(ventana_actual, text="Volver", command=ventana_mensajes)
    boton_volver.config(bg="orange")
    boton_volver.pack(padx=5,pady=10)

ventana_bienvenida()