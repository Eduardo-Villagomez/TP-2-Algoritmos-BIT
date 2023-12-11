def leer(archivo):
    # lee el archivo y devuelve una lista delimitada por coma
    linea = archivo.readline()
    if linea:
        linea = linea.strip("\n")
    else:
        linea = ","
    return linea.split(",")

def usuarios_registrados():
    with open('registro.csv','r',encoding="utf-8") as archivo:
        usuarios_registrados = 0
        linea = leer(archivo)
        while linea and not linea == ['','']:
            usuarios_registrados += 1
            linea = leer(archivo)
        return usuarios_registrados

def armar_diccionario(usuario):
    diccionario = {}
    with open('mensajes.csv','r',encoding="utf-8") as archivo:
        if len(usuario) == 1:
            for linea in archivo:
                dest,remitente,clave,mensaje = linea.rstrip("\n").split(",")
                clave_tupla = (remitente,clave,mensaje)
                if clave_tupla not in diccionario:
                    diccionario[clave_tupla] = [1,dest,remitente,clave,mensaje]
                else:
                    diccionario[clave_tupla][0] += 1
        return diccionario