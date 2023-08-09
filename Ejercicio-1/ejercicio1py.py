numeros = [2,5,2,6,34,12,433,432,12,43]

def buscar_valor(lista, objetivo):
    for i in range(len(lista)):
        if(lista[i] == objetivo):
            return i
    return -1

print(buscar_valor(numeros, 2))
