from tkinter import messagebox
def leer(archivo):
    # lee el archivo y devuelve una lista delimitada por coma
    linea = archivo.readline()
    if linea:
        linea = linea.strip("\n")
    else:
        linea = ","
    return linea.split(",")

def leer_usuario(archivo):
    USUARIO = 0
    nombre = leer(archivo)
    return nombre[USUARIO]

def verificar_usuario(receptor):
    with open('registro.csv','r') as archivo:
        nombre = leer_usuario(archivo)
        valido = False
        if receptor == "*":
            valido = True
        while nombre and not valido:
            if nombre == receptor:
                valido = True
            nombre = leer_usuario(archivo)
        if not valido:
            messagebox.showerror("","Destinatario Inexistente")
    return valido

def elegir_receptor(receptor):
    with open('registro.csv','r',encoding='utf-8') as archivo:
        nombre = leer_usuario(archivo)
        lista = []
        valido = False
        while nombre and not valido:
            if receptor == "*":
                lista.append(nombre)
            elif nombre == receptor:
                lista.append(nombre)
                valido = False
            nombre = leer_usuario(archivo)
    return lista 
