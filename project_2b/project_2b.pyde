time = 0

# I am replicating the clouds using object instancing

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
        camera (0, 0, 150, 0, 0, 0, 0,  1, 0)  # position of the virtual camera

        background (205, 232, 247)  # clear screen and set background to light blue
        
        if time <= 2:
            camera(0, 0, 150 - 40* time, 0, 0, 0, 0, 1, 0)
        # walking
        if time > 2 and time <= 5.5:
            camera(10 * (time-2), 0, 70, time * 5, 0, 0, 0, 1, 0)
        # delay for wings to sprout
        if time > 5.5 and time < 6 :
            camera(10 * (5.5-2), 0, 70 , 27.5, 0, 0, 0, 1, 0)
        # pan up and zoom out for flying
        if time >= 6 and time < 7:
            camera((35) - (35*(time - 6)), 0, 70 + (time-6) * 50, 27.5 - (27.5*(time-6)), -(time-6) * 5, 0, 0, 1, 0)
        if time >= 7 and time < 8:
            camera(0, 0, 120, 0 ,-5, 0, 0, 1, 0)
        if time >= 8 and time <= 13:
            camera((time-8) * 3, -(time-8) * 4, 120 -((time-8) * 6), (time-8) * 3, -5 + (time-8) * -2 , 0, 0, 1, 0)
            # camera(100 * cos(time-8), 0, 100 * sin(time-8), -10 ,-10, 0, 0, 1, 0)
            # camera(80 * cos(time-6), 0, 80 * sin(1 + (time-6)), 25, 0, 0, 0, 1, 0)
        if time > 13:
            camera(15, -20, 90, 15, -15, 0, 0, 1, 0)
        if time >= 15:
            time = 0
        # set up the lights
        ambientLight(100, 100, 100);
        lightSpecular(50, 50, 50)
        directionalLight (150, 150, 150, -0.3, 0.5, -1)
        
        # set some of the surface properties
        noStroke()
        specular (180, 180, 180)
        shininess (15.0)
        
        fill(50, 168, 82)
        pushMatrix()
        translate(0, 37, 0)
        scale(10,1,8)
        box(50)
        popMatrix()
        
        pushMatrix()
        translate(0, 1, 0)
        scale(0.5, 0.5, 0.5)
        if time > 2 and time <= 3:
            rotateY((time-2)*PI/2)
            translate(0, 1, time * 10)

        if time <=5 and time > 3:
            rotateY(PI/2)
            translate(0, 1, time * 10)
        if time > 5 and time < 5.5:
            rotateY(PI/2)
            translate(0, 1, 50)
        if time >= 5.5 and time < 6.5:
            rotateY(PI/2)
            translate((time - 5.5) * 30, (-(time - 5.5) * 50) + 1, 50)
        if time >= 6.5 and time < 7.5:
            rotateY(PI/2)
            rotateY(-(time-6.5)*PI/2)
            translate(30, -51, 50)
        if time > 7.5:
            translate(30, -51, 50)
            # rotateY(PI/2)
            # rotateX(11*PI/6)
            # translate((time-6.5) * 15, -(time-6.5) * 10, 0)
            # rotateZ(sin(10.25-5)/6)
        # if time >= 10.25 and time < 15:
            # rotateY(PI/2)
            # rotateX(11*PI/6)
            # translate((10.75-5) * 15, -(10.75-5) * 50, 0)
            # rotateX((PI/6) *time)
            # rotateY((PI/4)*time)
        if time >= 15:
            time =0
        
        doraemon()
        popMatrix()
        
        pushMatrix()
        cloud(-10 + (time * -3), -30, 10)
        cloud(10 + (time * -2), -25, -8)
        cloud(50 + (time * 5), -10, 20)
        cloud(-50 + (time * 1), -10, -5)
        cloud(30 + (time * 1.5), -1, -15)
        cloud(-70 + (time * -4), -35, 0)
        cloud(70 + (time * 2), -20, -10)
        cloud(-15 + (time * -1.5), -15, -20)
        popMatrix()
        
    except Exception:
        traceback.print_exc()
    

def cloud(x, y, z):
    pushMatrix()
    fill(255, 255, 255)
    pushMatrix()
    translate(x, y, z)
    sphere(2)
    popMatrix()
    
    fill(255, 255, 255)
    pushMatrix()
    translate(x-2, y, z)
    sphere(2.5)
    popMatrix()
    
    fill(255, 255, 255)
    pushMatrix()
    translate(x-5, y, z)
    sphere(3)
    popMatrix()
    
    fill(255, 255, 255)
    pushMatrix()
    translate(x-7, y, z)
    sphere(2.5)
    popMatrix()
    
    fill(255, 255, 255)
    pushMatrix()
    translate(x-9, y, z)
    sphere(2)
    popMatrix()
    
    fill(255, 255, 255)
    pushMatrix()
    translate(x-6, y-2.5, z)
    sphere(2)
    popMatrix()
    
    fill(255, 255, 255)
    pushMatrix()
    translate(x-3, y-2.5, z)
    sphere(2)
    popMatrix()
    
    fill(255, 255, 255)
    pushMatrix()
    translate(x-4, y-3.5, z)
    sphere(2)
    popMatrix()
    
    popMatrix()
    


def doraemon():
    
    global time
    
    head()
        
    # bell on collar
    fill (255, 255, 0)
    pushMatrix()
    translate (0, -3.5, 13)
    sphere(2)
    popMatrix()
    
    pushMatrix()
    if time < 5:
        translate(0, 10, 0)
    if time >= 5 and time < 6:
        translate(0, time/33*2, 0)
    # if time >= 5.5:
    #     translate(0, 5.5*3, 0)
    wings()
    popMatrix()
    
    if time < 5:
        pushMatrix()
        arms(0)
        popMatrix()
    if time >= 5 and time < 13:
        pushMatrix()
        arms(1)
        popMatrix()
    if time >= 13:
        pushMatrix()
        arms(2)
        popMatrix()
    
    pushMatrix()
    if time > 2 and time < 5:
        rotateX(-sin(time * 8)/2)
    leg(-6.5, 10)
    popMatrix()
    
    pushMatrix()
    if time > 2 and time < 5:
        rotateX(sin(time * 8)/2)
    leg(6.5, 10)
    popMatrix()
    
    pushMatrix()
    body()
    popMatrix()
    

 
# except Exception:
#     traceback.print_exc()

def wings():
    
    # pushMatrix()
    
    fill(255, 230, 5)
    pushMatrix()
    translate(0, -33, 0)
    rotateX(PI/2)
    scale(0.5, 0.5, 10)
    cylinder()
    popMatrix()
    
    fill(255, 230, 5)
    pushMatrix()
    translate(0, -42, -2)
    rotateX(-PI/2)
    
    scale(2, 2, 2)
    rotateZ(sin(50*time))
    cone()
    popMatrix()
    
    fill(255, 230, 5)
    pushMatrix()
    translate(0, -42, 2)
    rotateX(PI/2)
    
    scale(2, 2, 2)
    rotateZ(-sin(50*time))
    cone()
    popMatrix()
    
def arms(mode):
    
    # both arms down
    if mode == 0:
        # left arm
        fill (51, 153, 255)
        pushMatrix()
        translate (-10, -1.5, -1)
        rotateY(PI/2)
        rotateX(5*PI/4)
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
        translate (-18, 6.5, -1)
        sphere(3.5)
        popMatrix()
        
        # right hand
        fill (255, 255, 255)
        pushMatrix()
        translate (18, 5.5, -1)
        sphere(3.5)
        popMatrix()
        
    
    # one arm up
    if mode == 1:
        # left arm
        fill (51, 153, 255)
        pushMatrix()
        
        
        translate (-10, -1.5, -1)
        rotateY(PI/2)
        # if time > 5.5 and time < 6:
        #     rotateX((time-5.5) * 3 * PI/4)
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
        # old position: translate (-18, 6.5, -1)
        # if time > 5.5 and time < 6:
        #     translate(-18, 6.5 + (time - 5.5) * -32, -1)
        translate (-18, -9.5, -1)
        sphere(3.5)
        popMatrix()
        
        # right hand
        fill (255, 255, 255)
        pushMatrix()
        translate(18, 5.5, -1)
        sphere(3.5)
        popMatrix()
    
    # waving left arm
    if mode == 2:
        # left arm
        fill (51, 153, 255)
        pushMatrix()
        rotateY(-cos(time * 8)/5)
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
        rotateY(-cos(time * 8)/5)
        translate (-18, -9.5, -1)
        
        sphere(3.5)
        popMatrix()
        
        # right hand
        fill (255, 255, 255)
        pushMatrix()
        
        translate (18, 5.5, -1)
        sphere(3.5)
        popMatrix()
        

def leg(x, y):
    # distance from leg to foot is 7
    

    fill (51, 153, 255)
    pushMatrix()
    translate (x, y, 0)
    rotateX(PI/2)
    scale (5.5, 5.5, 7)
    cylinder()
    popMatrix()
    

    fill (255, 255, 255)
    pushMatrix()
    translate (x, y+7, 0)
    rotateX(PI/2)
    sphere(5.5)
    popMatrix()
    

def body():
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
    sphere(12)
    popMatrix()
    
    # tail
    fill(255, 0, 0)
    pushMatrix()
    translate(0, 9, -12)
    sphere(2)
    popMatrix()

def head():
    # head
    fill (51, 153, 255)
    pushMatrix()
    translate (0, -21, 0)
    sphereDetail(60)  
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
    sphere(4.5)
    popMatrix()
        
    # right eye
    fill (255, 255, 255)
    pushMatrix()
    translate (4, -24.5, 15)
    sphere(4.5)
    popMatrix()
    
    # nose
    fill (255, 0, 0)
    pushMatrix()
    translate (0, -22, 18)
    sphere(2.5)
    popMatrix()
        
    # left pupil
    fill (0, 0, 0)
    pushMatrix()
    translate (-2.5, -24.5, 19)
    sphere(1)
    popMatrix()
    
    # right pupil
    fill (0, 0, 0)
    pushMatrix()
    translate (2.5, -24.5, 19)
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

# Draw a cone pointing in the -y direction (up), with radius 1, with y in range [-1, 1]
def cone(sides=50):
    sides = int(sides)

    # draw triangles making up the sides of the cone
    for i in range(sides):
        theta = 2.0 * PI * i / sides
        theta_next = 2.0 * PI * (i + 1) / sides
        
        beginShape()
        normal(cos(theta), 0.6, sin(theta))
        vertex(cos(theta), 1.0, sin(theta))
        normal(cos(theta_next), 0.6, sin(theta_next))
        vertex(cos(theta_next), 1.0, sin(theta_next))
        normal(0.0, -1.0, 0.0)
        vertex(0.0, -1.0, 0.0)
        endShape()

    # draw the cap of the cone
    beginShape()
    for i in range(sides):
        theta = 2.0 * PI * i / sides
        vertex(cos(theta), 1.0, sin(theta))
    endShape()
        
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
