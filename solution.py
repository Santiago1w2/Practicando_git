def pregunta_1(n: int) -> int:
    """
    Parametros:
        n (int): numero entero positivo.
    Retorna:
        int: cantidad de digitos primos encontrados en n.
    """
    contador = 0
    conjunto = [2, 3, 5, 7]
    while n > 0:
        digito = n % 10
        if digito in conjunto:
            contador += 1
        n = n // 10
    return contador

def pregunta_2(suma: int) -> float:
    """
    Parametros:
        suma (int): valor de suma deseado (entre 2 y 12).
    Retorna:
        float: porcentaje de veces que esa suma ocurre entre todas las combinaciones posibles.
    """
    contador = 0
    for i in range(1, 7, 1):
        for j in range(1, 7, 1):
            if i + j == suma:
                contador += 1
    porcentaje = (contador * 100) / 36
    return round(porcentaje,2)


def pregunta_3(cadena: str) -> (int, int, int):
    """
    Parametros:
        cadena (str): la cadena de entrada.
    Retorna:
        tuple: tupla con el conteo de (mayusculas, minusculas, otros).
    """
    cn_mayus = 0
    cn_min = 0
    cn_carac = 0
    f_cadena=str(cadena).replace(" ","")
    for i in f_cadena:
        if i in "ABCDEFGHIJKLMNOPQRSTUWXYZÑ":
            cn_mayus += 1
        elif i in "abcdefghijklmnopqrstuwxyzñ":
            cn_min += 1
        else:
            cn_carac += 1
    return (cn_mayus,cn_min,cn_carac)


def pregunta_4(lista1: list[int], lista2: list[int]) -> list[int]:
    """
    Parametros:
        lista1 (list) : lista
        lista2 (list) : lista
    Retorna:
        resultado (list): lista
    """

    return None 