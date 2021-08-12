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


def informacoes_sobre_o_jogo(palavra, palavra_certa, tentativas):
    print("Dicas:")
    print(f"palavra: {palavra_certa}")
    print(f"É uma fruta")
    print(f"A sua palavra tem {len(palavra)} letras")
    print(f"{boneco(posicao=tentativas)}")
    print(palavra)



def jogando(palavra, palavra_modicificada):
    from time import sleep
    """
    jogando() -> Aqui onde a lógica do jogo acontece 
    return se o usuário ganhou ou não o jogo
    """
    clean()
    # chutando e Subisituindo a letra
    chances = 0
    while chances != 8:
        informacoes_sobre_o_jogo(palavra=palavra_modicificada, palavra_certa=palavra, tentativas=chances)
        chute = input("Insira uma letra ou a palavra: ")
        # Se for uma palavra
        if chute == palavra: 
            print("\033[1;42;30mVocê ganhou !!!\033[m")
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
            elif palavra == ''.join(palavra_modicificada):
                print("\033[1;32mVocê ganhou !!!\033[m")
                break
            # Sem reptição
            else: 
                posicao = palavra.find(chute)
                palavra_modicificada[posicao] = chute
            print(palavra_modicificada)
        else: 
            chances += 1
            if chances == 7: 
                boneco(posicao=7)
                chances += 1
                print("\033[1;41;97mVocê perdeu\033[m ")
            else:
                print("\033[1;33mLetra Errada\033[m ")  
                sleep(2)
        clean()


def boneco(posicao):
    """
    Funcao boneco 
    return -> devolve a forca 
    """
    b = ["""
+=======+ 
|       |
|
|
|
|
=========
    """, """
+=======+ 
|       |
|       o
|
|
|
=========
    """, """
+=======+ 
|       |
|       o
|       |
|
|
=========
    """, """
+=======+ 
|       |
|       o
|      /|
|
|
=========
    """, """
+=======+ 
|       |
|       o
|      /|\\
|
|
=========
    """, 
    """
+=======+ 
|       |
|       o
|      /|\\
|       |
|
=========
    """, """
+=======+ 
|       |
|       o
|      /|\\
|       |
|      /|
=========
    """, """\033[1;31m 
+=======+ 
|       |
|       o
|      /|\\
|       |
|      /|\\
=========\033[m 
    """]
    return b[posicao]


def apresentando_regra(): 
    from time import sleep
    clean()
    print("jogo da forca".upper())
    print("""Regras: \n1 - Você tera 6 chances de acertar a palavra \n1.1 - Se acertar a palavra dentro das 6 chances você ganha o jogo \n1.2 - Se não você perde 
    """)
    print("Começando ...")
    sleep(3)


# Escopo principal
apresentando_regra()
p1, p2 = tratando_palavra_sorteda()
jogando(palavra=p1, palavra_modicificada=p2)
