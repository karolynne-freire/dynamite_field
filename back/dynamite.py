from pickle import TRUE
import random
import ast 
import os
import time


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
        linha_bomba = random.randint(0, len(tabuleiro_campo) - 1)
        coluna_bomba = random.randint(0, len(tabuleiro_campo[0]) - 1)

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

    return linha - 1, coluna - 1



def salvar_jogo(tabuleiro_campo, posicoes_bombas, posicoes_escolhidas, tempo_anterior, arquivo_jogo, nome_jogador):
    with open(arquivo_jogo, "w") as arquivo:
        arquivo.write(f"Jogador = {nome_jogador}\n")
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

                      
def cinco_melhores_tempos(arquivo_vitoria):
    if not os.path.exists(arquivo_vitoria):
        print("Arquivo de vitórias não encontrado.")
        return

    melhores_tempos = []

    with open(arquivo_vitoria, "r") as arquivo:
        linhas = arquivo.read().split(",")
        for linha in linhas:
            if ":" in linha:
                try:
                    nome, tempo = linha.strip().split(":")
                    melhores_tempos.append((nome, float(tempo)))
                except ValueError:
                    pass

    if not melhores_tempos:
        print("Não possui nenhuma vitória registrada.")
        return

    melhores_tempos.sort(key=lambda x: x[1])
    melhores_tempos = melhores_tempos[:5]

    print("🏆 Melhores Tempos:")

    posicoes = {
        1: "🥇 Primeiro",
        2: "🥈 Segundo",
        3: "🥉 Terceiro",
        4: "Quarto",
        5: "Quinto"
    }

    for i, (nome, tempo) in enumerate(melhores_tempos):
        posicao = posicoes.get(i + 1, f"{i+1}º")
        print(f"{posicao}: {nome} - {tempo:.2f} segundos")



def verificarPosicaoEscolhida(posicoesBombas, posicoesEscolhidas, tabuleiroCampoMinado, tempoAnterior, arquivoTemposVitoria, arquivoJogoSalvo):
    print("Aperte CTRL+C, a qualquer momento, para encerrar o jogo!")
    listaPosicoesEscolhidas = posicoesEscolhidas
    tempoInicial = time.time()

    while True:
        try:
            print(posicoesBombas)
            mostrar_tabuleiro(tabuleiroCampoMinado)
            linha, coluna = posicao_escolhida(tabuleiroCampoMinado)
            contadorBombasAoRedor = 0
            listaPosicaoEscolhida = [linha, coluna]

            if listaPosicaoEscolhida in listaPosicoesEscolhidas:
                os.system("cls")
                print("Essa posição já foi preenchida!")
            else:
                os.system("cls")
                listaPosicoesEscolhidas.append(listaPosicaoEscolhida)

            if listaPosicaoEscolhida in posicoesBombas:
                os.system("cls")
                for posicaoBomba in posicoesBombas:
                    tabuleiroCampoMinado[posicaoBomba[0] - 1][posicaoBomba[1] - 1] = "X"
                mostrar_tabuleiro(tabuleiroCampoMinado)
                print("Você perdeu!")

                salvar = input("Deseja salvar esta partida? (s/n): ").strip().lower()
                if salvar == "s":
                    nome = input("Digite seu nome: ").strip()
                    salvar_jogo(tabuleiroCampoMinado, posicoesBombas, listaPosicoesEscolhidas, tempoAnterior, arquivoJogoSalvo, nome)
                break

            for bomba in posicoesBombas:
                if (linha + 1) == bomba[0] or (linha - 1) == bomba[0]:
                    if bomba[1] in [coluna, coluna - 1, coluna + 1]:
                        contadorBombasAoRedor += 1
                elif linha == bomba[0]:
                    if bomba[1] in [coluna - 1, coluna + 1]:
                        contadorBombasAoRedor += 1

            tabuleiroCampoMinado[linha - 1][coluna - 1] = contadorBombasAoRedor

            if len(listaPosicoesEscolhidas) == ((len(tabuleiroCampoMinado) ** 2) - len(posicoesBombas)):
                os.system("cls")
                tempoFinal = time.time()
                tempoVitoria = (tempoFinal - tempoInicial) + tempoAnterior

                mostrar_tabuleiro(tabuleiroCampoMinado)
                print(f"{round(tempoVitoria, 2)} segundos")
                print("Parabéns, você ganhou!")

                nome = input("Digite seu nome para registrar o tempo: ").strip()
                with open(arquivoTemposVitoria, "a") as tempos:
                    tempos.write(f"{nome}:{round(tempoVitoria, 2)},")
                break

        except KeyboardInterrupt:
            tempoFinal = time.time()
            tempoAnterior = (tempoFinal - tempoInicial) + tempoAnterior
            nome = input("\nDigite seu nome para salvar o progresso: ").strip()
            salvar_jogo(tabuleiroCampoMinado, posicoesBombas, listaPosicoesEscolhidas, tempoAnterior, arquivoJogoSalvo, nome)
            break


def campominado():
    print("-----projeto de lógica programacional----")
    print("-----Karolynne, Ruth e Erwin-----")

    tabuleiroCampoMinado4x4=[]
    posicoesBombasSorteadas4x4=[]
    listaPosicoesEscolhidas4x4=[]

    tabuleiroCampoMinado6x6=[]
    posicoesBombasSorteadas6x6=[]
    listaPosicoesEscolhidas6x6=[]

    tempoAnterior = 0

    while True:
        opcao1 = menu_principal()
        os.system("cls")

        if opcao1 == "1":
            while True:
                opcao2 = menu_dificuldade()
                os.system("cls")

                if opcao2 == "1":
                    listaPosicoesEscolhidas4x4=[]
                    tempoAnterior = 0
                    tabuleiroCampoMinado4x4 = criar_tabuleiro(4)
                    posicoesBombasSorteadas4x4 = posicoes_bombas(6, tabuleiroCampoMinado4x4)
                    verificarPosicaoEscolhida(posicoesBombasSorteadas4x4, listaPosicoesEscolhidas4x4, tabuleiroCampoMinado4x4, tempoAnterior, "tempovitoria4bombas.txt", "ultimojogo4x4.txt")

                elif opcao2 == "2":
                    listaPosicoesEscolhidas6x6=[]
                    tempoAnterior = 0
                    tabuleiroCampoMinado6x6 = criar_tabuleiro(6)
                    posicoesBombasSorteadas6x6 = posicoes_bombas(10, tabuleiroCampoMinado6x6)
                    verificarPosicaoEscolhida(posicoesBombasSorteadas6x6, listaPosicoesEscolhidas6x6, tabuleiroCampoMinado6x6, tempoAnterior, "tempovitoria6bombas.txt", "ultimojogo6x6.txt")

                elif opcao2 == "3":
                    break
                else:
                    print("opcao Invalida!")

        elif opcao1 == "2":
            while True:
                opcao3 = menu_dificuldade()
                os.system("cls")

                if opcao3 == "1":
                    tabuleiroCampoMinado4x4, posicoesBombasSorteadas4x4, listaPosicoesEscolhidas4x4, tempoAnterior = carregar_jogo("ultimojogo4x4.txt")
                    verificarPosicaoEscolhida(posicoesBombasSorteadas4x4, listaPosicoesEscolhidas4x4, tabuleiroCampoMinado4x4, tempoAnterior, "temposvitoria4bombas.txt", "ultimojogo4x4.txt")

                elif opcao3 == "2":
                    tabuleiroCampoMinado6x6, posicoesBombasSorteadas6x6, listaPosicoesEscolhidas6x6, tempoAnterior = carregar_jogo("ultimojogo6x6.txt")
                    verificarPosicaoEscolhida(posicoesBombasSorteadas6x6, listaPosicoesEscolhidas6x6, tabuleiroCampoMinado6x6, tempoAnterior, "temposvitoria6bombas.txt", "ultimojogo6x6.txt")

                elif opcao3 == "3":
                    break
                else:
                    print("Opcao Invalida!")

        elif opcao1 == "3":
            while True:
                opcao4 = menu_dificuldade()
                os.system("cls")

                if opcao4 == "1":
                    cinco_melhores_tempos("temposvitoria4bombas.txt")

                elif opcao4 == "2":
                    cinco_melhores_tempos("temposvitoria4bombas.txt")

                elif opcao4 == "3":
                    break
                else:
                    print("Opcao Invalida!")

        elif opcao1 == "4":
            break

        else:
            print("Opcao Invalida!")


if __name__ == "__main__":
    campominado()
                    

                    