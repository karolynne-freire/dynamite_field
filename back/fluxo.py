from pickle import TRUE
import random
import ast 


def menu_principal():
    print("--- Jogo Campo Minado ---")
    print("(1) Começar o jogo")
    print("(2) Recomeçar o último jogo")
    print("(3) Os cinco melhores tempos")
    print("(4) Sair")
    
    opcao = input("Escolha uma das opções acima: ")
    return opcao

def menu_dificuldade ():
    print("\n(1) Fácil")
    print("(2) Médio")
    print("(3) Voltar")
   
    opcao = input("Escolha uma das opções acima: ")
    return opcao

def criar_tabuleiro(quant_linhas):
    linha_campo = ["*"] * quant_linhas
    tabuleiro_campo = []

    for _ in range(quant_linhas):
        tabuleiro_campo.append(linha_campo[:])

    return tabuleiro_campo


def mostrar_tabuleiro(tabuleiro_campo):
    print("\t", end="")

    for coluna in range(1, len(tabuleiro_campo[0]) + 1):
        print(coluna, end="\t")
    print()

    for linha_idx, linha in enumerate(tabuleiro_campo):
        print(linha_idx + 1, end="\t")
        for elemento in linha:
            print(elemento, end="\t")
        print()


def posicoes_bombas(quant_bombas, tabuleiro_campo):
    coordenadas_bombas = []

    while len(coordenadas_bombas) != quant_bombas:
        linha_bomba = random.randint(1, len(tabuleiro_campo))
        coluna_bomba = random.randint(1, len(tabuleiro_campo[0]))

        if [linha_bomba, coluna_bomba] not in coordenadas_bombas:
            coordenadas_bombas.append([linha_bomba, coluna_bomba])

    return coordenadas_bombas

def posicao_escolhida(tabuleiro_campo):
    while True:
        try:
            linha = int(input("Digite o número da linha: "))

            if linha < 1 or linha > len(tabuleiro_campo):
                raise ValueError

            break
        except ValueError:
            print(f"A posição da linha deve ser um número inteiro entre 1 e {len(tabuleiro_campo)}!")

    while True:
        try:
            coluna = int(input("Digite o número da coluna: "))

            if coluna < 1 or coluna > len(tabuleiro_campo[0]):
                raise ValueError

            break
        except ValueError:
            print(f"A posição da coluna deve ser um número inteiro entre 1 e {len(tabuleiro_campo[0])}!")

    return linha, coluna


def salvar_jogo(tabuleiro_campo, posicoes_bombas, posicoes_escolhidas, tempo_anterior, arquivo_jogo):
    with open(arquivo_jogo, "w") as arquivo:
        arquivo.write(f"Tabuleiro = {tabuleiro_campo}\n")
        arquivo.write(f"Bombas = {posicoes_bombas}\n")
        arquivo.write(f"Posições Escolhidas = {posicoes_escolhidas}\n")
        arquivo.write(f"Tempo de Jogo = {tempo_anterior}\n")

def carregar_jogo(arquivo_salvo):
    tabuleiro = []
    bombas = []
    posicoes = []
    tempo = 0

    with open(arquivo_salvo, "r") as arquivo:
        for linha in arquivo:
            chave, valor = linha.strip().split(" = ")
            if chave == "Tabuleiro":
                tabuleiro = ast.literal_eval(valor)
            elif chave == "Bombas":
                bombas = ast.literal_eval(valor)
            elif chave == "Posições Escolhidas":
                posicoes = ast.literal_eval(valor)
            elif chave == "Tempo de Jogo":
                tempo = float(valor)

    return tabuleiro, bombas, posicoes, tempo
                      
            
            
            
            