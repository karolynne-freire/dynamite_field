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
    tabuleiro_campo = []

    for _ in range(quant_linhas):
        linha = ["*"] * quant_linhas
        tabuleiro_campo.append(linha)

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
 with open(arquivo_jogo, "w", encoding="utf-8") as arquivo:
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
    nome_jogador = ""

    with open(arquivo_salvo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            chave, valor = linha.strip().split(" = ")
            if chave == "Jogador":
                nome_jogador = valor
            elif chave == "Tabuleiro":
                tabuleiro = ast.literal_eval(valor)
            elif chave == "Bombas":
                bombas = ast.literal_eval(valor)
            elif chave == "Posições Escolhidas":
                posicoes = ast.literal_eval(valor)
            elif chave == "Tempo de Jogo":
                tempo = float(valor)

    return tabuleiro, bombas, posicoes, tempo, nome_jogador


                      
def cinco_melhores_tempos(arquivo_vitoria):
    if not os.path.exists(arquivo_vitoria):
        print("❌ Não possui nenhum arquivo de vitórias registrado.")
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
        print(" ❌ Não possui nenhuma vitória registrada.")
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


def verificarPosicaoEscolhida(posicoesBombas, posicoesEscolhidas, tabuleiroCampoMinado, tempoAnterior, arquivoTemposVitoria, arquivoJogoSalvo, nomeJogador):
    print("Aperte CTRL+C, a qualquer momento, para encerrar o jogo!")
    listaPosicoesEscolhidas = posicoesEscolhidas
    tempoInicial = time.time()

    while True:
        try:
            mostrar_tabuleiro(tabuleiroCampoMinado)
            linha, coluna = posicao_escolhida(tabuleiroCampoMinado)
            contadorBombasAoRedor = 0
            listaPosicaoEscolhida = [linha, coluna]

            if listaPosicaoEscolhida in listaPosicoesEscolhidas:
                os.system("cls")
                print("Essa posição já foi preenchida!")
                continue
            else:
                os.system("cls")
                listaPosicoesEscolhidas.append(listaPosicaoEscolhida)

            if listaPosicaoEscolhida in posicoesBombas:
                os.system("cls")
                for posicaoBomba in posicoesBombas:
                    tabuleiroCampoMinado[posicaoBomba[0]][posicaoBomba[1]] = "💣"
                mostrar_tabuleiro(tabuleiroCampoMinado)
                print("Você perdeu!")

                salvar = input("Deseja salvar esta partida? (s/n): ").strip().lower()
                if salvar == "s":
                    salvar_jogo(tabuleiroCampoMinado, posicoesBombas, listaPosicoesEscolhidas, tempoAnterior, arquivoJogoSalvo, nomeJogador)
                break

            for bomba in posicoesBombas:
                if abs(bomba[0] - linha) <= 1 and abs(bomba[1] - coluna) <= 1:
                    if bomba != [linha, coluna]:
                        contadorBombasAoRedor += 1

            tabuleiroCampoMinado[linha][coluna] = contadorBombasAoRedor

            if len(listaPosicoesEscolhidas) == ((len(tabuleiroCampoMinado) ** 2) - len(posicoesBombas)):
                os.system("cls")
                tempoFinal = time.time()
                tempoVitoria = (tempoFinal - tempoInicial) + tempoAnterior
                mostrar_tabuleiro(tabuleiroCampoMinado)
                print(f"{round(tempoVitoria, 2)} segundos")
                print("Parabéns, você ganhou!")
                with open(arquivoTemposVitoria, "a", encoding="utf-8") as tempos:
                    tempos.write(f"{nomeJogador}:{round(tempoVitoria, 2)},")
                break

        except KeyboardInterrupt:
            tempoFinal = time.time()
            tempoAnterior = (tempoFinal - tempoInicial) + tempoAnterior
            salvar_jogo(tabuleiroCampoMinado, posicoesBombas, listaPosicoesEscolhidas, tempoAnterior, arquivoJogoSalvo, nomeJogador)
            break




def campominado():
    print("-----projeto de lógica programacional----")
    print("-----Karolynne, Ruth e Erwin-----")

    nomeJogador = input("Digite seu nome: ").strip()

    tabuleiroCampoMinado4x4 = []
    posicoesBombasSorteadas4x4 = []
    listaPosicoesEscolhidas4x4 = []

    tabuleiroCampoMinado6x6 = []
    posicoesBombasSorteadas6x6 = []
    listaPosicoesEscolhidas6x6 = []

    tempoAnterior = 0

    while True:
        opcao1 = menu_principal()
        os.system("cls")

        if opcao1 == "1":
            while True:
                opcao2 = menu_dificuldade()
                os.system("cls")

                if opcao2 == "1":
                    listaPosicoesEscolhidas4x4 = []
                    tempoAnterior = 0
                    tabuleiroCampoMinado4x4 = criar_tabuleiro(4)
                    posicoesBombasSorteadas4x4 = posicoes_bombas(6, tabuleiroCampoMinado4x4)
                    verificarPosicaoEscolhida(
                        posicoesBombasSorteadas4x4,
                        listaPosicoesEscolhidas4x4,
                        tabuleiroCampoMinado4x4,
                        tempoAnterior,
                        "tempovitoria4bombas.txt",
                        "ultimojogo4x4.txt",
                        nomeJogador
                    )

                elif opcao2 == "2":
                    listaPosicoesEscolhidas6x6 = []
                    tempoAnterior = 0
                    tabuleiroCampoMinado6x6 = criar_tabuleiro(6)
                    posicoesBombasSorteadas6x6 = posicoes_bombas(10, tabuleiroCampoMinado6x6)
                    verificarPosicaoEscolhida(
                        posicoesBombasSorteadas6x6,
                        listaPosicoesEscolhidas6x6,
                        tabuleiroCampoMinado6x6,
                        tempoAnterior,
                        "tempovitoria6bombas.txt",
                        "ultimojogo6x6.txt",
                        nomeJogador
                    )

                elif opcao2 == "3":
                    break
                else:
                    print("Opção inválida!")

        elif opcao1 == "2":
            while True:
                opcao3 = menu_dificuldade()
                os.system("cls")

                if opcao3 == "1":
                    try:
                        tabuleiroCampoMinado4x4, posicoesBombasSorteadas4x4, listaPosicoesEscolhidas4x4, tempoAnterior, _ = carregar_jogo("ultimojogo4x4.txt")

                        if any("💣" in linha for linha in tabuleiroCampoMinado4x4):
                            mostrar_tabuleiro(tabuleiroCampoMinado4x4)
                            print("⚠️ Você perdeu na última jogada. Comece um novo jogo para continuar.")
                            input("Pressione Enter para voltar ao menu...")
                        else:
                            verificarPosicaoEscolhida(
                                posicoesBombasSorteadas4x4,
                                listaPosicoesEscolhidas4x4,
                                tabuleiroCampoMinado4x4,
                                tempoAnterior,
                                "tempovitoria4bombas.txt",
                                "ultimojogo4x4.txt",
                                nomeJogador
                            )
                    except FileNotFoundError:
                        print("❌ Nenhum jogo salvo para recomeçar no nível Fácil.")
                        input("Pressione Enter para continuar...")

                elif opcao3 == "2":
                    try:
                        tabuleiroCampoMinado6x6, posicoesBombasSorteadas6x6, listaPosicoesEscolhidas6x6, tempoAnterior, _ = carregar_jogo("ultimojogo6x6.txt")

                        if any("💣" in linha for linha in tabuleiroCampoMinado6x6):
                            mostrar_tabuleiro(tabuleiroCampoMinado6x6)
                            print("⚠️ Você perdeu na última jogada. Comece um novo jogo para continuar.")
                            input("Pressione Enter para voltar ao menu...")
                        else:
                            verificarPosicaoEscolhida(
                                posicoesBombasSorteadas6x6,
                                listaPosicoesEscolhidas6x6,
                                tabuleiroCampoMinado6x6,
                                tempoAnterior,
                                "tempovitoria6bombas.txt",
                                "ultimojogo6x6.txt",
                                nomeJogador
                            )
                    except FileNotFoundError:
                        print("❌ Nenhum jogo salvo para recomeçar no nível Médio.")
                        input("Pressione Enter para continuar...")

                elif opcao3 == "3":
                    break
                else:
                    print("Opção inválida!")

        elif opcao1 == "3":
            while True:
                opcao4 = menu_dificuldade()
                os.system("cls")

                if opcao4 == "1":
                    cinco_melhores_tempos("tempovitoria4bombas.txt")
                elif opcao4 == "2":
                    cinco_melhores_tempos("tempovitoria6bombas.txt")
                elif opcao4 == "3":
                    break
                else:
                    print("Opção inválida!")

        elif opcao1 == "4":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    campominado()
         

                    