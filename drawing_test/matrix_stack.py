import math
# Your Matrix Stack Library

# you should modify the provided empty routines to complete the assignment

matrixStack = []

def identityMatrix():
    return [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    
def gtInitialize():
    global matrixStack
    matrixStack = []
    matrixStack.append(identityMatrix())

def gtMultiply(matrix1, matrix2):
    result = [[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                result[i][j] += matrix2[i][k] * matrix1[k][j]
    return result


def gtPopMatrix():

    if len(matrixStack) > 1:
        del matrixStack[-1]
    else:
        print("cannot pop the matrix stack")

def gtPushMatrix():

    ctm = matrixStack[-1]
    copyMatrix = identityMatrix()
    for i in range(4):
        for j in range(4):
            copyMatrix[i][j]=ctm[i][j]
    matrixStack.append(copyMatrix)

def gtScale(x,y,z):
    matrix = identityMatrix()
    matrix[0][0] = x
    matrix[1][1] = y
    matrix[2][2] = z
    matrixStack[-1] = gtMultiply(matrix, matrixStack[-1])

def gtTranslate(x,y,z):
    matrix = identityMatrix()
    matrix[0][3] = x
    matrix[1][3] = y
    matrix[2][3] = z
    matrixStack[-1] = gtMultiply(matrix, matrixStack[-1])

def gtRotateX(theta):
    ctm = identityMatrix()
    theta = theta * (math.pi/180)
    ctm[1][1] = cos(theta)
    ctm[1][2] = -(sin(theta))
    ctm[2][1] = sin(theta)
    ctm[2][2] = cos(theta)
    matrixStack[-1] = gtMultiply(ctm, matrixStack[-1])

def gtRotateY(theta):
    ctm = identityMatrix()
    theta = theta * (math.pi/180)
    ctm[0][0] = cos(theta)
    ctm[0][2] = sin(theta)
    ctm[2][0] = -(sin(theta))
    ctm[2][2] = cos(theta)
    matrixStack[-1] = gtMultiply(ctm, matrixStack[-1])

def gtRotateZ(theta):
    ctm = identityMatrix()
    theta = theta * (math.pi/180)
    ctm[0][0] = cos(theta)
    ctm[0][1] = -(sin(theta))
    ctm[1][0] = sin(theta)
    ctm[1][1] = cos(theta)
    matrixStack[-1] = gtMultiply(ctm, matrixStack[-1])

def print_ctm():
    # print(matrixStack)
    for row in matrixStack[-1]:
        print(row)
    print("\n")
    
def getMatrixStack():
    return matrixStack
    
