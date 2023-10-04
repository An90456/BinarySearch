

def binary_search(lista, numero_a_buscar):
    numero_inicial = 0
    numero_final = len(lista)-1
    while lista[(numero_final+numero_inicial)//2] != numero_a_buscar:
        if lista[(numero_final+numero_inicial)//2] < numero_a_buscar:
            numero_inicial = lista[(numero_final + numero_inicial) // 2]
        else:
            numero_final = lista[(numero_final + numero_inicial) // 2]

    return "Encontrado el numero: "+str(lista[(numero_final+numero_inicial)//2])



if __name__ == '__main__':
    lista = [1,2,3,4,5,6,7,8,9,10]
    numero_a_buscar = 7
    print(binary_search(lista, numero_a_buscar))
