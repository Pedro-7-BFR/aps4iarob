import random


def gerar_mundo(n):
    if n < 2:
        raise ValueError('A dimens]ao mínima é 2.')

    mapa = []

    for linha in range(n):
        nova_linha = []

        for coluna in range(n):
            nova_linha.append(0)

        mapa.append(nova_linha)


    posicoes = []

    for linha in range(n):
        for coluna in range(n):
            posicoes.append((linha, coluna))

    agente, pacote, destino = random.sample(posicoes, 3)

    livres = []

    for pos in posicoes:
        if pos != agente and pos != pacote and pos != destino:
            livres.append(pos)
    random.shuffle(livres)


    qtd_obstaculos = random.randint(0, int(len(livres) * 0.30))
    obstaculos = []
    for i in range(qtd_obstaculos):
        obstaculos.append(livres[i])

    restantes = []
    for i in range(qtd_obstaculos, len(livres)):
        restantes.append(livres[i])

    qtd_pedagios = random.randint(0, int(len(restantes) * 0.20))
    pedagios = []
    for j in range(qtd_pedagios):
        pedagios.append(restantes[j])


    for linha, coluna in obstaculos:
        mapa[linha][coluna] = 1
    for linha, coluna in pedagios:
        mapa[linha][coluna] = 2

    return mapa, agente, pacote, destino


def mostrar_mapa(mapa, agente, pacote, destino):
    print('\nMapa gerado:')
    print('A = agente | P = pacote | X = destino | # = obstáculo | $ = pedágio | . = livre\n')
    for linha in range(len(mapa)):
        simbolos = []
        for coluna in range(len(mapa)):
            pos = (linha, coluna)
            if pos == agente:
                simbolo = 'A'
            elif pos == pacote:
                simbolo = 'P'
            elif pos == destino:
                simbolo = 'X'
            elif mapa[linha][coluna] == 1:
                simbolo = '#'
            elif mapa[linha][coluna] == 2:
                simbolo = '$'
            else:
                simbolo = '.'
            simbolos.append(simbolo)
        print(' '.join(simbolos))
