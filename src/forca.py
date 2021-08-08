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
    # chutando uma letra
    print()
    


def apresentando_regra(): 
    print("jogo da forca".upper())
    print("""Regras: \n1 - Você tera 6 chances de acertar a palavra \n1.1 - Se acertar a palavra dentro das 6 chances você ganha o jogo \n1.2 - Se não você perde 
    """)

apresentando_regra()
