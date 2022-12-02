import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import matplotlib.ticker as mtick
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

#                   AMOSTRA EXPERIMENTAL
#       primeiro     |   segundo   |   terceiro  |  quarto
# m2a | 1.07 ± 0.02  | 2.26 ± 0.04 | 3.48 ± 0.05 | 4.66 ± 0.05
# m2b | 1.48 ± 0.02  | 3.10 ± 0.03 | 4.76 ± 0.04 | 6.38 ± 0.05
#

# coordenadas da amostra
x = [1.07, 2.26, 3.48, 4.66]
y = [15.00, 30.00, 45.00, 60.00]

# Incertezas da amostra
x_error = [0.02, 0.04, 0.05, 0.05]
y_error = [0.05, 0.05, 0.05, 0.05]

# com pesos
x = [1.48, 3.10, 4.76, 6.38]
y = [15.00, 30.00, 45.00, 60.00]

x_error = [0.02, 0.03, 0.04, 0.05]
y_error = [0.05, 0.05, 0.05, 0.05]

# tamanho da amostra
n = len(x)

# variaveis da amostra
sum_x = np.sum(x)
sum_x2 = np.sum(np.square(x))

sum_y = np.sum(y)
sum_y2 = np.sum(np.square(y))

sum_xy = np.sum(np.matmul(x, y))

#  coeficientes
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x)/n

s = sum_y2 + b**2 * sum_x2 - 2*b * sum_xy - 2*a * sum_y + 2*b*a * sum_x + n*a**2

#  incertezas
da = np.sqrt((s * sum_x2) / ((n - 2) * (n * sum_x2 - (sum_x)**2)))
db = np.sqrt((n * s)/((n - 2) * n * sum_x2 - (sum_x)**2))

# print("Sum_x: %.10f", sum_x)
# print("Sum_y: %.10f", sum_y)
# print("Sum_x2: %.10f", sum_x2)
# print("Sum_y2: %.10f", sum_y2)
# print("Sum_xy: %.10f", sum_xy)
# print("S: %.10f", s)

print("Minimos quadrados\n\n")

print("y = a + bx \n")
print("a = (%.10f +/- %.10f)\nb = (%.10f +/- %.10f)" % (a, da, b, db))

# Plotando o grafico

fig = plt.figure()
ax = fig.add_subplot()

plt.scatter(x, y, s=15, zorder=3, color='black')



cm = 1/2.54  # para acertar unidades

# tamanho do grafico
height = 18*cm
width = 28*cm

fig.set_size_inches (width, height)

plt.minorticks_on()
plt.grid(which="minor", linestyle='--', color='gray', linewidth=0.5)
plt.grid(which="major", linestyle='-', color='black', linewidth=0.5)

plt.locator_params(axis='x', nbins=20)
plt.locator_params(axis='y', nbins=10)

# ax.set_xlim([1, 4.75])
# ax.set_ylim([14, 61])

yfit = [a + b * xi for xi in x]
yfit2 = [(a+da) + (b+db) * xi for xi in x]
yfit3 = [(a-da) + (b-db) * xi for xi in x]

ax.plot(x, yfit, color='red', linewidth=0.5)
# ax.plot(x, yfit2, color='gray', linewidth=1.0)
# ax.plot(x, yfit3, color='gray', linewidth=1.0)

xlabel('t² [s²]')
ylabel('Distância [cm]')
title('Tempo ao quadrado por distância (com peso)')

(_, caps, _) = plt.errorbar(x, y, yerr=y_error, xerr=x_error, markersize=1, capsize=4, color='red', zorder=2)

for cap in caps:
    cap.set_markeredgewidth(0.5)

plt.savefig('myimage.svg', format='svg', dpi=1200)
