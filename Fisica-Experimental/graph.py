# sample points 
#sem pesos
X = [1.07, 2.26, 3.48, 4.66]
Y = [15.00, 30.00, 45.00, 60.00]

xerror = [0.02, 0.04, 0.05, 0.05]
yerror = [0.05, 0.05, 0.05, 0.05]

#       primeiro     |   segundo   |   terceiro  |  quarto
# m2a | 1.07 ± 0.02  | 2.26 ± 0.04 | 3.48 ± 0.05 | 4.66 ± 0.05
# m2b | 1.48 ± 0.02  | 3.10 ± 0.03 | 4.76 ± 0.04 | 6.38 ± 0.05

# com pesos
X = [1.48, 3.10, 4.76, 6.38]
Y = [15.00, 30.00, 45.00, 60.00]

xerror = [0.02, 0.03, 0.04, 0.05]
yerror = [0.05, 0.05, 0.05, 0.05]

# solve for a and b
def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

    S = sum([yi**2 for yi in Y]) + sum([xi**2 for xi in X])*b**2 - 2*b*sum([xi*yi for xi,yi in zip(X,Y)]) - 2*a*sum([yi for yi in Y]) + 2*b*a*sum([xi for xi in X]) + len(X)*a**2

    # n = len(X) = len(Y)
    numer = S*sum([xi**2 for xi in X])
    denum = (len(X) - 2)*(len(X)*sum([xi**2 for xi in X]) - sum([xi for xi in X])**2)

    da = (numer / denum)**(1/2)

    numer = n*len(X)
    db = (numer / denum)**(1/2)

    print('errors:\nda = {:.2f}\ndb = {:.2f}\n'.format(da, db)) 
    return a, b




# solution
a, b = best_fit(X, Y)
#best fit line:
#sem peso:
# distancia = 1.63 + 12.51(t²)
# da = 0.17
# db = 0.53

#com peso:
# distância = 1.47 + 9.17(t²)
# da = 0.14
# db = 0.39

# plot points and fit line
import matplotlib.pyplot as plt
from pylab import *
import matplotlib.ticker as mtick

fig = plt.figure()
ax = fig.add_subplot(111)

#ax.set_xticks(np.arange(min(X),max(X),0.15)) 
#ax.set_yticks(np. arange(min(Y),max(Y),5)) 

plt.locator_params(axis='x', nbins=40)
plt.locator_params(axis='y', nbins=10)

plt.scatter(X, Y)
yfit = [a + b * xi for xi in X]

ax.plot(X, yfit)

ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))


xlabel('t² [s²]')
ylabel('Distância [cm]')
title('Tempo ao quadrado por distância (com peso)')

plt.grid()

(_, caps, _) = plt.errorbar(X, Y, yerr=yerror, xerr=xerror, fmt='.k', markersize=1, capsize=4)

for cap in caps:
    cap.set_markeredgewidth(0.5)

show()