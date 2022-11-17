matriz = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

for linha in range(5):
    for coluna in range(5):
        if linha == coluna:
            matriz[linha][coluna] = 1
        else:
            matriz[linha][coluna] = 0

for index in range(5):
    print(matriz[index])
    
#esse eu treinei,e muito, fazendo a lista de matriz kkkk, pelo menos decidi treinar o certo :)