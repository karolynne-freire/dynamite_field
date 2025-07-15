#Função que possui a logica do campo minado

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def verificar_posicao_escolhida (posicoes_bombas, posicoes_escolhidas, tabuleiro_campo_minado, tempo_anterior, arquivo_tempos_vitoria, arquivo_jogo_salvo):
    print("Aperte CTRL+C, a qualquer momento, para encerrar o jogo!")
    lista_posicoes_escolhidas = posicoes_escolhidas
    tempo_inicial = time.time()

    while True:
        try:
            print(posicoes_bombas)
            mostrar_tabuleiro(tabuleiro_campo_minado)
            linha, coluna = posicao_escolhida(tabuleiro_campo_minado)
            contador_bombas_ao_redor = 0
            lista_posicao_escolhida = [linha, coluna]

            #verificando se a posição ja foi escolhida
            if lista_posicao_escolhida in lista_posicoes_escolhidas:
                limpar_tela()
                print("Essa posicao ja foi preenchida!")

            else:
                limpar_tela()
                lista_posicoes_escolhidas.append(lista_posicao_escolhida)

            #verificando se o jogador perdeu
            if lista_posicao_escolhida in posicoes_bombas:
                limpar_tela()
                for posicao_bomba in posicoes_bombas:
                    tabuleiro_campo_minado[posicao_bomba[0]-1] [posicao_bomba[1]-1]="X"
                mostrar_tabuleiro(tabuleiro_campo_minado)
                print("Voce perdeu")
                break

            #Verificando quantas bombas ha ao redor da posicao escolhida
            for bomba in posicoes_bombas:
                if (linha +1) == bomba[0] or (linha - 1)== bomba[0]:
                    if bomba[1] == coluna:
                        contador_bombas_ao_redor +=1

                    if bomba[1] == coluna -1:
                        contador_bombas_ao_redor +=1
                    
                    if bomba[1] == coluna +1:
                        contador_bombas_ao_redor +=1

                elif linha == bomba[0]:
                    if bomba[1] == coluna -1:
                        contador_bombas_ao_redor +=1
                       
                    if bomba[1] == coluna +1:
                        contador_bombas_ao_redor +=1
            tabuleiro_campo_minado[linha -1][coluna -1]= contador_bombas_ao_redor

            #verificando se o jogador ganhou
            if len(lista_posicoes_escolhidas) == ((len(tabuleiro_campo_minado)**2) - len(posicoes_bombas)):
                limpar_tela()
                tempo_final = time.time()
                tempo_vitoria = (tempo_final - tempo_inicial) + tempo_anterior

                tempos = open(arquivo_tempos_vitoria, "a")
                tempos.write(str(round(tempo_vitoria,2))+",")
                tempos.close()

                mostrar_tabuleiro(tabuleiro_campo_minado)
                print(round(tempo_vitoria,2))
                print("Parabens, voce ganhou!")
                break
        
        #Caso o jagador saia, salva a partida ate aquele momento
        except KeyboardInterrupt:
            tempo_final = time.time()
            tempo_anterior = (tempo_final - tempo_inicial) + tempo_anterior
            salvar_jogo(tabuleiro_campo_minado, posicoes_bombas, lista_posicoes_escolhidas, tempo_anterior, arquivo_jogo_salvo)
            break
