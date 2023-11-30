def sumMatrix(matrix1, matrix2):

    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        matrixResult = [] 
        for i in range(len(matrix1)):
            matrixResult.append([])
            for j in range (len(matrix1[0])):
                matrixResult[i].append(matrix1[i][j] + matrix2[i][j])      
        return matrixResult
    else:
        return None
