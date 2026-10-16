from aigyminsper.search.search_algorithms import AEstrela
from aigyminsper.search.graph import State


class Entregador(State):
    conta_nodos = 0

    def __init__(self, op, posAg, posPack, pegou, mapa, destino, custo=0):
        super().__init__(op)
        self.posAg = posAg
        self.posPack = posPack
        self.pegou = pegou
        self.mapa = mapa
        self.destino = destino
        self.custo = custo

    def successors(self):
        Entregador.conta_nodos += 1
        sucessores = []
        if self.is_goal():
            return sucessores

        linha, coluna = self.posAg
        n = len(self.mapa)

        if linha > 0 and self.mapa[linha - 1][coluna] != 1:
            nova_pos = (linha - 1, coluna)

            if self.pegou:
                nova_pos_pack = nova_pos
            else:
                nova_pos_pack = self.posPack

            sucessores.append(Entregador(
                'cima', nova_pos, nova_pos_pack,
                self.pegou, self.mapa,
                self.destino, self.custo_acao()
            ))


        if linha < n - 1 and self.mapa[linha + 1][coluna] != 1:
            nova_pos = (linha + 1, coluna)

            if self.pegou:
                nova_pos_pack = nova_pos
            else:
                nova_pos_pack = self.posPack

            sucessores.append(Entregador(
                'baixo', nova_pos, nova_pos_pack,
                self.pegou, self.mapa,
                self.destino, self.custo_acao()
            ))


        if coluna > 0 and self.mapa[linha][coluna - 1] != 1:
            nova_pos = (linha, coluna - 1)

            if self.pegou:
                nova_pos_pack = nova_pos
            else:
                nova_pos_pack = self.posPack

            sucessores.append(Entregador(
                'esquerda', nova_pos, nova_pos_pack,
                self.pegou, self.mapa,
                self.destino, self.custo_acao()
            ))


        if coluna < n - 1 and self.mapa[linha][coluna + 1] != 1:
            nova_pos = (linha, coluna + 1)

            if self.pegou:
                nova_pos_pack = nova_pos
            else:
                nova_pos_pack = self.posPack

            sucessores.append(Entregador(
                'direita', nova_pos, nova_pos_pack,
                self.pegou, self.mapa,
                self.destino, self.custo_acao()
            ))

        if not self.pegou and self.posAg == self.posPack:
            sucessores.append(Entregador(
                'pegar', self.posAg, self.posPack, True,
                self.mapa, self.destino, self.custo_acao()
            ))

        if self.pegou and self.posAg == self.destino:
            sucessores.append(Entregador(
                'entregar', self.posAg, self.posAg, False,
                self.mapa, self.destino, self.custo_acao()
            ))

        return sucessores

    def is_goal(self):
        return self.posPack == self.destino and not self.pegou

    def description(self):
        return 'Entregador de pacote em grid'

    def custo_acao(self):
        linha, coluna = self.posAg

        if self.mapa[linha][coluna] == 2:
            return 3
        
        return 1
    
    def cost(self):
        return self.custo


    def env(self):
        return str((self.posAg, self.posPack, self.pegou))

    

    def h(self):
        if self.is_goal():
            return 0

        xAg, yAg = self.posAg
        xPack, yPack = self.posPack
        xDest, yDest = self.destino

        return (abs(xPack - xAg) + abs(yPack - yAg)
                + abs(xDest - xPack) + abs(yDest - yPack))


def main():
    mapa = [
        [0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    inicial = Entregador(
        '', (4, 1), (7, 2),
        False, mapa, (3, 3)
    )


    Entregador.conta_nodos = 0
    resultado = AEstrela().search(inicial, pruning="general")
    if resultado is None:
        print('Nao existe solucao para este mapa.')
        print('Nodos analisados:', Entregador.conta_nodos)

    else:
        print('Solucao:', resultado.show_path())
        print('Custo total:', resultado.g)
        print('Nodos analisados:', Entregador.conta_nodos)


if __name__ == '__main__':
    main()