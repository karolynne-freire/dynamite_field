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


def mostrar_tabuleiro (tabuleiro_campo):
    print("\t", end = "")
    
    for elemento in range (1, len(tabuleiro_campo[0])+1):
        print(elemento, end ="\t")
        
    print()
    
    for linha in range(len(tabuleiro_campo)):
        print(linha + 1, end= "\t")
        
        for elemento in tabuleiro_campo[linha]:
            print(elemento, end = "\t")
        
        print()
        
