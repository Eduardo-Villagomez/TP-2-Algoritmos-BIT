import csv
import tkinter as tk
from tp_P1 import cifrado_cesar
from tp_P2 import cifrado_atbash

usuario_global = {}

def cifrar_mensaje_cesar(destinatario, remitente, mensaje):
    clave = int(input("Ingrese la clave para cifrado César: "))
    mensaje_cifrado = cifrado_cesar(mensaje, clave)
    guardar_mensaje(destinatario, remitente, "C" + str(clave), mensaje_cifrado)

def cifrar_mensaje_atbash(destinatario, remitente, mensaje):
    mensaje_cifrado = cifrado_atbash(mensaje)
    guardar_mensaje(destinatario, remitente,"A", mensaje_cifrado)

def guardar_mensaje(destinatario, remitente, cifrado, mensaje_cifrado):
    with open('mensajes.csv', 'a', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow([destinatario, remitente, cifrado, mensaje_cifrado])
    print("Mensaje Enviado")

def enviar_mensaje():
    destinatario = input("Ingrese el destinatario del mensaje (* para todos): ")
    remitente = usuario_global["nombre"]
    mensaje = input("Ingrese el mensaje: ")
    
    print("Seleccione el tipo de cifrado:")
    print("1. Cifrado César")
    print("2. Cifrado Atbash")

    opcion = input("Ingrese el número correspondiente al cifrado deseado: ")

    if opcion == "1":
        cifrar_mensaje_cesar(destinatario, remitente, mensaje)
    elif opcion == "2":
        cifrar_mensaje_atbash(destinatario, remitente, mensaje)
    else:
        print("Opción no válida")

def ventana_bienvenida():
    ventana_bienvenida = tk.Tk()
    #ventana_bienvenida.resizable(0, 0)
    ventana_bienvenida.title("TP Grupal Parte 1 - Grupo: BIT")
    ventana_bienvenida.config(bg="light sky blue")

    mensaje_bienvenida = tk.Label(ventana_bienvenida, text="Bienvenido a la aplicación de mensajes \nsecretos del grupo BIT. Para continuar,\n presione Continuar, de lo contrario \ncierre la ventana" ,font=("Comic sans MS",14))
    mensaje_bienvenida.config(bg="light sky blue")
    mensaje_bienvenida.pack()

    integrantes_grupo = ['Eduardo Villagomez', 'Francisco Albinati', 'Cindy Calderón']

    lista_integrantes = tk.Label(ventana_bienvenida, text="Construída por:")
    lista_integrantes.config(bg="light sky blue")
    lista_integrantes.pack()

    for integrante in integrantes_grupo:
        label_integrante = tk.Label(ventana_bienvenida, text=integrante)
        label_integrante.config(bg="light sky blue")
        label_integrante.pack()

    
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    usuario_global["nombre"] = nombre_usuario

    boton_continuar = tk.Button(ventana_bienvenida, text="Continuar", command=ventana_mensajes)
    boton_continuar.config(bg="deep sky blue")
    boton_continuar.pack(padx=10,pady=15)

    ventana_bienvenida.mainloop()

def ventana_mensajes():
    ventana_mensajes = tk.Toplevel()
    #ventana_mensajes.resizable(0, 0)
    ventana_mensajes.title("TP Grupal Parte 2 - Grupo: BIT")
    ventana_mensajes.config(bg="navajo white")

    label_mensaje = tk.Label(ventana_mensajes, text="¡Bienvenido, {}! \nIngrese sus mensajes secretos:".format(usuario_global["nombre"]))
    label_mensaje.config(bg="navajo white")
    label_mensaje.pack()

    boton_enviar_mensaje = tk.Button(ventana_mensajes, text="Enviar Mensaje", command=enviar_mensaje)
    boton_enviar_mensaje.config(bg="yellow green")
    boton_enviar_mensaje.pack(padx=5, pady=10)

    ventana_mensajes.mainloop()

ventana_bienvenida()