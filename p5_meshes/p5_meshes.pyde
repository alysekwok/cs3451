# Provided code for Subdivison and Geodesic Spheres

from __future__ import division
import traceback

# parameters used for object rotation by mouse
mouseX_old = 0
mouseY_old = 0
rot_mat = PMatrix3D()
V = [] # V-table
G = [] # Geometry-table
O = {} # Opposite-table
currentCorner = 0
currentCornerVisible = False
showRandomColors = False


# initalize things
def setup():
    size (800, 800, OPENGL)
    frameRate(30)
    noStroke()

# draw the current mesh (you will modify parts of this routine)
def draw():
    global G, V, O, currentCorner, currentCornerVisible, showRandomColors
    randomSeed(0)
    background (100, 100, 180)    # clear the screen to black

    perspective (PI*0.2, 1.0, 0.01, 1000.0)
    camera (0, 0, 6, 0, 0, 0, 0, 1, 0)    # place the camera in the scene
    
    # create an ambient light source
    ambientLight (102, 102, 102)

    # create two directional light sources
    lightSpecular (202, 202, 202)
    directionalLight (100, 100, 100, -0.7, -0.7, -1)
    directionalLight (152, 152, 152, 0, 0, -1)
    
    pushMatrix();

    stroke (0)                    # draw polygons with black edges
    fill (200, 200, 200)          # set the polygon color to white
    ambient (200, 200, 200)
    specular (0, 0, 0)            # turn off specular highlights
    shininess (1.0)
    
    applyMatrix (rot_mat)   # rotate the object using the global rotation matrix

    # THIS IS WHERE YOU SHOULD DRAW YOUR MESH
    c = 0
    while c < len(V):
        beginShape()
        if showRandomColors:
            fill(random(255), random(255), random(255))
        else:
            fill(255, 255, 255)
        vertex(G[V[c]][0], G[V[c]][1], G[V[c]][2])
        vertex(G[V[c + 1]][0], G[V[c + 1]][1], G[V[c + 1]][2])
        vertex(G[V[c + 2]][0], G[V[c + 2]][1], G[V[c + 2]][2])
        endShape(CLOSE)
        c += 3
    if currentCornerVisible:
        pushMatrix()
        currentVertex = G[V[currentCorner]]
        
        next = nextCorner(currentCorner)
        prev = previousCorner(currentCorner)
        nextVertex = G[V[next]]
        previousVertex = G[V[prev]]
        
        weightedX = currentVertex[0] * 0.8 + nextVertex[0] * 0.1 + previousVertex[0] * 0.1
        weightedY = currentVertex[1] * 0.8 + nextVertex[1] * 0.1 + previousVertex[1] * 0.1
        weightedZ = currentVertex[2] * 0.8 + nextVertex[2] * 0.1 + previousVertex[2] * 0.1

        translate(weightedX, weightedY, weightedZ)
        noStroke()
        fill(255, 10, 0)
        sphere(0.05)
        popMatrix()
    
    popMatrix()

# read in a mesh file (this needs to be modified)
def read_mesh(filename):
    global G, V, O, currentCorner, currentCornerVisible, showRandomColors

    fname = "data/" + filename
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # determine number of vertices (on first line)
    words = lines[0].split()
    num_vertices = int(words[1])
    print "number of vertices =", num_vertices

    # determine number of faces (on first second)
    words = lines[1].split()
    num_faces = int(words[1])
    print "number of faces =", num_faces

    # read in the vertices
    for i in range(num_vertices):
        words = lines[i+2].split()
        x = float(words[0])
        y = float(words[1])
        z = float(words[2])
        print "vertex: ", x, y, z
        # update G by appending (x, y, z)
        G.append([x, y, z])

    # read in the faces
    for i in range(num_faces):
        j = i + num_vertices + 2
        words = lines[j].split()
        nverts = int(words[0])
        if (nverts != 3):
            print "error: this face is not a triangle"
            exit()

        index1 = int(words[1])
        index2 = int(words[2])
        index3 = int(words[3])
        print "triangle: ", index1, index2, index3
        # update V by extending it by (index1, index2, index3)
        V = V + [index1, index2, index3]
    # instantiate O table by called computeOTable(G,V)
    computeOTable(G, V)
    print_mesh()

# make sure proper error messages get reported when handling key presses
def keyPressed():
    try:
        handleKeyPressed()
    except Exception:
        traceback.print_exc()

# process key presses (call your own routines!)
def handleKeyPressed():
    global G, V, O, currentCorner, currentCornerVisible, showRandomColors

    if key == '1':
        G = []
        V = []
        O = {}
        read_mesh ('tetra.ply')
    elif key == '2':
        G = []
        V = []
        O = {}
        read_mesh ('octa.ply')
    elif key == '3':
        G = []
        V = []
        O = {}
        read_mesh ('icos.ply')
    elif key == '4':
        G = []
        V = []
        O = {}
        read_mesh ('star.ply')
    elif key == 'n': # next
        currentCorner = nextCorner(currentCorner)
    elif key == 'p': # previous
        currentCorner = previousCorner(currentCorner)
    elif key == 'o': # opposite
        currentCorner = oppositeCorner(currentCorner)
    elif key == 's': # swing
        currentCorner = swingCorner(currentCorner)
    elif key == 'd': # subdivide mesh
        result = subdivide()
        G = result[0]
        V = result[1]
        print(result)
        print_mesh()
    elif key == 'i': # inflate mesh
        G = inflate()
    elif key == 'r': # toggle random colors
        if showRandomColors != True:
            showRandomColors = True
        else:
            showRandomColors = False
    elif key == 'c': # toggle showing current corner
        if currentCornerVisible != True:
            currentCornerVisible = True
        else:
            currentCornerVisible = False
    elif key == 'q': # quit the program
        exit()

# remember where the user first clicked
def mousePressed():
    global mouseX_old, mouseY_old
    mouseX_old = mouseX
    mouseY_old = mouseY

# change the object rotation matrix while the mouse is being dragged
def mouseDragged():
    global rot_mat
    global mouseX_old, mouseY_old
    
    if (not mousePressed):
        return
    
    dx = mouseX - mouseX_old
    dy = mouseY - mouseY_old
    dy *= -1

    len = sqrt (dx*dx + dy*dy)
    if (len == 0):
        len = 1
    
    dx /= len
    dy /= len
    rmat = PMatrix3D()
    rmat.rotate (len * 0.005, dy, dx, 0)
    rot_mat.preApply (rmat)

    mouseX_old = mouseX
    mouseY_old = mouseY

def nextCorner(cornerNum):
    triangleNum = cornerNum // 3
    # find triangle number based on cornerNum
    return 3 * triangleNum + ((cornerNum + 1) % 3)

def previousCorner(cornerNum):
    triangleNum = cornerNum // 3
    return 3 * triangleNum + ((cornerNum - 1) % 3)

def oppositeCorner(cornerNum):
    global O
    # use opposite table dictionary
    return O[cornerNum]

def swingCorner(cornerNum):
    return nextCorner(oppositeCorner(nextCorner(cornerNum)))


def computeOTable(G, V):
    # temp variable to store triplets
    triplets = []
    for i in range(len(V)):
        triplets.append([min(V[nextCorner(i)], V[previousCorner(i)]), max(V[nextCorner(i)], V[previousCorner(i)]), i])
    # sort the triplets (see slide 8)
    sortedTriplets = sorted(triplets)
    j = 0
    while j < len(sortedTriplets): # (add 2 to iterator each time)
        cornerA = sortedTriplets[j][2]
        cornerB = sortedTriplets[j+1][2]
        # assign O[cornerA] = cornerB and vice versa
        O[cornerA] = cornerB
        O[cornerB] = cornerA
        j += 2


def inflate():
    global G
    normalizedG = []
    for arr in G:
        magnitude = sqrt((arr[0] * arr[0]) + (arr[1] * arr[1]) + (arr[2] * arr[2]))
        normalizedG.append([arr[0]/magnitude, arr[1]/magnitude, arr[2]/magnitude])
    return normalizedG
        
        
    # normalize each array in G and return this new normalized version
    # the in keyPressed section, when the inflate key is pressed, update G table by calling this function
    pass

def subdivide():
    global G, V, O, currentCorner, currentCornerVisible, showRandomColors
    numEdges = len(V) // 2
    newGTable = []
    for val in G:
        newGTable.append(val)
        print("g-table val: ", val)
    newVTable = []
    midpoints = {}
    for a,b in O.items():
        endpoint1 = [G[V[previousCorner(a)]][0], G[V[previousCorner(a)]][1], G[V[previousCorner(a)]][2]]
        endpoint2 = [G[V[nextCorner(a)]][0], G[V[nextCorner(a)]][1], G[V[nextCorner(a)]][2]]
        midpoint = [(endpoint1[0] + endpoint2[0])/2, (endpoint1[1] + endpoint2[1])/2, (endpoint1[2] + endpoint2[2])/2]
        midpointIndex = len(newGTable)
        newGTable.append(midpoint)
        midpoints[a] = midpointIndex
        midpoints[b] = midpointIndex
    x = 0
    while x < len(V):
        y = x + 1
        z = x + 2
        newVTable.extend([V[x], midpoints[z], midpoints[y]])
        newVTable.extend([midpoints[z], V[y], midpoints[x]])
        newVTable.extend([midpoints[y], midpoints[x], V[z]])
        newVTable.extend([midpoints[x], midpoints[y], midpoints[z]])
        x += 3

    return newGTable, newVTable, computeOTable(newGTable, newVTable)
        

def print_mesh():
    print "Vertex table (maps corner num to vertex num):"
    print "corner num\tvertex num:"
    for c, v in enumerate(V):
        print c, "\t\t", v
    print ""
    
    print "Opposite table (maps corner num to opposite corner num):"
    print "corner num\topposite corner num"
    for c, o in O.iteritems():
        print c, "\t\t", o
    print ""
    
    print "Geometry table (maps vertex num to position): "
    print "vertex num\tposition:"
    for v, g in enumerate(G):
        print v, "\t\t", g
    print ""

  
    print ""
    print "" 

        
    

    
