import re

def reemplazarCaracteres(cadena:str, primer_car, segundo_car):
    contador = 0
    contador_primer_cadena = 0
    for caracteres in cadena:
        if(caracteres == segundo_car):
            contador_primer_cadena += 1
    cadena_reemplazada = re.sub(primer_car, segundo_car, cadena)
    for caracteres in cadena_reemplazada:
        if(caracteres == segundo_car):
            contador += 1
    contador = contador - contador_primer_cadena
    print(cadena_reemplazada)
    return contador

reemplazarCaracteres("hola", "o", "a")