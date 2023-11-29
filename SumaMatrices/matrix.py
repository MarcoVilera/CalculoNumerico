import random


class Matrix:
    # Constructor, siempre recibe self como parametro aparte de otros parametros si es necesario
    def __init__(self):
        # Matriz Vacia
        self.matrix = []

    # Crea una matriz tamaño nxm
    def create_matrix(self):
        while True:
            tipo = input('Introduce el tipo de matriz Cuadrada o Rectangular ').lower()
            print(tipo)

            if tipo in ('cuadrada', 'rectangular'):
                pass
            else:
                print('Tipo de matriz no válido')
                continue

            if tipo == 'cuadrada':
                n = int(input('Introduce el tamaño de la matriz '))
                self.matrix = [[0 for i in range(n)] for j in range(n)]

                for i in range(n):
                    for j in range(n):
                        self.matrix[i][j] = random.randint(0, 100)
            else:
                n = int(input('Introduce número de filas '))
                m = int(input('Introduce número de columnas '))
                self.matrix = [[0 for i in range(m)] for j in range(n)]

                for i in range(n):
                    for j in range(m):
                        self.matrix[i][j] = random.randint(0, 100)

            break

    # Imprime la matriz
    def show_matrix(self):
        for row in self.matrix:
            print(*row, sep='\t')


matriz = Matrix()

matriz.create_matrix()
matriz.show_matrix()
