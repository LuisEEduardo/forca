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
    from random import choice  
    palavras = pegando_palavras()
    palavra_sorteada = choice(palavras)
    return palavra_sorteada


def tratando_palavra_sorteda(): 




