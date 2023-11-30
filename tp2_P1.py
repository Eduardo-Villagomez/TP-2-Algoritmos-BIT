import csv
def crear_usuario(usuario):
    """
    >>> crear_usuario('Foco120.')
    True
    >>> crear_usuario('Cel y120¡')
    False
    >>> crear_usuario('AbCdEf')
    False
    >>> crear_usuario('123123')
    False
    >>> crear_usuario('HOLA_15')
    True
    >>> crear_usuario('Zzzz-010')
    True
    >>> crear_usuario('ascci#1200')
    False
    >>> crear_usuario('michi')
    False
    >>> crear_usuario('Sol{}.010')
    False
    >>> crear_usuario('ABcde2020')
    False
    """
    letras = False
    caracter_especial = ["_","-","."]
    simbolos = False
    nombre_usuario = True
    i = 0
    
    if (5 <= len(usuario) <= 15):
        while i < len(usuario) and nombre_usuario:
            if usuario[i].isalnum():
                letras = True
            elif usuario[i] in caracter_especial:
                simbolos = True
            else:
                nombre_usuario = False
            i += 1
    return nombre_usuario if letras and simbolos else False

def crear_clave(clave):
    """
    >>> crear_clave('Ho2_')
    True
    >>> crear_clave('flo5#')
    False
    >>> crear_clave('Abba4*')
    False
    >>> crear_clave('D ado3*')
    False
    >>> crear_clave('Rojo7?')
    False
    >>> crear_clave('Frut7-')
    True
    >>> crear_clave('Dulce99*0')
    False
    >>> crear_clave('MunDO11#')
    False
    >>> crear_clave('Juego14*')
    True
    >>> crear_clave('Bot75**')
    False
    """
    mayuscula = False
    minuscula = False
    numero = False
    caracteres = ["_","-","#","*"]
    simbolos = False
    codigo_clave = True
    adyacentes = False
    validar_clave = False
    i = 0
    if (4 <= len(clave) <= 8):
        
        while i < len(clave) and codigo_clave:
            
            if i > 0 and clave[i] == clave[i - 1]:
                adyacentes = True
            elif clave[i].isupper():
                mayuscula = True
            elif clave[i].islower():
                minuscula = True
            elif clave[i].isdigit():
                numero = True
            elif clave[i] in caracteres:
                simbolos = True
            else:
                codigo_clave = False
            
            i += 1
        if not adyacentes and mayuscula and minuscula and numero and simbolos and codigo_clave:
            validar_clave = True
    return validar_clave

def registro(usuario,clave,respuesta,pregunta):
    validar_clave = crear_clave(clave)
    validar_usuario = crear_usuario(usuario)
    usuarios=[]
    if validar_clave and validar_usuario and len(respuesta) > 0:
        with open('registro.csv', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                usuarios.append(fila[0])
                if usuario in usuarios:
                    return "Identificador en Uso"   
        with open('registro.csv', 'a', newline='') as archivo:
            escritor_csv = csv.writer(archivo)
            escritor_csv.writerow([usuario,clave,pregunta,respuesta])

        valido = "Registro Exitoso"
    else:
        mensajes_error = []

        if not validar_clave:
            mensajes_error.append("Clave inválida")
        
        if not validar_usuario:
            mensajes_error.append("Nombre de usuario inválido")

        if len(respuesta) == 0:
            mensajes_error.append("La respuesta no puede estar vacía")

        valido = " / ".join(mensajes_error)
    
    return valido

def comparar_inicio_sesion(usuario,clave):
    TEXTO_RESULTADO_INICIO_SESION = ""
    valores = []
    with open('registro.csv', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            valores.append(fila[:2])

    index = 0
    TEXTO_RESULTADO_INICIO_SESION = "Identificador inexistente o clave errónea\n\n Si no se encuentra registrado debe registrarse previamente\n o si olvidaste la clave presiona el botón recuperar clave"

    while index < len(valores) and not (usuario == valores[index][0] and clave == valores[index][1]):
        index += 1

    if index < len(valores):
        TEXTO_RESULTADO_INICIO_SESION = "Inicio de sesión exitoso"

    return TEXTO_RESULTADO_INICIO_SESION

def recuperar_clave(id_pregunta, respuesta):
    with open('registro.csv', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        for fila in lector_csv:
            usuario_id = fila[2]
            usuario_respuesta = fila[3]

            if usuario_id == id_pregunta and usuario_respuesta == respuesta:
                return fila[1]  # Retorna la clave correspondiente

    return "Respuesta incorrecta o usuario no encontrado"