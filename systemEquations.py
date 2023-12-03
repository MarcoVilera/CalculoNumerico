import numpy as np
import matplotlib.pyplot as plt

""" 
Sistema de ecuaciones
    x + y + z = 6
    2x + y - z = 1
    3x - y + 2z = 7
"""

def ecuacion1(x):
    return (6-x)

def ecuacion2(x):
    return ((1-2*x)/-1)

def ecuacion3(x):
    return ((7-3*x)/2)

x = np.linspace(-5, 5, 100)

y1 = ecuacion1(x)
y2 = ecuacion2(x)
y3 = ecuacion3(x)

fig, ax = plt.subplots()
ax.plot(x, y1, label='x + y + z = 6')
ax.plot(x, y2, label='2x + y - z = 1')
ax.plot(x, y3, label='3x - y + 2z = 7')
ax.legend()

punto_interseccion = np.array([np.linalg.solve([[1, 1, 1], [2, 1, -1], [3, -1, 2]], [6, 1, 7])])

print('Punto de intersección:', punto_interseccion)


ax.scatter(punto_interseccion[0][0], punto_interseccion[0][1], c='r', marker='o', s=100)


plt.show()
