import numpy as np 
import matplotlib.pyplot as plt 



A = np.array([[-2 ,5 ,9 ],
              [ 7 ,1 ,1 ],
              [-3 ,7 -1 ]])


B = np.array([1,6,-26])

#A = np.array([[2,3,-1],
#               [-1,4,2],
#             [1,1,1]])
#B = np.array([7,2,4])

x_vals = np.linspace(-5,5,100)
y_vals = np.linspace(-5,5,100)
k = 1.8


y1 = (B[0]-(A[0,0]*x_vals)-A[0,2]*k)/A[0,1]
y2 = (B[1]-(A[1,0]*x_vals)-A[1,2]*k)/A[1,1]
y3 = (B[2]-(A[2,0]*x_vals)-A[2,2]*k)/A[2,1]
print(-A[2,2])
solutionSystem = np.linalg.solve(A,B)


plt.plot(x_vals, y1, label='-2x + 5y + 9z = 1')
plt.plot(x_vals, y2, label='7x + y + z = 6')
plt.plot(x_vals, y3, label='-3x + 7y - z = -26')

x_inter = solutionSystem[0]
y_inter = solutionSystem[1]
punto = 'Intersección ({},{})'.format(x_inter, round(y_inter,2))
plt.scatter(x_inter, y_inter, c='red', marker='o', s=100, label=punto)

plt.legend()
plt.grid()
plt.show()