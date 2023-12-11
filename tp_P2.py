def cifrado_atbash(mensaje):
    """
    >>> cifrado_atbash("HOLA MUNDO")
    'sloz ñfnwl'
    >>> cifrado_atbash("CIFRADO ATBASH")
    'xruizwl zgyzhs'
    >>> cifrado_atbash("algoritmos1")
    'ZOTLIRGÑLH8'
    >>> cifrado_atbash("12345")
    '87654'
    >>> cifrado_atbash("!@#$")
    '!@#$'
    >>> cifrado_atbash("riverescampeon")
    'IREVIVHXZÑKVLN'
    >>> cifrado_atbash("¡Hola! ¿Cómo estás? 123")
    '¡sLOZ! ¿xóÑL VHGáH? 876'
    >>> cifrado_atbash("Hello123#World")
    'sVOOL876#dLIOW'
    >>> cifrado_atbash("HELLO")
    'svool'
    >>> cifrado_atbash("Este es un mensaje secreto.")
    'vHGV VH FN ÑVNHZQV HVXIVGL.'
    >>> cifrado_atbash("La respuesta es 42.")
    'oZ IVHKFVHGZ VH 57.'
    """
    alfabeto_normal = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    alfabeto_atbash = "ZYXWVUTSRQPOÑNMLKJIHGFEDCBAzyxwvutsrqpoñnmlkjihgfedcba9876543210"

    resultado = ""
    for caracter in mensaje:
        if caracter in alfabeto_normal:
            indice = alfabeto_normal.index(caracter)
            cifrado = alfabeto_atbash[indice]
            resultado += cifrado
        else:
            resultado += caracter
    return resultado
