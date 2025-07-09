

#função principal que recebeos demis funçoes para executar

def campominado():
    print("-----projeto de lógica programacional----")
    print("-----Karolynne, Ruth e Erwin-----")
    print("-----campo minado-----")
    tabuleiroCampoMinado4x4=[]
    posicoesBombasSorteadas4x4=[]
    listaPosicoesEscolhidas4x4=[]

    tabuleiroCampoMinado6x6=[]
    posicoesBombasSorteadas6x6=[]
    listaPosicoesEscolhidas6x6=[]

    tempoAnterior = 0

    while True:
        opcao1 = menuCampoMinado()
        os.system("cls")

        if opcao1 == "1":
            while True:
                opcao2 = menuDificuldade()
                os.system("cls")

                if opcao2 == "1":
                    listaPosicoesEscolhidas4x4=[]
                    tempoAnterior = 0
                    tabuleiroCampoMinado4x4 = criarTabuleiro(4)
                    posicoesBombasSorteadas4x4 = (posicoesBombasSorteadas(6,tabuleiroCampoMinado4x4))
                    verificarPosicaoEscolhida(posicoesBombasSorteadas4x4, listaPosicoesEscolhidas4x4, tabuleiroCampoMinado4x4, tempoAnterior, "tempovitoria4bombas.txt", "ultimojogo4x4.txt")

                elif opcao2 == "2":
                    listaPosicoesEscolhidas6x6=[]
                    tempoAnterior = 0
                    tabuleiroCampoMinado6x6 = criarTabuleiro(6)
                    posicoesBombasSorteadas6x6 = (posicoesBombasSorteadas(10,tabuleiroCampoMinado6x6))
                    verificarPosicaoEscolhida(posicoesBombasSorteadas6x6, listaPosicoesEscolhidas6x6, tabuleiroCampoMinado6x6, tempoAnterior, "tempovitoria6bombas.txt", "ultimojogo6x6.txt")

                elif opcao2 == "3":
                    break
                else:
                    print("opcao Invalida!")
        elif opcao1 == "2":
            while True:
                opcao3 = menuDificuldade()
                os.system("cls")

                if opcao3 == "1":
                    tabuleiroCampoMimado4x4,posicoesBombasSorteadas4x4, listaPosicoesEscolhidas4x4, tempoAnterior = tabuleiroSalvo("ultimojogo4x4.txt")
                    verificarPosicaoEscolhida(posicoesBombasSorteadas4x4, listaposicoesEscolhidas4x4, tabuleiroCampoMinado4x4, tempoAnterior, "temposvitoria4bombas.txt", "ultimojogo4x4.txt")

                elif opcao3 == "2":
                    tabuleiroCampoMimado6x6,posicoesBombasSorteadas6x6, listaPosicoesEscolhidas6x6, tempoAnterior = tabuleiroSalvo("ultimojogo6x6.txt")
                    verificarPosicaoEscolhida(posicoesBombasSorteadas6x6, listaposicoesEscolhidas6x6, tabuleiroCampoMinado6x6, tempoAnterior, "temposvitoria6bombas.txt", "ultimojogo6x6.txt")

                elif opcao3 =="3":
                    break

                else:
                    print("Opcao Invalida!")

        elif opcao1 == "3":
            while True:
                opcao4 = menuDificuldade()
                os.system("cls")

                if opcao4 == "1":
                    cincoMelhoresTempos("temposvitoria4bombas.txt")

                elif opcao4 == "2":
                    cincoMelhoresTempos("temposvitoria4bombas.txt")

                elif opcao4 == "3":
                    break
                        
                else:
                    print("Opcao Invalida!")

                elif opcao1 == "4":
                    break

                elif:
                    print("Opcao Invalida!")



        if _name_ == "_main_":
            campoMinado()
                    

                    
                            
                    

            
                    
    
