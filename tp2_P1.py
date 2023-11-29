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

"""def agregar_preguntas():
    preguntas = [["6", "Email"],["7", "Comida preferida"],["8", "Mes de nacimiento"],["9", "Tipo de mascota"],["10", "Pelicula favorita"]]
    with open('preguntas.csv', 'a') as archivo:
        for elemento in preguntas:
            numero = elemento[0]
            pregunta = elemento[1]
            archivo.write(f"{numero},{pregunta}\n")
agregar_preguntas()"""
def registro(usuario,clave,respuesta,pregunta):
    validar_clave = crear_clave(clave)
    validar_usuario = crear_usuario(usuario)
    
    if validar_clave and validar_usuario and len(respuesta) > 0:
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


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())