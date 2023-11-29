def cifrado_cesar(mensaje, clave):
    """
    >>> cifrado_cesar("hola", 3)
    'krod'
    >>> cifrado_cesar("HELLO", 7)
    'OLSSV'
    >>> cifrado_cesar("Hello World", 13)
    'Uryyb Jbeyq'
    >>> cifrado_cesar("12345", 2)
    '34567'
    >>> cifrado_cesar("!@#$", 4)
    '!@#$'
    >>> cifrado_cesar("hello", -3)
    'ebiil'
    >>> cifrado_cesar("¡Hola! ¿Cómo estás? 123", 30)
    '¡Lspe! ¿Góqs iwxáw? 123'
    >>> cifrado_cesar("Hello123#World", 10)
    'Rovvy123#Gybvn'
    >>> cifrado_cesar("HELLO", 0)
    'HELLO'
    >>> cifrado_cesar("Este es un mensaje secreto.", 5)
    'Jxyj jx zs rjsxfoj xjhwjyt.'
    >>> cifrado_cesar("La respuesta es 42.", -1)
    'Kz qdrotdrsz dr 31.'
    """
    caracteres_invalidos = "áéíóúÁÉÍÓÚ"
    cifrado = ''
    for caracter in mensaje:
        if caracter.isalpha():
            if caracter not in caracteres_invalidos:
                base = ord('a') if caracter.islower() else ord('A')
                cifrado += chr((ord(caracter) - base + clave) % 26 + base)
            else:
                cifrado += caracter
        elif caracter.isdigit():
            cifrado += str((int(caracter) + clave) % 10)
        else:
            cifrado += caracter
    return cifrado

def descifrado_cesar(mensaje_cifrado, clave):
    """
    >>> descifrado_cesar('krod', 3)
    'hola'
    >>> descifrado_cesar('OLSSV', 7)
    'HELLO'
    >>> descifrado_cesar('Uryyb Jbeyq', 13)
    'Hello World'
    >>> descifrado_cesar('34567', 2)
    '12345'
    >>> descifrado_cesar('!@#$', 4)
    '!@#$'
    >>> descifrado_cesar('ebiil', -3)
    'hello'
    >>> descifrado_cesar('¡Lspe! ¿Góqs iwxáw? 123', 30)
    '¡Hola! ¿Cómo estás? 123'
    >>> descifrado_cesar('Rovvy123#Gybvn', 10)
    'Hello123#World'
    >>> descifrado_cesar('HELLO', 0)
    'HELLO'
    >>> descifrado_cesar('Jxyj jx zs rjsxfoj xjhwjyt.', 5)
    'Este es un mensaje secreto.'
    >>> descifrado_cesar('Kz qdrotdrsz dr 31.', -1)
    'La respuesta es 42.'
    """
    return cifrado_cesar(mensaje_cifrado, -clave)

if __name__ == "__main__":
    import doctest
    doctest.testmod()