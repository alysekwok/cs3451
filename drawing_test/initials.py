# The routine below should draw your initials in perspective

from matrix_stack import *
from drawlib import *

def persp_initials():
    gtInitialize()
    gtPerspective(100,-100,100)
    gtPushMatrix()
    gtTranslate(-.7, .2, -4) 
    gtBeginShape()

    #A
    gtVertex( .5,  1.0,  .8)
    gtVertex( .5,  0,  .8)

    gtVertex( .5,  1.0,  .8)
    gtVertex( -1,  0,  .8)
    
    gtVertex(.07,  .7,  .8)
    gtVertex(.50,  .7,  .8)
    
    #K
    gtVertex(.7, 1.0, .8)
    gtVertex(.7, 0, .8)
    
    gtVertex(1, 1.0, .8)
    gtVertex(.7, 0.7, .8)
    
    gtVertex(.7, 0.7, .8)
    gtVertex(2, 0, .8)

    
