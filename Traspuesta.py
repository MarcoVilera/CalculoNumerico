matriz = [[29,12,44],
          [41,52,33]]

def trasponer (m):
    t = []
    for i in range(len(m[0])):
        t.append([])
        for j in range(len(m)):
            t[i].append(m[j][i])

    return t

traspuesta = trasponer (matriz)

for linea in matriz:
    for elemento in linea:
        print(elemento, end=" ")
    print()

print("----------------------")

for linea in traspuesta:
    for elemento in linea:
        print(elemento, end=" ")
    print()
