## Descirção do projeto:
A dimensão do grid é definida pelo usuário por meio de uma interface gráfica desenvolvida com Tkinter. As posições do agente, pacote, destino, obstáculos e pedágios são geradas aleatoriamente pelo gerador.py

Escolhi usar o Tkinter por ser uma biblioteca simples e como só foi pedido que a interface
fosse para o usuário determinar o tamanho do mapa, foi isso que fiz, então o usuário escolhe
o tamanho que ele quer e as demais variáveis são geradas aleatoriamente, e após isso o entregador percorre em busca do objetivo. Caso não haja solução, ele retorna que não existe.


## Ações do Agente:
1) cima: movimenta uma célula para cima.

2) baixo: movimenta uma célula para baixo.

3) esquerda: movimenta uma célula para a esquerda.

4) direita: movimenta uma célula para a direita.

5) pegar: coleta o pacote quando o agente está na mesma posição.

6) entregar: entrega o pacote quando o agente está na posição de destino.


## Representação do Estado:
1) posAg: posição atual do agente.

2) posPack: posição atual do pacote.

3) pegou: indica se o agente está carregando o pacote.

4) mapa: matriz que representa o mundo.

5) destino: posição onde o pacote deve ser entregue.


## Heurística Utilizada:
A heurística considera a distância do agente até o pacote somada à distância do pacote até o destino:


h(n) = |x_{pacote} - x_{agente}| + |y_{pacote} - y_{agente}| + |x_{destino} - x_{pacote}| + |y_{destino} - y_{pacote}|


## Para instalar as bibliotecas necessárias recomendo as instruções a seguir:
1) python -m venv venv

2) venv/Scripts/Activate

3) pip install aigymsper

4) O Tkinter normalmente já acompanha a instalação do Python no Windows. Para verificar se
   está disponível, execute:

   python -m tkinter

   Se uma janela abrir, o Tkinter está funcionando corretamente.

   Caso não esteja instalado, execute novamente o instalador do Python e habilite a opção tcl/tk and IDLE nas funcionalidades opcionais.


## Para executar o projeto basta ter as bibliotecas instaladas e executar no terminal:

python interface.py


## EXEMPLOS DE EXECUÇÃO ##

## N = 2

Mapa gerado:
A = agente | P = pacote | X = destino | # = obstáculo | $ = pedágio | . = livre

A P
. X

Agente Inicia: (0, 0) | Pacote: (0, 1) | Destino: (1, 1)
Solucao:  ; direita ; pegar ; baixo ; entregar
Custo total: 4
Nodos expandidos: 4


## N = 3

Mapa gerado:
A = agente | P = pacote | X = destino | # = obstáculo | $ = pedágio | . = livre

. # A
. . P
. X .

Agente Inicia: (0, 2) | Pacote: (1, 2) | Destino: (2, 1)
Solucao:  ; baixo ; pegar ; esquerda ; baixo ; entregar
Custo total: 5
Nodos expandidos: 6

## N = 4

Mapa gerado:
A = agente | P = pacote | X = destino | # = obstáculo | $ = pedágio | . = livre

X . . .
. . . .
A . # .
. . P .

Agente Inicia: (2, 0) | Pacote: (3, 2) | Destino: (0, 0)
Solucao:  ; direita ; baixo ; direita ; pegar ; esquerda ; esquerda ; cima ; cima ; cima ; entregar
Custo total: 10
Nodos expandidos: 12

## N = 5

Mapa gerado:
A = agente | P = pacote | X = destino | # = obstáculo | $ = pedágio | . = livre

. . . . P
# . . # .
# . . . .
. # # . A
X . . . .

Agente Inicia: (3, 4) | Pacote: (0, 4) | Destino: (4, 0)
Solucao:  ; cima ; cima ; cima ; pegar ; baixo ; baixo ; esquerda ; baixo ; baixo ; esquerda ; esquerda ; esquerda ; entregar
Custo total: 13
Nodos expandidos: 21

## N = 6

Mapa gerado:
A = agente | P = pacote | X = destino | # = obstáculo | $ = pedágio | . = livre

. . P # . $
. . # . . .
A . . . . .
# . $ . . .
# . . . . .
X # . . . .

Agente Inicia: (2, 0) | Pacote: (0, 2) | Destino: (5, 0)
Nao existe solucao para este mapa.

## N = 7

Mapa gerado:
A = agente | P = pacote | X = destino | # = obstáculo | $ = pedágio | . = livre

. # . # . . #
. . # . . . .
. . . . # . .
. . . . . . P
. # X . . # .
. . . # . . #
A # . . . . #

Agente Inicia: (6, 0) | Pacote: (3, 6) | Destino: (4, 2)
Solucao:  ; cima ; direita ; direita ; cima ; direita ; direita ; cima ; direita ; direita ; pegar ; esquerda ; esquerda ; esquerda ; esquerda ; baixo ; entregar
Custo total: 16
Nodos expandidos: 23

## N = 8

Mapa gerado:
A = agente | P = pacote | X = destino | # = obstáculo | $ = pedágio | . = livre

. . . . . X . .
. . . . . . . .
. A . . . . . .
. . . . . . . .
. . . . . # . P
$ . . . . . . .
. . . . . . . .
. . . $ . . . .

Agente Inicia: (2, 1) | Pacote: (4, 7) | Destino: (0, 5)
Solucao:  ; direita ; direita ; direita ; direita ; direita ; direita ; baixo ; baixo ; pegar ; esquerda ; cima ; esquerda ; cima ; cima ; cima ; entregar
Custo total: 16
Nodos expandidos: 26

## N = 9
Mapa gerado:
A = agente | P = pacote | X = destino | # = obstáculo | $ = pedágio | . = livre

. . . . $ . . . .
. . . . . . . $ .
. . . . . . . . .
$ . . X . . . . .
. A . . . . . $ .
. $ . . . . . . .
. . . . . . . . #
. $ P . . . . . .
. . . . . . . . .

Agente Inicia: (4, 1) | Pacote: (7, 2) | Destino: (3, 3)
Solucao:  ; direita ; baixo ; baixo ; baixo ; pegar ; direita ; cima ; cima ; cima ; cima ; entregar
Custo total: 11
Nodos expandidos: 13

## N = 10

Mapa gerado:
A = agente | P = pacote | X = destino | # = obstáculo | $ = pedágio | . = livre

. . . . . $ . . . .
. . # . . . . $ X .
. . . . . . # $ . .
. # . $ . # . . # #
. # . . $ . . . # .
. . # . # A . . . $
# # # . # . . # . $
. # . . . # . . . .
# . . # . . . . . $
P . . # # # . # . .

Agente Inicia: (5, 5) | Pacote: (9, 0) | Destino: (1, 8)
Solucao:  ; cima ; esquerda ; esquerda ; baixo ; baixo ; baixo ; esquerda ; baixo ; esquerda ; baixo ; esquerda ; pegar ; direita ; direita ; cima ; cima ; direita ; cima ; cima ; cima ; cima ; cima ; direita ; direita ; cima ; direita; direita ; direita ; entregar
Custo total: 35
Nodos expandidos: 106