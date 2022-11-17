def criarlistaZero(tamanho):
    lista = [0] * tamanho
    return lista

tamanhoDesejado= int(input("Qual será o tamanho escolhido?"))
lista = criarlistaZero(tamanhoDesejado)

for index in range(len(lista)):
    lista[index] = int(input(f"qual sera o valor da lista na posição?[{index}]:"))
    print(lista)
