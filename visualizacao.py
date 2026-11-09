import pygame


def visualizar(mapa, agente, pacote, destino, acoes):
    n = len(mapa)
    if n == 0:
        raise ValueError('O mapa nao pode ser vazio.')

    celula = max(12, min(60, 660 // n))
    margem = 20
    painel = 100
    largura = n * celula + 2 * margem
    altura = n * celula + 2 * margem + painel

    pygame.init()
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('APS4 - Entregador')
    fonte = pygame.font.SysFont('arial', max(13, min(20, celula // 2)))
    fonte_painel = pygame.font.SysFont('arial', 18)
    relogio = pygame.time.Clock()


    if isinstance(acoes, str):
        acoes = [acao.strip() for acao in acoes.split(';') if acao.strip()]
    else:
        acoes = list(acoes)

    pos_agente = tuple(agente)
    pos_pacote = tuple(pacote)
    carregando = False
    entregue = pos_pacote == tuple(destino)
    indice = 0
    ultima_acao = 'Inicio'
    intervalo_ms = 800
    proximo_passo = pygame.time.get_ticks() + intervalo_ms
    executando = True

    def aplicar_acao(acao):
        nonlocal pos_agente, pos_pacote, carregando, entregue
        linha, coluna = pos_agente
        deslocamentos = {
            'cima': (-1, 0),
            'baixo': (1, 0),
            'esquerda': (0, -1),
            'direita': (0, 1),
        }
        if acao in deslocamentos:
            dl, dc = deslocamentos[acao]
            nova = (linha + dl, coluna + dc)
            if not (0 <= nova[0] < n and 0 <= nova[1] < n):
                raise ValueError(f'Movimento fora do mapa: {acao}')
            if mapa[nova[0]][nova[1]] == 1:
                raise ValueError(f'Movimento em obstaculo: {acao}')
            pos_agente = nova
            if carregando:
                pos_pacote = nova
        elif acao == 'pegar':
            if pos_agente != pos_pacote or carregando:
                raise ValueError('Acao pegar invalida.')
            carregando = True
        elif acao == 'entregar':
            if not carregando or pos_agente != tuple(destino):
                raise ValueError('Acao entregar invalida.')
            carregando = False
            entregue = True
        else:
            raise ValueError(f'Acao desconhecida: {acao}')

    while executando:
        agora = pygame.time.get_ticks()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                executando = False

        if indice < len(acoes) and agora >= proximo_passo:
            ultima_acao = acoes[indice]
            aplicar_acao(ultima_acao)
            indice += 1
            proximo_passo = agora + intervalo_ms

        tela.fill((245, 246, 248))
        for linha in range(n):
            for coluna in range(n):
                valor = mapa[linha][coluna]
                cor = (255, 255, 255)
                if valor == 1:
                    cor = (35, 35, 35)
                elif valor == 2:
                    cor = (170, 176, 184)
                ret = pygame.Rect(margem + coluna * celula,
                                  margem + linha * celula, celula, celula)
                pygame.draw.rect(tela, cor, ret)
                pygame.draw.rect(tela, (95, 100, 106), ret, 1)

        def centro(pos):
            linha, coluna = pos
            return (margem + coluna * celula + celula // 2,
                    margem + linha * celula + celula // 2)

        # Destino (X vermelho)
        cx, cy = centro(destino)
        raio = max(4, celula // 4)
        pygame.draw.line(tela, (205, 45, 45), (cx-raio, cy-raio), (cx+raio, cy+raio), 3)
        pygame.draw.line(tela, (205, 45, 45), (cx-raio, cy+raio), (cx+raio, cy-raio), 3)

        # Pacote (quadrado amarelo) - aparece na celula ou sobre o agente quando carregado
        if not entregue:
            px, py = centro(pos_pacote)
            lado = max(7, celula // 3)
            pacote_ret = pygame.Rect(px-lado//2, py-lado//2, lado, lado)
            pygame.draw.rect(tela, (245, 181, 59), pacote_ret)
            pygame.draw.rect(tela, (125, 83, 15), pacote_ret, 2)

        # Agente (circulo azul); desloca ligeiramente quando carrega o pacote
        ax, ay = centro(pos_agente)
        pygame.draw.circle(tela, (20, 117, 157), (ax, ay + (celula // 8 if carregando else 0)), max(4, celula // 5))
        if carregando:
            lado = max(7, celula // 3)
            pygame.draw.rect(tela, (245, 181, 59), (ax-lado//2, ay-celula//3, lado, lado))

        topo_painel = margem + n * celula + 14
        status = 'Entrega concluída!' if entregue else ('Sem solução para animar' if not acoes else f'Acao: {ultima_acao}')
        texto = fonte_painel.render(status, True, (35, 45, 55))
        tela.blit(texto, (margem, topo_painel))
        progresso = fonte.render(f'Passo {indice}/{len(acoes)}', True, (65, 75, 85))
        tela.blit(progresso, (margem, topo_painel + 28))
        ajuda = fonte.render('ESC: fechar janela', True, (85, 90, 100))
        tela.blit(ajuda, (margem, topo_painel + 52))
        pygame.display.flip()
        relogio.tick(60)

    pygame.quit()
