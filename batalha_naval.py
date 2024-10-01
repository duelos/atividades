import random

tabuleiro = [['~'] * 10 for _ in range(10)]
tabuleiro_pc = tabuleiro[:]
tabuleiro_visivel = tabuleiro[:]

def mostrar_tabuleiro():
    print('Tabuleiro do Jogador:                         Tabuleiro do PC:')
    print('  0 1 2 3 4 5 6 7 8 9                         0 1 2 3 4 5 6 7 8 9') 
    letras = 'ABCDEFGHIJ' 

    for i in range(10):
        linhas_jogador = ' '.join(tabuleiro[i])
        linhas_pc = ' '.join(tabuleiro_visivel[i])
        print(f'{letras[i]} {linhas_jogador}                       {letras[i]} {linhas_pc}')
        
        


def jogar_jogador():
    vitoria = 0
    linhas = {'A':0,
              'B':1,
              'C':2,
              'D':3,
              'E':4,
              'F':5,
              'G':6,
              'H':7,
              'I':8,
              'J':9}
    while True:   
        mostrar_tabuleiro()
        
        linha = input("Digite a Linha: ").upper()
        coluna = int(input("Digite a Coluna: "))

        if tabuleiro[linhas[linha]][coluna] == '~':
            print('ERROU, AI É ÁGUA!')
            tabuleiro[linhas[linha]][coluna] = 'O'

        elif tabuleiro[linhas[linha]][coluna] == '=':
            print ('ACERTOU O NAVIO!')
            tabuleiro[linhas[linha]][coluna] = 'X'
            vitoria += 1

        else:
            print('VOCÊ JÁ JOGOU AÍ!')
        
        if vitoria == 15:
            print('VITORIA!')
            break

def jogar_pc():
    linha = random.randint(0,9)
    coluna = random.randint(0,9)
        


def colocar_navio(tamanho=5):
    if tamanho == 0:
        return
    
    else:
        while True:

            pos = 'HV'
            sentido = random.choice(pos)

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
        colocar_navio(tamanho-1)

def computador():
        colocar_navio()
        vitoria = 0
        while True:
            mostrar_tabuleiro()
            pc_linha = random.randint(0,9)
            pc_coluna = random.randint(0,9)
            tabuleiro[pc_linha][pc_coluna]
            if tabuleiro[pc_linha][pc_coluna] == '~':
                print('ERROU, AI É ÁGUA!')
                tabuleiro[pc_linha][pc_coluna] = 'O'

            elif tabuleiro[pc_linha][pc_coluna] == '=':
                print ('ACERTOU O NAVIO!')
                tabuleiro[pc_linha][pc_coluna] = 'X'
            vitoria += 1

#colocar_navio()
#jogar()
mostrar_tabuleiro()

