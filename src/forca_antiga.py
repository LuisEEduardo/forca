nome_arquivo = "C:/Users/franc/Desktop/Forca/palavras_forca.txt"
from  random import choice
while True:
# Menu
    print('JOGO DA FORCA')
    print('\nMenu:\n')
    print('Digite G para gravar palavras no jogo\n')
    print('Digite J para jogar\n')
    print('Digite "sair" encerrar o jogo\n')
    opcao = input('\nDigite a opção: ')
        # Opção G:
    if opcao.lower() == 'g':
        # Lendo com read
        arquivo = open(nome_arquivo, 'r')
        lista_read = arquivo.read()
        arquivo.close()
        # Lendo com readlines
        arquivo = open(nome_arquivo, 'r')
        lista_de_palavras = arquivo.readlines()
        print('Lista de palavras:\n{}'.format(lista_read))
        print('\nColocando palavras para a forca: \nPara voltar ao menu principal digite "sair" ')
        while True:
            colocando_palavra = input('\nDigite uma palavra para o jogo: ').lower().strip()
            if colocando_palavra.lower() == 'sair':
                break
            # Verificando a existencia de uma palavra
            elif (colocando_palavra in lista_read):
                print('Está palavra já foi colocada !!!\n')
            else:
                lista_de_palavras.append(colocando_palavra + '\n')
                arquivo.close()
            
        # Gravando as palavras
        arquivo = open(nome_arquivo, 'w')
        arquivo.writelines(lista_de_palavras)
        arquivo.close()
    # Opção J
    elif opcao.lower() == 'j':
        arquivo = open(nome_arquivo, 'r')
        lista_jogar = arquivo.readlines()
        jogar_de_novo = 1
        palavra_sorteada = choice(lista_jogar)
        palavras_usadas = []
        while jogar_de_novo == 1:
            arquivo.close()
            tamanho_palavra = len(palavra_sorteada) - 1
            lista_underline = ['_'] * tamanho_palavra
            print('\nVocê tem 4 tentativas para acertar a palavra')
            print('\nA palavra sorteada tem {} letras'.format(tamanho_palavra))
            print(lista_underline)
            for i in range(1, 4 + 1):
                chute = input('\nDigite uma letra: ')
                # Se acertar a palavra
                if len(chute) > 1 and (chute.lower() in palavra_sorteada.lower()):
                    print('\nParabéns você acertou a palavra !!!\n')
                    break
                # Se acertar uma letra
                elif chute.lower() in palavra_sorteada.lower():
                    print('\nVocê acertou uma letra !!!\n')
                    # Se for somente uma letra 
                    if palavra_sorteada.count(chute.lower())==1: 
                        posicao_palavra = palavra_sorteada.index(chute)
                        removendo_underline = lista_underline.pop(posicao_palavra)
                        posicao_underline = lista_underline.insert(posicao_palavra, chute.upper())
                        print(lista_underline)
                    # Se a letra se repetir mais de uma vez 
                    elif palavra_sorteada.count(chute.lower())>1: 
                        # 1ª posição: 
                        n = palavra_sorteada.count(chute.lower()) # <---
                        posicao_palavra = palavra_sorteada.index(chute)
                        removendo_underline = lista_underline.pop(posicao_palavra)
                        posicao_palavra = lista_underline.insert(posicao_palavra, chute.upper())
                        # 2ª posição: 
                        for k in range(0,n+1): 
                            count_posicao = 0 
                            p1 = palavra_sorteada.find(chute.lower()) 
                            p2 = palavra_sorteada.find(chute.lower(),p1 + k) 
                            removendo_underline2 = lista_underline.pop(p2)
                            lista_letras = []
                            lista_letras.append(p2)
                            k = lista_letras[count_posicao]
                            posicao_underline2 = lista_underline.insert(k, chute.upper())
                            count_posicao = count_posicao + 1 
                        print(lista_underline)
                elif (chute.lower() in palavra_sorteada.lower()) == False and len(chute) > 1:
                    print('\nPERDEU !!! \n')
                if (chute.lower() in palavra_sorteada.lower()) == False and len(chute) == 1:
                    print('\nVocê errou uma letra !!! \n')
                if (4 - i) != 0: 
                    print('-' * 30 + '\n')
                    print('\nVOCÊ TEM MAIS {} TENTATIVAS\n'.format(4 - i))
                if len(chute)==1:
                    print('\nLetras que você já usou: ')
                    palavras_usadas.append(chute.upper())
                print(palavras_usadas)

            else:
                print('\nPerdeu\n')
                print('-' * 30)
            # Jogar Novamente 
            opcao_jogar = input('\nDeseja jogar novamente? (S/N) ')
            if opcao_jogar.lower() == 's':
                palavras_usadas.clear() 
                jogar_de_novo = 1
                sorteando_nova_palavra = choice(lista_jogar)
                # Sorteando a palavra novamente
                def escolha(palavra1,palavra2):
                    if palavra2 != palavra1:
                        return palavra2
                    else: 
                        palavra2 = choice(lista_jogar)
                        return escolha(palavra1,palavra2)
                palavra_sorteada = escolha(palavra_sorteada, sorteando_nova_palavra)
                #print(palavra_sorteada)
            else:
                jogar_de_novo = 0
    elif opcao == 'sair': 
        break 
    elif (opcao.lower() != 'g') and (opcao.lower() != 'j') and (opcao.lower() != 'sair'):
        print('\nOpção invalida\n')