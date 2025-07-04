#Função que possui a logica do campo minado

def verificarPosicaoEscolhida (posicoesBombas, posicoesEscolhidas, tabuleiroCampoMinado, tempoAnterior, arquivoTemposVitoria, arquivoJogoSalvo):
    print("Aperte CTRL+C, a qualquer momento, para encerrar o jogo!")
    listaPosicoesEscolhidas = posicoesEscolhidas
    tempoInicial = time.time()

    while True:
        try:
            print(posicoesBombas)
            mostrarTabuleiro(tabuleiroCampoMinado)
            linha, coluna = posicaoEscolhida(tabuleiroCampoMinado)
            contadorBombasAoRedor = 0
            listaPosicaoEscolhida = [linha, coluna]

            #verificando se a posição ja foi escolhida
            if listaPosicaoEscolhida in listaPosicoesEscolhidas:
                os.system("cls")
                print("Essa posicao ja foi preenchida!")

            else:
                os.system("cls")
                listaPosicoesEscolhidas.append(listaPosicaoEscolhida)

            #verificando se o jogador perdeu
            if listaPosicaoEscolhida in posicoesBombas:
                os.system("cls")
                for posicaoBomba in posicoesBombas:
                    tabuleiroCampoMinado[posicaoBomba[0]-1]="X"
                mostrarTabuleiro(tabuleiroCampoMinado)
                print("Voce perdeu")
                break

            #Verificando quantas bombas ha ao redor da posicao escolhida
            for bomba in posicoesBombas:
                if (linha +1) == bomba[0] or (linha - 1)== bomba[0]:
                    if bomba[1] == coluna:
                        contadorBombasAoRedor +=1

                    if bomba[1] == coluna -1:
                        contadorBombasAoRedor +=1
                    
                    if bomba[1] == coluna +1:
                        contadorBombasAoRedor +=1

                elif linha == bomba[0]:
                    if bomba[1] == coluna -1:
                        contadorBombasAoRedor +=1
                       
                    if bomba[1] == coluna +1:
                        contadorBombasAoRedor +=1
            tabuleiroCampoMinado[linha -1][coluna -1]= contadorBombasAoRedor

            #verificando se o jogador ganhou
            if len(listaPosicoesEscolhidas) == ((len(tabuleiroCampoMinado)**2) - len(posicoesBombas)):
                os.system("cls")
                tempoFinal = time.time()
                tempoVitoria = (tempoFinal - tempoInicial) + tempoAnterior

                tempos = open(arquivoTemposVitoria, "a")
                tempos.write(str(round(tempoVitoria,2))+",")
                tempos.close()

                mostrarTabuleiro(tabuleiroCampoMinado)
                print(round(tempoVitoria,2))
                print("Parabens, voce ganhou!")
                break
        
        #Caso o jagador saia, salva a partida ate aquele momento
        except KeyboardInterrupt:
            tempoFinal = time.time()
            tempoAnterior = (tempoFinal - TempoInicial) + tempoAnterior
            salvarJogo(tabuleiroCampoMinado, posicoesBombas, listaPosicoesEscolhidas, tempoAnterior, arquivoJogoSalvo)
            break
