import matplotlib.pyplot as plt
import numpy as np

#---------------------------------------------------------------------------------
# Função que plota o gráfico da função f:
# plane_func(a, b, L, U, c)
# Args:
# a : limite infgerior do intervalo da função.
# b : limite superior do intervalo da função.
# L : limite inferior do gráfico plotado.
# U : limite superior do gráfico plotado.
# c : cor do gráfico plotado.
def plane_func(f: float, a: float, b: float,L: float, U: float, c: str):
  x = np.arange(a, b, 0.1)
  fig, ax = plt.subplots()
  ax.set_xlim(L, U)
  ax.set_ylim(L, U)
  plt.plot(x, f(x), c)
  plt.xlabel("x")
  plt.ylabel(f"{str(f)[9:13]}")
  plt.title(f"{str(f)[9:14]} grafic")
  plt.grid(True)

def plane_func_INFO():
   print("Função que plota o gráfico da função f:\n" \
          "plane_func(a, b, L, U, c).\n" \
          "Args:\n" \
          "a : limite infgerior do intervalo da função.\n" \
          "b : limite superior do intervalo da função.\n" \
          "L : limite inferior do gráfico plotado.\n" \
          "U : limite superior do gráfico plotado.\n" \
          "c : cor do gráfico plotado.")
#---------------------------------------------------------------------------------
# Função para plotar um unico ponto:
# plane_ponto(x, y, c)
# Args:
# x : coordenada cartesiana x do ponto.
# y : coordenada cartesiana y do ponto.
# c : cor do ponto.
def plane_ponto(x: float, y: float, c: str):
  plt.plot(x, y, marker='o', color=c, linestyle='none')

def plane_ponto_INFO():
   print( "Função para plotar um unico ponto:\n" \
          "plane_ponto(x, y, c)\n" \
          "Args:\n" \
          "x : coordenada cartesiana x do ponto.\n" \
          "y : coordenada cartesiana y do ponto.\n" \
          "c : cor do ponto.")

#---------------------------------------------------------------------------------
# Função que plota muitos pontos:
# Args:
# lista_x : Lista das coordenadas x.
# lista_y : Lista das Cordenads y.
# lista_c : Lista daas cores de cada ponto.
def plane_pontos(lista_x: list[float], lista_y: list[float], lista_c: list[str]):
  i = 0
  while i < len(lista_x):
    plane_ponto(lista_x[i], lista_y[i], lista_c[i])
    i += 1
  plt.show()

def plane_pontos_INFO():
   print( "Função que plota muitos pontos:\n"\
          "Args:\n"\
          "lista_x : Lista das coordenadas x.\n"\
          "lista_y : Lista das Cordenads y.\n"\
          "lista_c : Lista daas cores de cada ponto.")
#---------------------------------------------------------------------------------
# Plota múltiplos vetores no mesmo gráfico.
# plane_vetores(origins, finals, colors)
# Args:
# origins (list[list[float]]): Uma lista de pontos de origem para cada vetor.
# finals (list[list[float]]): Uma lista de pontos finais para cada vetor.
# colors (list[str]): Uma lista de cores para cada vetor.
def plane_vetores(origins: list[list[float]], finals: list[list[float]], colors: list[str]):
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

def plane_vetores_INFO():
   print( "Plota múltiplos vetores no mesmo gráfico.\n"\
          "plane_vetores(origins, finals, colors)\n" \
          "Args:\n" \
          "origins (list[list[float]]): Uma lista de pontos de origem para cada vetor.\n"\
          "finals (list[list[float]]): Uma lista de pontos finais para cada vetor.\n" \
          "colors (list[str]): Uma lista de cores para cada vetor.\n" )
#--------------------------------------------------
# Função que plota gráfico junto com vetores
# plane_vet_graf(f, a, b, c, origins, finals, colors)
# Args:
# f : Função a ser plotada
# a : Extremo inferior do intervalo da função
# b : Exetremo superior do intervalo da função
# c : Cor da finção a ser plotada
# origins : lista das origens dos vetore
# finals : lista dos finais dos respectivos vetores
# colors : listas das cores de cada vetor respectivamente
def plane_vet_graf(f: float, a: float, b: float, c: str,
                        origins: list[list[float]], finals: list[list[float]], colors: list[str]):
   # ---> funções
   x = np.arange(a, b, 0.1)
   fig, ax = plt.subplots()
   plt.plot(x, f(x), c)
   # ---> vetores
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
   plt.show()

def plane_vet_graf_INFO():
   print("Função que plota gráfico junto com vetores\n" \
         "plane_vet_graf(f, a, b, c, origins, finals, colors)\n" \
         "Args:\n" \
          "f : Função a ser plotada\n" \
          "a : Extremo inferior do intervalo da função\n" \
          "b : Exetremo superior do intervalo da função\n" \
          "c : Cor da finção a ser plotada\n" \
          "origins : lista das origens dos vetore\n" \
          "finals : lista dos finais dos respectivos vetores\n" \
          "colors : listas das cores de cada vetor respectivamente")
#--------------------------------------------------------------------
# Função que plota gráfico junto com vetores e pontos:
# plane_vet_graf(f, a, b, c, origins, finals, colors)
# Args:
# func = [f : Função a ser plotada,
# ....... a : Extremo inferior do intervalo da função,
# ....... b : Exetremo superior do intervalo da função,
# ....... c : Cor da finção a ser plotada];
# vets = [origins : lista das origens dos vetore,
# ....... finals : lista dos finais dos respectivos vetores,
# ....... colors : listas das cores de cada vetor respectivamente],
# poits = [lista_x : Lista das coordenadas x,
# ....... lista_y : Lista das Cordenads y,
# ....... lista_c : Lista daas cores de cada ponto]

def plane_vetgrafp(funct: list, vets: list, points: list):                       
   # ---> funções
   x = np.arange(funct[1], funct[2], 0.1)
   fig, ax = plt.subplots()
   plt.plot(x, funct[0](x), funct[3])
   
   # ---> vetores
   # Ajusta o os limites do gráfico para plotagem do vetores
   min_x, max_x = np.inf, -np.inf
   min_y, max_y = np.inf, -np.inf

   for inicial, final, cor in zip(vets[0], vets[1], vets[2]):
        # Calcula as componentes do vetor
        u = final[0] - inicial[0]
        v = final[1] - inicial[1]

        ax.quiver(inicial[0], inicial[1], u, v,
                    angles='xy', scale_units='xy', scale=1, color=cor[0])

        # Atualiza os limites para o ajuste do gráfico
        min_x = min(min_x, inicial[0], final[0])
        max_x = max(max_x, inicial[0], final[0])
        min_y = min(min_y, inicial[1], final[1])
        max_y = max(max_y, inicial[1], final[1])
   # ---> pontos
   i = 0
   while i < len(points[0]):
      plane_ponto(points[0][i], points[1][i], points[2][i])
      i += 1

   ax.set_aspect('equal', adjustable='box')
   ax.set_xlim([min_x - 1, max_x + 1])
   ax.set_ylim([min_y - 1, max_y + 1])
   ax.grid(True)
   plt.show()

def plane_vetgrafp_INFO():
   print( 'Função que plota gráfico junto com vetores e pontos:\n' \
          'plane_vet_graf(f, a, b, c, origins, finals, colors)\n' \
          'Args:\n' \
          'func = [f : Função a ser plotada,\n' \
          '....... a : Extremo inferior do intervalo da função,\n' \
          '....... b : Exetremo superior do intervalo da função,\n' \
          '....... c : Cor da finção a ser plotada];\n' \
          'vets = [origins : lista das origens dos vetore,\n' \
          '....... finals : lista dos finais dos respectivos vetores,\n' \
          '....... colors : listas das cores de cada vetor respectivamente],\n' \
          'poits = [lista_x : Lista das coordenadas x,\n' \
          '....... lista_y : Lista das Cordenads y,\n' \
          '....... lista_c : Lista daas cores de cada ponto]')
