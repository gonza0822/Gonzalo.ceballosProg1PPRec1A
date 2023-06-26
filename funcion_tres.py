def ordenarCaracteres(cadena:str):
    cadena_ordenada = ""
    lista = list(cadena)
    print(lista)
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i +1, tam):
            if (lista[i] > lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    for caracteres in lista:
        cadena_ordenada += caracteres
    print(cadena_ordenada)
    return cadena_ordenada

ordenarCaracteres("hola")