import matplotlib.pyplot as plt
import numpy as np

#---------------------------------------------------------------------------------
# plota o gráfico da função f no intervalo [a,b], limites L e U com cor "c":
def plot_func(f: float, a: float, b: float,L: float, U: float, c: str):
  x = np.arange(a, b, 0.1)
  fig, ax = plt.subplots()
  ax.set_xlim(L, U)
  ax.set_ylim(L, U)
  plt.plot(x, f(x), c)
  plt.xlabel("x")
  plt.ylabel(f"{str(f)[9:13]}")
  plt.title(f"{str(f)[9:14]} grafic")
  plt.grid(True)

#---------------------------------------------------------------------------------
# Função para plotar um ponto na coordenada (x, y) e cor "c":
def plot_ponto(x: float, y: float, c: str):
  plt.plot(x, y, marker='o', color=c, linestyle='none')

#---------------------------------------------------------------------------------
# Função que plota muitos pontos:
# Args:
# lista_x : Lista das coordenadas x.
# lista_y : Lista das Cordenads y.
# lista_c : Lista daas cores de cada ponto.
def plot_pontos(lista_x: list[float], lista_y: list[float], lista_c: list[str]):
  i = 0
  while i < len(lista_x):
    plot_ponto(lista_x[i], lista_y[i], lista_c[i])
    i += 1
  plt.show()

#---------------------------------------------------------------------------------
# Plota múltiplos vetores no mesmo gráfico.
# Args:
# origins (list[list[float]]): Uma lista de pontos de origem para cada vetor.
# finals (list[list[float]]): Uma lista de pontos finais para cada vetor.
# colors (list[str]): Uma lista de cores para cada vetor.
def plot_vetores(origins: list[list[float]], finals: list[list[float]], colors: list[str]):
    fig, ax = plt.subplots()
    
    # Ajusta o os limites do gráfico para plotagem do vetores
    min_x, max_x = np.inf, -np.inf
    min_y, max_y = np.inf, -np.inf

    for origin, final, c in zip(origins, finals, colors):
        # Calcula as componentes do vetor
        u = final[0] - origin[0]
        v = final[1] - origin[1]

        ax.quiver(origin[0], origin[1], u, v,
                    angles='xy', scale_units='xy', scale=1, color=c)

        # Atualiza os limites para o ajuste do gráfico
        min_x = min(min_x, origin[0], final[0])
        max_x = max(max_x, origin[0], final[0])
        min_y = min(min_y, origin[1], final[1])
        max_y = max(max_y, origin[1], final[1])

    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim([min_x - 1, max_x + 1])
    ax.set_ylim([min_y - 1, max_y + 1])
    ax.grid(True)
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.set_title("Plot de Múltiplos Vetores")
    plt.show()