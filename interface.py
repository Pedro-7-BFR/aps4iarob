import tkinter as tk
from tkinter import messagebox

from aigyminsper.search.search_algorithms import AEstrela
from Entregador import Entregador
from gerador import gerar_mundo, mostrar_mapa


def executar():
    try:
        n = int(entrada.get())
        if n < 2:
            raise ValueError
    except ValueError:
        messagebox.showerror('Dimensão inválida', 'Digite um número inteiro maior ou igual a 2.')
        return

    mapa, agente, pacote, destino = gerar_mundo(n)
    mostrar_mapa(mapa, agente, pacote, destino)
    print(f'\nAgente Inicia: {agente} | Pacote: {pacote} | Destino: {destino}', flush=True)

    inicial = Entregador('', agente, pacote, False, mapa, destino)
    Entregador.conta_nodos = 0
    resultado = AEstrela().search(inicial, pruning='general')

    if resultado is None:
        print('Nao existe solucao para este mapa.', flush=True)
        messagebox.showinfo('Resultado', 'Não existe solução para este mapa.\n Veja o terminal.\nCaso queira encerrar o programa feche a janela Entregador')
    else:
        print('Solucao:', resultado.show_path())
        print('Custo total:', resultado.g)
        print('Nodos expandidos:', Entregador.conta_nodos, flush=True)
        messagebox.showinfo('Resultado', f'Solução encontrada! Custo: {resultado.g}\nVeja as ações no terminal.\nCaso queira encerrar o programa feche a janela Entregador')


janela = tk.Tk()
janela.title('Entregador')
janela.geometry('400x200')
janela.resizable(False, False)

tk.Label(janela, text='Dimensão do grid quadrado:').pack(pady=(18, 6))
entrada = tk.Entry(janela, justify='center')
entrada.insert(0, '2')
entrada.pack()
tk.Button(janela, text='Gerar e executar', command=executar).pack(pady=16)

janela.mainloop()
