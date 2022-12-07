# Object Modeling Example Code

from __future__ import division
import traceback

time = 0   # time is used to move objects from one frame to another

def setup():
    size (800, 800, P3D)
    try:
        frameRate(120)       # this seems to be needed to make sure the scene draws properly
        perspective (60 * PI / 180, 1, 0.1, 1000)  # 60-degree field of view
    except Exception:
        traceback.print_exc()

def draw():
    try:
        
        global time
        time += 0.01
     
        camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  # position of the virtual camera

        background (200, 200, 255)  # clear screen and set background to light blue
        
        # set up the lights
        ambientLight(100, 100, 100);
        lightSpecular(100, 100, 100)
        directionalLight (100, 100, 100, -0.3, 0.5, -1)
        
        # set some of the surface properties
        noStroke()
        specular (180, 180, 180)
        shininess (15.0)
        
        pushMatrix()
        rotateY(time)
        
    
        # head
        fill (51, 153, 255)
        pushMatrix()
        translate (0, -21, 0)
        # translate (0, 8 * sin(4 * time), 0)  # move up and down
        sphereDetail(60)  # this controls how many polygons make up each sphere
        sphere(17)
        popMatrix()
        
        # white part of head
        fill (255, 255, 255)
        pushMatrix()
        translate (0, -18.5, 6)
        sphere(13)
        popMatrix()
        
        # left eye
        fill (255, 255, 255)
        pushMatrix()
        translate (-4, -24.5, 15)
        # translate (0, 8 * sin(4 * time), 0)  # move up and down
        # sphereDetail(60)  # this controls how many polygons make up each sphere
        sphere(4.5)
        popMatrix()
        
        # right eye
        fill (255, 255, 255)
        pushMatrix()
        translate (4, -24.5, 15)
        # translate (0, 8 * sin(4 * time), 0)  # move up and down
        # sphereDetail(60)  # this controls how many polygons make up each sphere
        sphere(4.5)
        popMatrix()
        
        # nose
        fill (255, 0, 0)
        pushMatrix()
        translate (0, -22, 18)
        # translate (0, 8 * sin(4 * time), 0)  # move up and down
        # sphereDetail(60)  # this controls how many polygons make up each sphere
        sphere(2.5)
        popMatrix()
        
        # left pupil
        fill (0, 0, 0)
        pushMatrix()
        translate (-2.5, -24.5, 19)
        # translate (0, 8 * sin(4 * time), 0)  # move up and down
        # sphereDetail(60)  # this controls how many polygons make up each sphere
        sphere(1)
        popMatrix()
        
        # right pupil
        fill (0, 0, 0)
        pushMatrix()
        translate (2.5, -24.5, 19)
        # translate (0, 8 * sin(4 * time), 0)  # move up and down
        # sphereDetail(60)  # this controls how many polygons make up each sphere
        sphere(1)
        popMatrix()
   
        
        # collar
        fill (255, 0, 0)
        pushMatrix()
        translate (0,-5.5, 0)
        rotateX(PI/2)
        scale (12.5, 13.5, 1.5)
        cylinder(20)
        popMatrix()
        
        # left top whisker
        fill(0, 0, 0)
        pushMatrix()
        translate(8, -20, 18)
        rotateX(PI/2)
        rotateY(PI/3)
        scale(0.3, 0.3, 4)
        cylinder()
        popMatrix()
        
        # right top whisker
        fill(0, 0, 0)
        pushMatrix()
        translate(-8.2, -20, 18)
        rotateX(PI/2)
        rotateY(-PI/3)
        scale(0.3, 0.3, 4)
        cylinder()
        popMatrix()
        
        # left middle whisker
        fill(0, 0, 0)
        pushMatrix()
        translate(8.2, -16.5, 18)
        rotateX(PI/2)
        rotateY(PI/2)
        scale(0.3, 0.3, 4)
        cylinder()
        popMatrix()
        
        # right middle whisker
        fill(0, 0, 0)
        pushMatrix()
        translate(-8, -16.5, 18)
        rotateX(PI/2)
        rotateY(PI/2)
        scale(0.3, 0.3, 4)
        cylinder()
        popMatrix()
        
        # left bottom whisker
        fill(0, 0, 0)
        pushMatrix()
        translate(8, -12.75, 17.5)
        rotateX(PI/2)
        rotateY(-PI/3)
        scale(0.3, 0.3, 4)
        cylinder()
        popMatrix()
        
        # right bottom whisker
        fill(0, 0, 0)
        pushMatrix()
        translate(-8, -12.75, 17.5)
        rotateX(PI/2)
        rotateY(PI/3)
        scale(0.3, 0.3, 4)
        cylinder()
        popMatrix()
        
        
        # bell on collar
        fill (255, 255, 0)
        pushMatrix()
        translate (0, -3.5, 13)
        sphere(2)
        popMatrix()
        
        # left arm
        fill (51, 153, 255)
        pushMatrix()
        translate (-10, -1.5, -1)
        rotateY(PI/2)
        rotateX(3*PI/4)
        scale (3, 3, 10)
        
        cylinder()
        popMatrix()
        
        # right arm
        fill (51, 153, 255)
        pushMatrix()
        translate (10, -2.5, -1)
        rotateY(PI/2)
        rotateX(3*PI/4)
        scale (3, 3, 10)

        cylinder()
        popMatrix()
        
        # left hand
        fill (255, 255, 255)
        pushMatrix()
        translate (-18, -9.5, -1)
        sphere(3.5)
        popMatrix()
        
        # right hand
        fill (255, 255, 255)
        pushMatrix()
        translate (18, 5.5, -1)
        sphere(3.5)
        popMatrix()
        
        # left leg
        fill (51, 153, 255)
        pushMatrix()
        translate (-6.5, 10, 0)
        # rotateX (-time)
        rotateX(PI/2)
        scale (5.5, 5.5, 7)
        cylinder()
        popMatrix()
        
        # right leg
        fill (51, 153, 255)
        pushMatrix()
        translate (6.5, 10, 0)
        # rotateX (-time)
        rotateX(PI/2)
        scale (5.5, 5.5, 7)
        cylinder()
        popMatrix()
        
        # left foot
        fill (255, 255, 255)
        pushMatrix()
        translate (-6.5, 17, 0)
        # rotateX (-time)
        rotateX(PI/2)
        # scale (7, 7.2, 2)
        sphere(5.5)
        popMatrix()
        
        # # right foot
        fill (255, 255, 255)
        pushMatrix()
        translate (6.5, 17, 0)
        # rotateX (-time)
        rotateX(PI/2)
        # scale (6.5, 7.2, 2)
        sphere(5.5)
        popMatrix()
        
        # white belly
        fill (255, 255, 255)
        pushMatrix()
        translate (0, 2, 3)
        sphere(10)
        popMatrix()

        # body
        fill (51, 153, 255)
        pushMatrix()
        translate(0, 3, 0)
        # strokeJoin(ROUND)
        # smooth()
        sphere(12)
        popMatrix()
        
        # tail
        fill(255, 0, 0)
        pushMatrix()
        translate(0, 9, -12)
        sphere(2)
        popMatrix()
        
        # fill (51, 153, 255)
        # pushMatrix()
        # translate (0, 3, 0)
        # # rotateX (-time)
        # rotateX(PI/2)
        # scale (12, 9, 8)
        # cylinder()
        # popMatrix()
   
        
        popMatrix()
    except Exception:
        traceback.print_exc()
        
 

# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 50):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # round main body
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2
        
# Draw a torus flat in the XY plane
def torus(radius=1.0, tube_radius=0.5, detail_x=16, detail_y=16):
    radius = float(radius)
    tube_radius = float(tube_radius)
    detail_x = int(detail_x)
    detail_y = int(detail_y)

    tube_ratio = (tube_radius / radius)

    def make_torus():
        vertices = []
        normals = []
        for torus_segment in range(detail_x):
            theta = 2 * PI * torus_segment / detail_x
            cos_theta = cos(theta)
            sin_theta = sin(theta)

            segment_vertices = []
            segment_normals = []

            for tube_segment in range(detail_y):
                phi = 2 * PI * tube_segment / detail_y
                cos_phi = cos(phi)
                sin_phi = sin(phi)
                segment_vertices.append(PVector(
                    cos_theta * (radius + cos_phi * tube_radius),
                    sin_theta * (radius + cos_phi * tube_radius),
                    sin_phi * tube_radius,
                ))
                segment_normals.append(PVector(
                    cos_phi * cos_theta,
                    cos_phi * sin_theta,
                    sin_phi,
                ))
            vertices.append(segment_vertices)
            normals.append(segment_normals)
        return vertices, normals

    global GEOMETRY_CACHE
    try:
        GEOMETRY_CACHE
    except NameError:
        GEOMETRY_CACHE = {}
    cache_index = ("torus", radius, tube_radius, detail_x, detail_y)
    if cache_index in GEOMETRY_CACHE:
        vertices, normals = GEOMETRY_CACHE[cache_index]

    else:
        vertices, normals = make_torus()
        GEOMETRY_CACHE[cache_index] = (vertices, normals)

    for i in range(detail_x):
        for j in range(detail_y):
            beginShape()

            normal(normals[i][j].x, normals[i][j].y, normals[i][j].z)
            vertex(vertices[i][j].x, vertices[i][j].y, vertices[i][j].z)
            normal(normals[(i + 1) % detail_x][j].x, normals[(i + 1) % detail_x][j].y, normals[(i + 1) % detail_x][j].z)
            vertex(vertices[(i + 1) % detail_x][j].x, vertices[(i + 1) % detail_x][j].y, vertices[(i + 1) % detail_x][j].z)
            normal(normals[(i + 1) % detail_x][(j + 1) % detail_y].x, normals[(i + 1) % detail_x][(j + 1) % detail_y].y, normals[(i + 1) % detail_x][(j + 1) % detail_y].z)
            vertex(vertices[(i + 1) % detail_x][(j + 1) % detail_y].x, vertices[(i + 1) % detail_x][(j + 1) % detail_y].y, vertices[(i + 1) % detail_x][(j + 1) % detail_y].z)
            normal(normals[i][(j + 1) % detail_y].x, normals[i][(j + 1) % detail_y].y, normals[i][(j + 1) % detail_y].z)
            vertex(vertices[i][(j + 1) % detail_y].x, vertices[i][(j + 1) % detail_y].y, vertices[i][(j + 1) % detail_y].z)

            endShape(CLOSE)
