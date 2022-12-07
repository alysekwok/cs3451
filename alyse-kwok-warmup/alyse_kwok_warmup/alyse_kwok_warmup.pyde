def setup():
    size(600, 600) # set size of screen
    rectMode(CENTER)

def draw():
    background(255, 255, 255) # set background color to white
    noStroke() # do not draw shape outlines
    fill(0, 0, 0) # fill with black color
    # draw center rectangle
    x = height/2
    y = width/2
    sideLength = height/3
    rect(x, y, sideLength, sideLength)
    offset = mouseX - width/2
   
    helper(x, y, sideLength, offset, 4)
    

def helper(parentX, parentY, parentLen, offset, count):
    if count == 0:
        return 
    else:
        k = 2.0 * float((600.0-mouseY)/600.0)
        count = count - 1 
        currLength = (parentLen /4)
        currOffset = parentLen/2
        
        square1x = parentX + offset
        square2x = parentX + currOffset + (k* currLength)
        square3x = parentX - offset
        square4x = parentX - currOffset - (k* currLength)
        
        square1y = parentY - currOffset - (k* currLength)
        square2y = parentY + offset
        square3y = parentY + currOffset + (k* currLength)
        square4y = parentY - offset
        
        
        rectSize = currOffset * k
        fill(204, 102, 0)
        rect(square1x, square1y, rectSize, rectSize)
        fill(102, 204, 0)
        rect(square2x, square2y, rectSize, rectSize)
        fill(0, 102, 204)
        rect(square3x, square3y, rectSize, rectSize)
        fill(0, 204, 102)
        rect(square4x, square4y, rectSize, rectSize)
        
        helper(square1x, square1y, rectSize, k * offset/2, count)
        helper(square2x, square2y, rectSize, k * offset/2, count)
        helper(square3x, square3y, rectSize, k * offset/2, count)
        helper(square4x, square4y, rectSize, k * offset/2, count)
        
        # rect(parentX + offset, parentY - offset - (parentLen/4), currLength, currLength) # (s, t)
        # rect(600-currY, currX + offset, currLength, currLength) # (t, -s)
        # rect(currY, currX - offset, currLength, currLength) # (-s, -t)
        # rect(currX - offset, 600-currY, currLength, currLength) # (-t, s)
        
        # helper(parentX + offset, parentY - offset - (parentLen/4), currLength, currOffset/2, count)
        # helper(currY, currX - offset, currLength, currOffset/2, count)
        # helper(currY, currX - offset, currLength, currOffset/2, count)
        # helper(currX - offset, 600-currY, currLength, currOffset/2, count)
    
    
    # helper(currX, currY, currLength, currOffset, count)
    # helper(currY, currX, currLength, offset/2, count)
    # helper(600-currY, currX, currLength, offset/2, count)
    # helper(currX, 600-currY, currLength, offset/2, count)

    # currLen = sideLength * factorK
    # offset = mouseX - width/2
    # rect((width/2), 150, (sideLength/2), (sideLength/2)) # (s, t)
    # rect(600-(width/2), 450, (sideLength/2), (sideLength/2)) # (-s, -t)
    # rect(450, 600- (width/2), (sideLength/2), (sideLength/2)) # (t, -s)
    # rect(150, (width/2), (sideLength/2), (sideLength/2)) # (-t, s)
    # draw smaller rectangles to be controlled by mouse
    # controlled by mouseY
    
