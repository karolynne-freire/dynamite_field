

#função principal que recebeos demis funçoes para executar

def campo_minado():
    print("-----projeto de lógica programacional----")
    print("-----Karolynne, Ruth e Erwin-----")
    print("-----campo minado-----")
# primeiro declaro uma lista vazia 4x4 e 6x6 e o tempo inicia zero
    tabuleiro_campo_minado4x4=[]
    posicoes_bombas_sorteadas4x4=[]
    lista_posicoes_escolhidas4x4=[]

    tabuleiro_campo_minado6x6=[]
    posicoes_bombas_sorteadas6x6=[]
    lista_posicoes_escolhidas6x6=[]

    tempo_anterior = 0

    while True:
        opcao1 = menu_campo_minado()
        os.system("cls")

        if opcao1 == "1":
            while True:
                opcao2 = menu_dificuldade()
                os.system("cls")

                if opcao2 == "1":
                    lista_posicoes_escolhidas4x4=[]
                    tempo_anterior = 0
                    tabuleiro_campo_minado4x4 = criar_tabuleiro(4)
                    posicoes_bombas_sorteadas4x4 = (posicoes_bombas_sorteadas(6,tabuleiro_campo_minado4x4))
                    verificar_posicao_escolhida(posicoes_bombas_sorteadas4x4, lista_posicoes_escolhidas4x4, tabuleiro_campo_minado4x4, tempo_anterior, "tempovitoria4bombas.txt", "ultimojogo4x4.txt")

                elif opcao2 == "2":
                    lista_posicoes_escolhidas6x6=[]
                    tempo_anterior = 0
                    tabuleiro_campoMinado6x6 = criar_tabuleiro(6)
                    posicoes_bombas_sorteadas6x6 = (posicoes_bombas_sorteadas(10,tabuleiro_campo_minado6x6))
                    verificar_posicao_escolhida(posicoes_bombas_sorteadas6x6, lista_posicoes_escolhidas6x6, tabuleiro_campo_minado6x6, tempo_anterior, "tempovitoria6bombas.txt", "ultimojogo6x6.txt")

                elif opcao2 == "3":
                    break
                else:
                    print("opção Inválida!")
        elif opcao1 == "2":
            while True:
                opcao3 = menu_dificuldade()
                os.system("cls")

                if opcao3 == "1":
                    tabuleiro_campo_mimado4x4,posicoes_bombas_sorteadas4x4, lista_posicoes_escolhidas4x4, tempo_anterior = tabuleiro_salvo("ultimojogo4x4.txt")
                    verificar_posicao_escolhida(posicoes_bombas_sorteadas4x4, lista_posicoes_escolhidas4x4, tabuleiro_campo_minado4x4, tempo_anterior, "temposvitoria4bombas.txt", "ultimojogo4x4.txt")

                elif opcao3 == "2":
                    tabuleiro_campo_mimado6x6,posicoes_bombas_sorteadas6x6, lista_posicoes_escolhidas6x6, tempo_anterior = tabuleiro_salvo("ultimojogo6x6.txt")
                    verificar_posicao_escolhida(posicoes_bombas_sorteadas6x6, lista_posicoes_escolhidas6x6, tabuleiro_campoMinado6x6, tempo_anterior, "temposvitoria6bombas.txt", "ultimojogo6x6.txt")

                elif opcao3 =="3":
                    break

                else:
                    print("Opção Inválida!")

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
                    print("Opção Inválida!")

        elif opcao1 == "4":
                    break

        else:
            print("Opção Inválida!")



        if _name_ == "_main_":
            campo_minado()
                    

                    
                            
                    

            
                    
    
