import random

#dados
dado=(1,2,3,4,5,6)
Jogador1= []
Jogador2= []
jogada= 2

#menu do jogador
def menu ():
    print('''
    menu:
    [1] - jogar  
    [2] - Sair
    ''')
    
opcçãoescolhida= int(input("qual é a sua opção"))
    
jogar= 1
sair=2

if opcçãoescolhida == 1:
    return jogar()
if opcçãoescolhida == 2:
    return sair()   
    
def randomLista():
    return random.choice(dado)
def jogo():
    global jogada
    num = randomLista()
    if jogada % 2 != 0:
        Jogador1.append(num)
        print(f"Jogador1 tirou {num}.")
        jogada += 1
    else:
        Jogador2.append(num)
        print(f"Jogador2 tirou {num}")
        jogada +=1
    jogarNovamente()
def pontuaçãodefimdeJogo():
    print(f"Jogadas do Jogador1: {Jogador1}, Jogadas do Player 2: {Jogador2}, Soma Player1: {sum(Jogador1)}, Soma Player2: {sum(Jogador2)}")
    if sum(Jogador1) > sum(Jogador2):
        print("O jogador1 venceu !")
    if sum(Jogador1) == sum(Jogador2):
        print("Empate !")
    if sum(Jogador1) < sum(Jogador2):
        print("Jogador2 venceu !")
def jogarNovamente():
    print("o que deseja fazer?[1] proxima jogada, [2] menu")
    escolha = int(input(":"))
    match escolha:
        case 1:
            jogar()
        case 2:
            menu()
