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
# Função que plota um vetor (a,b) de origem (a1,a2) e final (b1, b2) e cor "c":
def plot_vetor(origin: list[float], final: list[float], c: str):
  fig, ax = plt.subplots()
  ax.quiver(origin[0], origin[1], final[0], final[1],
            angles = 'xy', scale_units = 'xy', scale = 1, color = c)
  ax.set_aspect('equal', adjustable='box')
  ax.set_xlim([origin[0] - 1, final[0] + 1])
  ax.set_ylim([origin[1]- 1, final[1]+ 2])
  ax.grid(True)
  plt.show()