import numpy as np 
import matplotlib.pyplot as plt 

#systemEquations 

"""A = np.array([[-2,5,9],
              [7,1,1],
              [-3,7,-1]])

#vectorSolution 
B = np.array([1,6,-26])"""

A = np.array([[2,3,-1],
              [-1,4,2],
              [1,1,1]])

B = np.array([7,2,4])

solutionSystem = np.linalg.solve(A,B)

x_vals = np.linspace(-5,5,100)
y_vals = np.linspace(-5,5,100)

plt.plot(x_vals, (7 + 2*x_vals + 3*y_vals), label='-2x + 5y + 9z = 1')
plt.plot(x_vals, (2 - 1*x_vals + 4*y_vals), label='7x + y + z = 6')
plt.plot(x_vals, (4 + 1*x_vals + y_vals), label='-3x + 7y - z = -26')

x_inter = solutionSystem[0]
y_inter = solutionSystem[1]

plt.scatter(x_inter, y_inter, c='red', marker='o', s=100)

plt.legend()
plt.grid()
plt.show()
