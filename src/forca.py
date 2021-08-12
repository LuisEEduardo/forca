def clean(): 
    import os 
    os.system('cls' if os.name == 'nt' else 'clear')


def pegando_palavras():
    """
    def pegando_palavras
    return the words that utility in game 
    """
    nome_arquivo = "/home/luis/forca/src/frutas.txt"
    file = open(nome_arquivo, 'r')
    arquivo_ref = file.readlines()
    file.close()
    palavras = tuple(map(lambda fruta: fruta.replace("\n", ""), arquivo_ref))
    return palavras


def escolhendo_palavra_aleatoria():    
    """
    def escolhendo_palavra_aleatoria -> Escolhe uma palavra aleatória da base de palavras
    return palavra escolhida randomicamente 
    """
    from random import choice  
    palavras = pegando_palavras()
    palavra_sorteada = choice(palavras)
    return palavra_sorteada


def tratando_palavra_sorteda(): 
    """
    tratando_palavra_sorteda -> pega a palavra sorteada e a trata 
    return Uma palavra 
    """
    palavra = escolhendo_palavra_aleatoria()
    palavra_underline = ["_" for x in range(len(palavra))]
    return palavra, palavra_underline


def jogando(palavra, palavra_modicificada):
    """
    jogando() -> Aqui onde a lógica do jogo acontece 
    return se o usuário ganhou ou não o jogo
    """
    # chutando uma letra
    clean()
    print(palavra)
    print("Dicas: ")
    print(f"É uma fruta")
    print(f"A sua palavra tem {len(palavra_modicificada)} letras")
    
    print(f"\n\n{palavra_modicificada}")

    # Subisituindo a letra
    chances = 6
    while chances > 0:
        chute = input("Insira uma letra ou a palavra: ")
        # Se for uma palavra
        if chute == palavra: 
            print("Você ganhou !!!")
            break
        # Se for uma letra
        elif chute in palavra: 
            qtd_de_repeticoes = palavra.count(chute)
            # chute repetida
            if (qtd_de_repeticoes > 1): 
                indice = palavra.index(chute)
                for i in range(qtd_de_repeticoes + 1): 
                    posicao = palavra.find(chute, indice)
                    if posicao > -1:
                        palavra_modicificada[posicao] = chute
                    indice = palavra.find(chute, (indice + 1))
            # verificando se ganhou 
            elif palavra_modicificada == ''.join(palavra_modicificada):
                print("Você ganhou !!!")
            # Sem reptição
            else: 
                posicao = palavra.find(chute)
                palavra_modicificada[posicao] = chute
            print(posicao)
            print(palavra_modicificada)
        else: 
            chances -= 1
            print(False)  
    

def apresentando_regra(): 
    from time import sleep
    clean()
    print("jogo da forca".upper())
    print("""Regras: \n1 - Você tera 6 chances de acertar a palavra \n1.1 - Se acertar a palavra dentro das 6 chances você ganha o jogo \n1.2 - Se não você perde 
    """)
    print("Começando ...")
    sleep(1)


# Escopo principal
apresentando_regra()
p1, p2 = tratando_palavra_sorteda()
jogando(palavra=p1, palavra_modicificada=p2)
