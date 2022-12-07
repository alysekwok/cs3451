# Drawing Routines that are similar to those in OpenGL
import math
from matrix_stack import *
vertexList = []

matrixStack = getMatrixStack()
type = ""
gLeft = 0
gRight = 0
gBottom = 0
gTop = 0
gFov = 0



def gtOrtho(left, right, bottom, top, near, far):
    global gLeft
    global gRight
    global gBottom
    global gTop
    global type 
    type = "ortho"
    gLeft = left
    gRight = right
    gBottom = bottom
    gTop = top


def gtPerspective(fov, near, far):
    global gFov
    global type
    type = "perspective"
    gFov = fov

def gtVertex(x, y, z):
    global vertexList

    global type
    global matrixStack
    global gLeft
    global gRight
    global gBottom
    global gTop
    global gFov
    matrixStack = getMatrixStack()
    
    ctm = matrixStack[-1] # get top of stack
    # print_ctm()
    if len(vertexList) == 1:
        endPoint= multiplyVector(ctm, [x,y,z,1])
        # print(endPoint)
        startPoint = multiplyVector(ctm, vertexList[0])
    else:
        vertexList.append([x,y,z,1])
        return
    if type == "ortho":
        matrix = [[float(width) / (gRight - gLeft),0,0,float(-gLeft) * width / (gRight - gLeft)],
            [0, float(height)/(gTop - gBottom),0,float(-gBottom) * height / (gTop - gBottom)],
            [0,0,1,0],
            [0,0,0,1]]
        startPoint = multiplyVector(matrix, startPoint)
        endPoint = multiplyVector(matrix, endPoint)
    else:
        fov = gFov * (math.pi/180)
        k = tan(fov/2)

        xPrimeStart = float(startPoint[0])/abs(startPoint[2])
        yPrimeStart = float(startPoint[1])/abs(startPoint[2])
        # xDoublePrimeStart = float(xPrime + k) * (width/(startPoint[2]*k))
        # yDoublePrime = float(yPrime + k) * (height/(startPoint[2]*k))
        startPoint[0] = float(xPrimeStart + k) * (width/(2*k))
        startPoint[1] = float(yPrimeStart + k) * (height/(2*k))
        xPrimeEnd = float(endPoint[0])/abs(endPoint[2])
        yPrimeEnd = float(endPoint[1])/abs(endPoint[2])
     
        
        endPoint[0] = float(xPrimeEnd + k) * (width/(2*k))
        endPoint[1] = float(yPrimeEnd + k) * (height/(2*k))
                                          
    line(startPoint[0], height-startPoint[1], endPoint[0], height-endPoint[1])
    vertexList = []


def multiplyVector(matrix, vect):
    result = []
    for num in range(4):
        result.append(matrix[num][0]*vect[0] + matrix[num][1]*vect[1] + matrix[num][2]*vect[2] + matrix[num][3]*vect[3])

    return result

def gtBeginShape():
    global vertexList
    vertexList = []

def gtEndShape():
    global vertexList
    vertexList = []
