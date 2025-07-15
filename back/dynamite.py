from pickle import TRUE
import random 
import ast 
import os 
import time

def boas_vindas():
    print("\033[1;34m" + "=" * 70 + "\033[m")
    print("\033[1;31m")
    print(r"""
  ____   _    __  __ ____   ___    __  __ ___ _   _    _    ____   ___  
 / ___| / \  |  \/  |  _ \ / _ \  |  \/  |_ _| \ | |  / \  |  _ \ / _ \ 
| |    / _ \ | |\/| | |_) | | | | | |\/| || ||  \| | / _ \ | | | | | | |
| |___/ ___ \| |  | |  __/| |_| | | |  | || || |\  |/ ___ \| |_| | |_| |
 \____/_/   \_\_|  |_|_|   \___/  |_|  |_|___|_| \_/_/   \_\____/ \___/ 
    """)
    print("\033[m")
    print("\033[1;34m               🎯 Bem-vindo nosso Campo Minado! 🎯\033[m")
    print("\033[1;35m        Prepare-se para testar sua sorte e lógica...\033[m")
    print("\033[1;35m         Desenvolvido por Karolynne, Ruth e Erwin 💡\033[m")
    print("\033[1;34m" + "=" * 70 + "\033[m\n")

    nomeJogador = input("\033[1;35mDigite seu nome para começar: \033[m").strip()
    return nomeJogador




# Exibe o menu principal e retorna a opção escolhida
def menu_principal():
    limpar_tela()
    print("\033[1;34m" + "=" * 40)
    print("        🚩 MENU PRINCIPAL 🚩")
    print("=" * 40 + "\033[m")
    
    print("\033[1;32m(1)\033[m 🎮 Começar o jogo")
    print("\033[1;33m(2)\033[m 🔁 Recomeçar o último jogo")
    print("\033[1;36m(3)\033[m ⏱️ Os cinco melhores tempos")
    print("\033[1;35m(4)\033[m 📊 Estatísticas e Histórico")
    print("\033[1;31m(5)\033[m ❌ Sair")
    
    opcao = input("\n\033[1;36mEscolha uma das opções acima: \033[m")
    return opcao


# Exibe o menu de escolha do nível de dificuldade e retorna a opção escolhida
def menu_dificuldade():
    print("\033[1;34m" + "=" * 40)
    print("       🌟 Selecione a Dificuldade 🌟")
    print("=" * 40 + "\033[m")
    
    print("\033[1;32m(1)\033[m 😄 Fácil")
    print("\033[1;33m(2)\033[m 😬 Médio")
    print("\033[1;31m(3)\033[m 🔙 Voltar")
    
    opcao = input("\n\033[1;36mEscolha uma das opções acima: \033[m")
    return opcao


def menu_estatisticas():
    while True:
        print("\033[1;34m" + "=" * 40)
        print("       📊 MENU DE ESTATÍSTICAS")
        print("=" * 40 + "\033[m")
        
        print("\033[1;33m(1)\033[m 🏆 Ver Top 5 Melhores Vitórias")
        print("\033[1;36m(2)\033[m 📜 Ver Histórico Completo")
        print("\033[1;35m(3)\033[m 📈 Ver Estatísticas Gerais")
        print("\033[1;31m(4)\033[m 🔙 Voltar")
        
        opcao = input("\n\033[1;36mEscolha uma das opções acima: \033[m")

        if opcao == "1":
            cinco_melhores_tempos("tempovitoria4bombas.txt")
            cinco_melhores_tempos("tempovitoria6bombas.txt")
        elif opcao == "2":
            exibir_historico_completo()
        elif opcao == "3":
            exibir_estatisticas_gerais()
        elif opcao == "4":
            break
        else:
            print("\033[1;31m❌ Opção inválida! Tente novamente.\033[m\n")


# Cria um tabuleiro com o número de linhas informado
def criar_tabuleiro(quant_linhas):
    tabuleiro_campo = []

    for _ in range(quant_linhas):
        linha = ["*"] * quant_linhas
        tabuleiro_campo.append(linha)

    return tabuleiro_campo

# Exibe o tabuleiro na tela, formatado com índices de linha e coluna
def mostrar_tabuleiro(tabuleiro_campo):
    print("\t", end="")
    
    for coluna in range(1, len(tabuleiro_campo[0]) + 1):
        print(f"{coluna}", end="\t")
    print()

    for linha_idx, linha in enumerate(tabuleiro_campo):
        print(f"{linha_idx + 1}", end="\t")
        for elemento in linha:
            print(f"\033[1;35m{elemento}\033[m", end="\t")  
        print()


# Gera posições aleatórias para as bombas
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
            print(f"\033[1;31m ❌ A posição da linha deve ser um número inteiro entre 1 e {len(tabuleiro_campo)}!\033[m")

    while True:
        try:
            coluna = int(input("Digite o número da coluna: "))
            if coluna < 1 or coluna > len(tabuleiro_campo[0]):
                raise ValueError
            break
        except ValueError:
            print(f"\033[1;31m ❌ A posição da coluna deve ser um número inteiro entre 1 e {len(tabuleiro_campo[0])}!\033[m")

    return linha - 1, coluna - 1


# Salva o estado atual do jogo em um arquivo de texto
def salvar_jogo(tabuleiro_campo, posicoes_bombas, posicoes_escolhidas, tempo_anterior, arquivo_jogo, nome_jogador, finalizado=False):
    with open(arquivo_jogo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Jogador = {nome_jogador}\n")
        arquivo.write(f"Tabuleiro = {tabuleiro_campo}\n")
        arquivo.write(f"Bombas = {posicoes_bombas}\n")
        arquivo.write(f"Posições Escolhidas = {posicoes_escolhidas}\n")
        arquivo.write(f"Tempo de Jogo = {tempo_anterior}\n")
        arquivo.write(f"Finalizado = {finalizado}\n")
        
        
def registrar_partida_historico(nome_jogador, nivel, tempo, resultado):
    linha = f"{nome_jogador} | Nível: {nivel} | Tempo: {round(tempo, 2)}s | Resultado: {resultado}\n"
    
    with open("historico_partidas.txt", "a", encoding="utf-8") as historico:
        historico.write(linha)

    if resultado == "Vitória":
        with open("vitorias.txt", "a", encoding="utf-8") as vit:
            vit.write(linha)
    elif resultado == "Derrota":
        with open("derrotas.txt", "a", encoding="utf-8") as der:
            der.write(linha)

def exibir_estatisticas_gerais():
    limpar_tela()
    total_vitorias = 0
    total_derrotas = 0

    if os.path.exists("vitorias.txt"):
        with open("vitorias.txt", "r", encoding="utf-8") as v:
            total_vitorias = len(v.readlines())

    if os.path.exists("derrotas.txt"):
        with open("derrotas.txt", "r", encoding="utf-8") as d:
            total_derrotas = len(d.readlines())

    total_partidas = total_vitorias + total_derrotas

    print("📈 Estatísticas Gerais:")
    print(f"🎮 Total de partidas: {total_partidas}")
    print(f"🏆 Vitórias: {total_vitorias}")
    print(f"💣 Derrotas: {total_derrotas}")
    
def exibir_historico_completo():
    limpar_tela()
    if not os.path.exists("historico_partidas.txt"):
        print("\033[1;31m ❌ Nenhuma partida registrada ainda. \033[m")
        return

    print("📜 Histórico Completo:")
    with open("historico_partidas.txt", "r", encoding="utf-8") as hist:
        linhas = hist.readlines()
        for linha in linhas:
            print(f"🔹 {linha.strip()}")


# Carrega o jogo salvo, convertendo as strings de volta para listas/valores originais
def carregar_jogo(arquivo_salvo):
    tabuleiro = []
    bombas = []
    posicoes = []
    tempo = 0
    nome_jogador = ""
    finalizado = False

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
            elif chave == "Finalizado":
                finalizado = valor.lower() == "true"

    return tabuleiro, bombas, posicoes, tempo, nome_jogador, finalizado



# Lê o arquivo de tempos de vitória e exibe os 5 melhores tempos                      
def cinco_melhores_tempos(arquivo_vitoria):
    limpar_tela()
    if not os.path.exists(arquivo_vitoria):
        print("\033[1;31m ❌ Não possui nenhum arquivo de vitórias registrado. \033[m")
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
        print("\033[1;31m ❌ Não possui nenhuma vitória registrada. \033[m")

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

# Limpa o terminal, considerando se o sistema é Windows/Linux/Mac
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Loop principal do jogo: jogador escolhe posições até vencer ou perder (acertar a bomba)
# Verifica se a posição escolhida já foi usada
# Conta bombas ao redor e atualiza o tabuleiro
# Detecta vitória e calcula tempo total
def verificarPosicaoEscolhida(posicoes_bombas, posicoes_escolhidas, tabuleiro_campo_minado, tempo_anterior, arquivo_tempos_vitoria, arquivo_jogo_salvo, nome_jogador):
    print("Aperte CTRL+C, a qualquer momento, para encerrar o jogo!")
    lista_posicoes_escolhidas = posicoes_escolhidas
    tempo_inicial = time.time()
    nivel = f"{len(tabuleiro_campo_minado)}x{len(tabuleiro_campo_minado)}"

    while True:
        try:
            mostrar_tabuleiro(tabuleiro_campo_minado)
            linha, coluna = posicao_escolhida(tabuleiro_campo_minado)
            contador_bombas_ao_redor = 0
            lista_posicao_escolhida = [linha, coluna]

            if lista_posicao_escolhida in lista_posicoes_escolhidas:
                limpar_tela()
                print("\033[1;31m❌ Essa posição já foi preenchida! Tente novamente.\033[m")
                continue
            else:
                limpar_tela()
                lista_posicoes_escolhidas.append(lista_posicao_escolhida)

            # Verifica se o jogador perdeu
            if lista_posicao_escolhida in posicoes_bombas:
                limpar_tela()
                for posicao_bomba in posicoes_bombas:
                    tabuleiro_campo_minado[posicao_bomba[0]][posicao_bomba[1]] = "💣"
                mostrar_tabuleiro(tabuleiro_campo_minado)
                print("=" * 30)
                print("⚠️ Você perdeu! Cuidado na próxima vez!")
                print("=" * 30)

                tempo_final = time.time()
                tempo_total = (tempo_final - tempo_inicial) + tempo_anterior
                registrar_partida_historico(nome_jogador, nivel, tempo_total, "Derrota")

                salvar = input("Deseja salvar esta partida? (s/n): ").strip().lower()
                if salvar == "s":
                    salvar_jogo(tabuleiro_campo_minado, posicoes_bombas, lista_posicoes_escolhidas, tempo_total, arquivo_jogo_salvo, nome_jogador, finalizado=True)
                break

            # Conta bombas ao redor
            for bomba in posicoes_bombas:
                if abs(bomba[0] - linha) <= 1 and abs(bomba[1] - coluna) <= 1:
                    if bomba != [linha, coluna]:
                        contador_bombas_ao_redor += 1

            tabuleiro_campo_minado[linha][coluna] = contador_bombas_ao_redor

            # Verifica se o jogador ganhou
            if len(lista_posicoes_escolhidas) == ((len(tabuleiro_campo_minado) ** 2) - len(posicoes_bombas)):
                limpar_tela()
                tempo_final = time.time()
                tempo_vitoria = (tempo_final - tempo_inicial) + tempo_anterior
                mostrar_tabuleiro(tabuleiro_campo_minado)
                print("=" * 40)
                print(f"{round(tempo_vitoria, 2)} segundos")
                print(" 🎉 Parabéns, você ganhou o jogo! 🎉")
                print("=" * 40)

                with open(arquivo_tempos_vitoria, "a", encoding="utf-8") as tempos:
                    tempos.write(f"{nome_jogador}:{round(tempo_vitoria, 2)},")

                registrar_partida_historico(nome_jogador, nivel, tempo_vitoria, "Vitória")
                salvar_jogo(tabuleiro_campo_minado, posicoes_bombas, lista_posicoes_escolhidas, tempo_vitoria, arquivo_jogo_salvo, nome_jogador, finalizado=True)
                break

        except KeyboardInterrupt:
            tempo_final = time.time()
            tempo_anterior = (tempo_final - tempo_inicial) + tempo_anterior
            print("\n⏸️ Jogo interrompido. Salvando progresso...")
            salvar_jogo(tabuleiro_campo_minado, posicoes_bombas, lista_posicoes_escolhidas, tempo_anterior, arquivo_jogo_salvo, nome_jogador, finalizado=False)
            break




# Função principal do jogo, possui a lógica do Campo Minado
# Controla o fluxo de menus e chamadas de funções com base nas escolhas do jogador
def campominado():
    nomeJogador = boas_vindas()
    limpar_tela()

    tabuleiroCampoMinado4x4 = []
    posicoesBombasSorteadas4x4 = []
    listaPosicoesEscolhidas4x4 = []

    tabuleiroCampoMinado6x6 = []
    posicoesBombasSorteadas6x6 = []
    listaPosicoesEscolhidas6x6 = []

    tempoAnterior = 0

    while True:
        opcao1 = menu_principal() 
        limpar_tela()

        if opcao1 == "1":
            while True:
                opcao2 = menu_dificuldade()
                limpar_tela()

                if opcao2 == "1":
                    # Nível Fácil
                    if os.path.exists("ultimojogo4x4.txt"):
                        try:
                            _, _, _, _, _, finalizado = carregar_jogo("ultimojogo4x4.txt")
                            if finalizado:
                                print("⚠️ Você finalizou a última partida deste nível.")
                                resp = input("Deseja começar um novo jogo? (s/n): ").strip().lower()
                                if resp != "s":
                                    continue
                        except Exception:
                            pass

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
                    # Nível Médio
                    if os.path.exists("ultimojogo6x6.txt"):
                        try:
                            _, _, _, _, _, finalizado = carregar_jogo("ultimojogo6x6.txt")
                            if finalizado:
                                print("⚠️ Você finalizou a última partida deste nível.")
                                resp = input("Deseja começar um novo jogo? (s/n): ").strip().lower()
                                if resp != "s":
                                    continue
                        except Exception:
                            pass

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
                    print("\033[1;31m❌ Opção inválida! Tente novamente.\033[m")

        elif opcao1 == "2":
            while True:
                opcao3 = menu_dificuldade()
                limpar_tela()

                if opcao3 == "1":
                    try:
                        tabuleiroCampoMinado4x4, posicoesBombasSorteadas4x4, listaPosicoesEscolhidas4x4, tempoAnterior, _, finalizado = carregar_jogo("ultimojogo4x4.txt")
                        if finalizado:
                            mostrar_tabuleiro(tabuleiroCampoMinado4x4)
                            print("⚠️ O último jogo já foi finalizado. Comece um novo jogo para jogar novamente.")
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
                        print("\033[1;31m❌ Nenhum jogo salvo para recomeçar no nível Fácil.\033[m")
                        input("Pressione Enter para continuar...")

                elif opcao3 == "2":
                    try:
                        tabuleiroCampoMinado6x6, posicoesBombasSorteadas6x6, listaPosicoesEscolhidas6x6, tempoAnterior, _, finalizado = carregar_jogo("ultimojogo6x6.txt")
                        if finalizado:
                            mostrar_tabuleiro(tabuleiroCampoMinado6x6)
                            print("⚠️ O último jogo já foi finalizado. Comece um novo jogo para jogar novamente.")
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
                        print("\033[1;31m❌ Nenhum jogo salvo para recomeçar no nível Médio.\033[m")
                        input("Pressione Enter para continuar...")

                elif opcao3 == "3":
                    break
                else:
                    print("\033[1;31m❌ Opção inválida! Tente novamente.\033[m")

        elif opcao1 == "3":
            while True:
                opcao4 = menu_dificuldade()
                limpar_tela()

                if opcao4 == "1":
                    cinco_melhores_tempos("tempovitoria4bombas.txt")
                elif opcao4 == "2":
                    cinco_melhores_tempos("tempovitoria6bombas.txt")
                elif opcao4 == "3":
                    break
                else:
                    print("\033[1;31m❌ Opção inválida! Tente novamente.\033[m")

        elif opcao1 == "4":
            menu_estatisticas()

        elif opcao1 == "5":
            print("Obrigado por jogar! Até a próxima!")
            break

        else:
            print("\033[1;31m❌ Opção inválida! Tente novamente.\033[m")



# Inicia o jogo se o arquivo for executado
if __name__ == "__main__":
    campominado()
         

                    