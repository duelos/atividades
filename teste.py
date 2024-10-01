import random

# Criação dos tabuleiros
tabuleiro_jogador = [['~'] * 10 for _ in range(10)]
tabuleiro_pc = [['~'] * 10 for _ in range(10)]
tabuleiro_visivel_pc = [['~'] * 10 for _ in range(10)]  # Tabuleiro que o jogador vê do PC


def mostrar_tabuleiros():
    print("Seu tabuleiro:                  Tabuleiro do PC:")
    print('  0 1 2 3 4 5 6 7 8 9             0 1 2 3 4 5 6 7 8 9')
    letras = 'ABCDEFGHIJ'
    for i in range(10):
        linha_jogador = ' '.join(tabuleiro_jogador[i])
        linha_pc = ' '.join(tabuleiro_visivel_pc[i])
        print(f'{letras[i]} {linha_jogador}        {letras[i]} {linha_pc}')


def colocar_navio(tabuleiro, tamanho=5):
    while True:
        sentido = random.choice(['H', 'V'])
        if sentido == 'H':
            linha = random.randint(0, 9)
            coluna = random.randint(0, 10 - tamanho)
            disponivel = True
            for i in range(tamanho):
                if tabuleiro[linha][coluna + i] != '~':
                    disponivel = False
                    break
            if disponivel:
                for i in range(tamanho):
                    tabuleiro[linha][coluna + i] = '='
                break
        elif sentido == 'V':
            linha = random.randint(0, 10 - tamanho)
            coluna = random.randint(0, 9)
            disponivel = True
            for i in range(tamanho):
                if tabuleiro[linha + i][coluna] != '~':
                    disponivel = False
                    break
            if disponivel:
                for i in range(tamanho):
                    tabuleiro[linha + i][coluna] = '='
                break


def jogar_jogador():
    linhas = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    while True:
        mostrar_tabuleiros()
        linha = input("Digite a Linha: ").upper()
        coluna = int(input("Digite a Coluna: "))

        if tabuleiro_pc[linhas[linha]][coluna] == '~':
            print('ERROU, AI É ÁGUA!')
            tabuleiro_visivel_pc[linhas[linha]][coluna] = 'O'
            break
        elif tabuleiro_pc[linhas[linha]][coluna] == '=':
            print('ACERTOU O NAVIO!')
            tabuleiro_visivel_pc[linhas[linha]][coluna] = 'X'
            tabuleiro_pc[linhas[linha]][coluna] = 'X'
            break
        else:
            print('VOCÊ JÁ JOGOU AÍ!')


def jogar_pc():
    while True:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        if tabuleiro_jogador[linha][coluna] == '~':
            print('O PC ERROU, ELE ACERTOU ÁGUA!')
            tabuleiro_jogador[linha][coluna] = 'O'
            break
        elif tabuleiro_jogador[linha][coluna] == '=':
            print('O PC ACERTOU SEU NAVIO!')
            tabuleiro_jogador[linha][coluna] = 'X'
            break


def verificar_vitoria(tabuleiro):
    for linha in tabuleiro:
        if '=' in linha:
            return False
    return True


# Colocando navios no tabuleiro do jogador
colocar_navio(tabuleiro_jogador, 5)
colocar_navio(tabuleiro_jogador, 4)
colocar_navio(tabuleiro_jogador, 3)
colocar_navio(tabuleiro_jogador, 3)
colocar_navio(tabuleiro_jogador, 2)

# Colocando navios no tabuleiro do PC
colocar_navio(tabuleiro_pc, 5)
colocar_navio(tabuleiro_pc, 4)
colocar_navio(tabuleiro_pc, 3)
colocar_navio(tabuleiro_pc, 3)
colocar_navio(tabuleiro_pc, 2)

# Loop principal do jogo
while True:
    jogar_jogador()
    if verificar_vitoria(tabuleiro_pc):
        print("VOCÊ VENCEU! AFUNDOU TODOS OS NAVIOS DO PC!")
        break

    jogar_pc()
    if verificar_vitoria(tabuleiro_jogador):
        print("O PC VENCEU! ELE AFUNDOU TODOS OS SEUS NAVIOS!")
        break
