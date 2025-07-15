import os
#função principal que recebeos demis funçoes para executar
def campo_minado():
    print("----- Projeto de Lógica Programacional -----")
    print("----- Karolynne, Ruth e Erwin -----")
    print("----- Campo Minado -----")

    # Inicialização dos dados para 4x4 e 6x6
    tabuleiro_4x4 = []
    bombas_4x4 = []
    escolhas_4x4 = []

    tabuleiro_6x6 = []
    bombas_6x6 = []
    escolhas_6x6 = []

    tempo_anterior = 0

    while True:
        opcao_menu = menu_campo_minado()
        os.system("cls")

        if opcao_menu == "1":  # Novo Jogo
            while True:
                dificuldade = menu_dificuldade()
                os.system("cls")

                if dificuldade == "1":
                    escolhas_4x4 = []
                    tempo_anterior = 0
                    tabuleiro_4x4 = criar_tabuleiro(4)
                    bombas_4x4 = posicoes_bombas_sorteadas(6, tabuleiro_4x4)
                    verificar_posicao_escolhida(bombas_4x4, escolhas_4x4, tabuleiro_4x4, tempo_anterior, "tempovitoria4bombas.txt", "ultimojogo4x4.txt")

                elif dificuldade == "2":
                    escolhas_6x6 = []
                    tempo_anterior = 0
                    tabuleiro_6x6 = criar_tabuleiro(6)
                    bombas_6x6 = posicoes_bombas_sorteadas(10, tabuleiro_6x6)
                    verificar_posicao_escolhida(bombas_6x6, escolhas_6x6, tabuleiro_6x6, tempo_anterior, "tempovitoria6bombas.txt", "ultimojogo6x6.txt")

                elif dificuldade == "3":
                    break
                else:
                    print("Opção inválida!")

        elif opcao_menu == "2":  # Continuar jogo
            while True:
                dificuldade = menu_dificuldade()
                os.system("cls")

                if dificuldade == "1":
                    tabuleiro_4x4, bombas_4x4, escolhas_4x4, tempo_anterior = tabuleiro_salvo("ultimojogo4x4.txt")
                    verificar_posicao_escolhida(bombas_4x4, escolhas_4x4, tabuleiro_4x4, tempo_anterior, "tempovitoria4bombas.txt", "ultimojogo4x4.txt")

                elif dificuldade == "2":
                    tabuleiro_6x6, bombas_6x6, escolhas_6x6, tempo_anterior = tabuleiro_salvo("ultimojogo6x6.txt")
                    verificar_posicao_escolhida(bombas_6x6, escolhas_6x6, tabuleiro_6x6, tempo_anterior, "tempovitoria6bombas.txt", "ultimojogo6x6.txt")

                elif dificuldade == "3":
                    break
                else:
                    print("Opção inválida!")

        elif opcao_menu == "3":  # Ver melhores tempos
            while True:
                dificuldade = menu_dificuldade()
                os.system("cls")

                if dificuldade == "1":
                    cinco_melhores_tempos("tempovitoria4bombas.txt")

                elif dificuldade == "2":
                    cinco_melhores_tempos("tempovitoria6bombas.txt")

                elif dificuldade == "3":
                    break
                else:
                    print("Opção inválida!")

        elif opcao_menu == "4":
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    campo_minado()
