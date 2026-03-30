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
    for i in cadena:
        if i in "ABCDEFJHIJKLMNEOPKRTUWXYZÑ":
            cn_mayus += 1
        elif i in "abcdefghijklmnopkrstuwxyzñ":
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
lista1=[1,3,5]
lista2=[2,4,6]



print("Esta es mi modificacion bro")
print("Segunda modificaicon")

#como estas amiguito
#espero que bien
