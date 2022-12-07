# This is the provided code for the ray tracing project.
#
# The most important part of this code is the command interpreter, which
# parses the scene description (.cli) files.

from __future__ import division
import traceback
import math
debug_flag = False   # print debug information when this is True

# global variables
global backgroundColor
global fov
global currMaterial
global eyePos

# lists:
lightSources = []
shapes = []
vertices = []
global uvw
class PVector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "PVector(%f, %f, %f)" % (self.x, self.y, self.z)

    def __add__(self, other):
        return PVector.add(self, other)

    def __mul__(self, n):
        return PVector.mult(self, n)

    def __rmul__(self, n):
        return PVector.mult(self, n)

    def mag(self):
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def magSq(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def copy(self):
        return PVector(self.x, self.y, self.z)

    def div(self, n):
        return PVector(
            a.x / n,
            a.y / n,
            a.z / n,
        )

    @staticmethod
    def dist(a, b):
        return PVector.sub(a, b).mag()

    @staticmethod
    def add(a, b):
        return PVector(
            a.x + b.x,
            a.y + b.y,
            a.z + b.z,
        )

    @staticmethod
    def sub(a, b):
        return PVector(
            a.x - b.x,
            a.y - b.y,
            a.z - b.z,
        )

    @staticmethod
    def mult(a, n):
        return PVector(
            n * a.x,
            n * a.y,
            n * a.z,
        )

    @staticmethod
    def pairwise_mult(a, b):
        return PVector(
            a.x * b.x,
            a.y * b.y,
            a.z * b.z,
        )

    @staticmethod
    def dot(a, b):
        return a.x * b.x + a.y * b.y + a.z * b.z

    @staticmethod
    def cross(a, b):
        return PVector(
            a.y * b.z - a.z * b.y,
            a.z * b.x - a.x * b.z,
            a.x * b.y - a.y * b.x,
        )

    def normalize(self):
        mag = sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
        self.x /= mag
        self.y /= mag
        self.z /= mag
        return self
    
class Light:
    def __init__(self, position, col):
        self.position = position
        self.col = col

class Sphere:
    def __init__(self, center, radius, surface):
        self.center = center
        self.radius = radius
        self.surface = surface
        self.normVector = PVector(0, 0, 0)
    
    def __repr__(self):
        return "Sphere(center=%s, radius=%f, normal=%s, surface=%s)" % (self.center, self.radius, self.normVector, self.surface)
    
    def intersect(self, ray):
        origin = ray.origin
        center = self.center
        r = self.radius
        # u = [origin[0] - center[0], origin[1] - center[1], origin[2] - center[2]]
        u = PVector(origin.x - center.x, origin.y - center.y, origin.z - center.z)
        dx = ray.direction.x
        dy = ray.direction.y
        dz = ray.direction.z
        ux = u.x
        uy = u.y
        uz = u.z
        a = (dx * dx) + (dy * dy) + (dz * dz)
        b = (2 * dx * ux) + (2 * dy * uy) + (2 * dz * uz)
        c = (ux * ux) + (uy * uy) + (uz * uz) - (r * r)
        tPlus = -1
        tMinus = -1


        if (-b - sqrt((b*b)-(4 * a * c)))/(2*a) > 0:
            tPlus = (-b - sqrt((b*b)-(4 * a * c)))/(2*a)
        if (-b + sqrt((b*b)-(4 * a * c)))/(2*a) > 0:
            tMinus = (-b + sqrt((b*b)-(4 * a * c)))/(2*a)
        
        # if debug_flag:
            # print "testing intersection with the sphere whose color is ", self.surface.diffusergb # change these variable names to match the rest of your code!
            # print "a, b, c coefficients of the quadratic: ", a, b, c
        
    
        if tMinus > 0.00001 and tPlus > 0.00001:
            t = min(tPlus, tMinus)
        elif tMinus > 0.00001 and tPlus < 0.00001:
            t = tMinus
        elif tMinus < 0.00001 and tPlus > 0.00001:
            t = tPlus
        else:
            return 1000000000000
        intersectionPoint = PVector.add(ray.origin, PVector.mult(ray.direction, t))
        normVector = PVector.sub(intersectionPoint,self.center).normalize()
        self.normVector = normVector
        return t
        
    def getIntersectionPoint(self, ray, t):
        return PVector.add(ray.origin, PVector.mult(ray.direction, t))


class Material:
    def __init__(self, dr, dg, db, ar, ag, ab, sr, sg, sb, specularPower, kRefl):
        self.diffusergb = PVector(dr, dg, db)
        self.ambientrgb = PVector(ar, ag, ab)
        self.specularrgb = PVector(sr, sg, sb)

        self.specularPower = specularPower
        self.kRefl = kRefl
        
    def __repr__(self):
        return "Material(diffuse=%s, ambient=%s, specular=%s, specularPower=%f, kRefl=%f)" % (self.diffusergb, self.ambientrgb, self.specularrgb, self.specularPower, self.kRefl)
   

class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
        
        
class Hit:
    def __init__(self, tShape, normVector, tVal, intersectPoint):
        self.tShape = tShape
        self.normVector = normVector
        self.tVal = tVal
        self.intersectPoint = intersectPoint
    
    def __repr__(self):
        return "Hit(t=%f, intersection_point=%s, intersected_shape=%s, normal=%s)" % (self.tVal, self.intersectPoint, self.tShape, self.normVector)
        
class Triangle:
    def __init__(self, a, b, c, surface):
        self.a = a
        self.b = b
        self.c = c
    
        self.ab = PVector.sub(b, a) # precompute the sides of the triangle
        self.bc = PVector.sub(c, b)
        self.ca = PVector.sub(a, c)
        triangleVector = PVector.cross(self.ab, self.bc)
        self.normVector = triangleVector.normalize()
        
    
        self.surface = surface
    
    def intersect(self, ray):
        # if debug_flag:
        #     print "testing intersection with triangle whose color is ", self.surface.diffusergb
        tVal = 1000000000000
        if PVector.dot(self.normVector, ray.direction) > 0:
            self.normVector = PVector.mult(self.normVector, -1)
        denom = PVector.dot(self.normVector, ray.direction)
        if denom == 0:
            # if debug_flag:
            #     print "no intersection! denom is 0"
            return tVal
    
        # if denom > 0:
        #     self.normVector = PVector.mult(self.normVector, -1)
        t = (PVector.dot(PVector.sub(self.b, ray.origin),self.normVector)) / denom
     
        # if debug_flag:
        #     print "ray direction: ", ray.direction
        #     print "normal vector: ", self.normVector
        #     print "plane intersects at at t=%f" % t
        if t < 0:
            # if debug_flag:
            #     print "t is negative! no intersection"
            return tVal
        # calculate intersection point using ray equation and t-value
        # p = ray.origin + t * ray.direction
        p = PVector.add(PVector.mult(ray.direction, t), ray.origin)

        # triple1 = ((p - self.a) * (b - self.a)) x self.normVector # dot product
        triple1 = PVector.dot(PVector.cross(self.ab, PVector.sub(self.a, p)), self.normVector)
        # triple2 = ((p - self.b) * (c - self.b)) x self.normVector # surface normal
        triple2 = PVector.dot(PVector.cross(self.bc, PVector.sub(self.b, p)), self.normVector)
        # triple3 = ((p - self.c) * (a - self.c)) x self.normVector # cross product
        triple3 = PVector.dot(PVector.cross(self.ca, PVector.sub(self.c, p)), self.normVector)
        # if debug_flag:
        #     print "p: ", p
        #     print "triple 1: ", triple1
        #     print "triple 2: ", triple2
        #     print "triple 3: ", triple3
       
        
        if (triple1 > -0.00001) == (triple2 > -0.00001) == (triple3  > -0.00001):
            return t
        else:
            # if debug_flag:
            #     print "a, b, and c don't all have the same sign. no intersection"
            return tVal
        
    def getIntersectionPoint(self, ray, t):
        return PVector.add(ray.origin, PVector.mult(ray.direction, t))
        

def setup():
    size(320, 320) 
    noStroke()
    colorMode(RGB, 1.0)  # Processing color values will be in [0, 1]  (not 255)
    background(0, 0, 0)
    frameRate(30)

# make sure proper error messages get reported when handling key presses
def keyPressed():
    try:
        handleKeyPressed()
    except Exception:
        traceback.print_exc()

# read and interpret a scene description .cli file based on which key has been pressed
def handleKeyPressed():
    if key == '1':
        interpreter("01_one_sphere.cli")
    elif key == '2':
        interpreter("02_three_spheres.cli")
    elif key == '3':
        interpreter("03_shiny_sphere.cli")
    elif key == '4':
        interpreter("04_many_spheres.cli")
    elif key == '5':
        interpreter("05_one_triangle.cli")
    elif key == '6':
        interpreter("06_icosahedron_and_sphere.cli")
    elif key == '7':
        interpreter("07_colorful_lights.cli")
    elif key == '8':
        interpreter("08_reflective_sphere.cli")
    elif key == '9':
        interpreter("09_mirror_spheres.cli")
    elif key == '0':
        interpreter("10_reflections_in_reflections.cli")
    elif key == "-":
        interpreter("11_star.cli")

# You should add code for each command that calls routines that you write.
# Some of the commands will not be used until Part B of this project.
def interpreter(fname):
    global backgroundColor, eyePos, fov, uvw, currMaterial, lightSources, shapes, vertices
    reset_scene()  # you should initialize any data structures that you will use here
    
    fname = "data/" + fname
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # parse the lines in the file in turn
    for line in lines:
        words = line.split()  # split up the line into individual tokens
        if len(words) == 0:   # skip empty lines
            continue
        if words[0] == 'sphere':
            x = float(words[2])
            y = float(words[3])
            z = float(words[4])
            radius = float(words[1])
            # center = [x, y, z]
            center = PVector(x, y, z)
            newSphere = Sphere(center, radius, currMaterial)
            shapes.append(newSphere)
 
        elif words[0] == 'fov':
            fov = float(words[1])
        elif words[0] == 'eye':
            x = float(words[1])
            y = float(words[2])
            z = float(words[3])
            eyePos = PVector(x, y, z)
 
        elif words[0] == 'uvw':
            u1 = float(words[1])
            u2 = float(words[2])
            u3 = float(words[3])
            u = PVector(u1, u2, u3)
            v1 = float(words[4])
            v2 = float(words[5])
            v3 = float(words[6])
            v = PVector(v1, v2, v3)
            w1 = float(words[7])
            w2 = float(words[8])
            w3 = float(words[9])
            w = PVector(w1, w2, w3)
            uvw = [u, v, w]

        elif words[0] == 'background':
            r = float(words[1])
            g = float(words[2])
            b = float(words[3])
            backgroundColor = PVector(r, g, b)
    
        elif words[0] == 'light':
            x = float(words[1])
            y = float(words[2])
            z = float(words[3])
            r = float(words[4])
            g = float(words[5])
            b = float(words[6])
            
            position = PVector(x, y, z)
            lightColor = PVector(r, g, b)
            lightSources.append(Light(position, lightColor))
            
        elif words[0] == 'surface':
            dr = float(words[1])
            dg = float(words[2])
            db = float(words[3])
            ar = float(words[4])
            ag = float(words[5])
            ab = float(words[6])
            sr = float(words[7])
            sg = float(words[8])
            sb = float(words[9])
            specularPower = float(words[10])
            kRefl = float(words[11])

            currMaterial = Material(dr, dg, db, ar, ag, ab, sr, sg, sb, specularPower, kRefl)
            
        elif words[0] == 'begin':
            vertices = []
        elif words[0] == 'vertex':
            x = float(words[1])
            y = float(words[2])
            z = float(words[3])
            vertices.append(PVector(x, y, z))
        elif words[0] == 'end':
            # append triangle object to list of shapes
            shapes.append(Triangle(vertices[0], vertices[1], vertices[2], currMaterial))
            
        elif words[0] == 'render':
            render_scene()    # render the scene (this is where most of the work happens)
        elif words[0] == '#':
            pass  # ignore lines that start with the comment symbol (pound-sign)
        else:
            print ("unknown command: " + word[0])

# render the ray tracing scene
def render_scene():
    global debug_flag, backgroundColor, eyePos, fov, uvw, lightSources, shapes

    counter = 0
    for j in range(height):
        for i in range(width):

            # Maybe set a debug flag to true for ONE pixel.
            # Have routines (like ray/sphere intersection)print extra information if this flag is set.
            debug_flag = False
            if i == 208 and j == 254:
                debug_flag = True

            # create an eye ray for pixel (i,j) and cast it into the scene
            d = 1 / (tan(radians(fov)/2))
            U = ((2 * i) / width) - 1
            V = ((2 * (height-j)) / height) - 1
            
            uu = PVector.mult(uvw[0], U)
            vv = PVector.mult(uvw[1], V)
            dw = PVector.mult(uvw[2], -d)
            rayDirection = PVector.add(dw, vv)
            rayDirection = PVector.add(rayDirection, uu)
            
            newRay = Ray(eyePos, rayDirection.normalize())
            hit = checkRayIntersect(newRay)

            if (hit != None):
                if debug_flag:
                    print "The hit with the smallest t value is ", hit
                
                rgb = shade(hit, newRay)
                set(i, j, color(rgb.x, rgb.y, rgb.z))
            else:
                set(i, j, color(backgroundColor.x, backgroundColor.y, backgroundColor.z))
                
    
# here you should reset any data structures that you will use for your scene (e.g. list of spheres)
def reset_scene():
    global shapes, uvw, eyePos, backgroundColor, lightSources
    shapes = []
    uvw = []
    eyePos = None
    backgroundColor = None
    lightSources = []
    
    
def checkRayIntersect(ray):
    global shapes
    currHit = None
    minT = 1000000000000
    for obj in shapes:
        t = obj.intersect(ray)
        if t > 0.00001 and t < minT:
            minT = t
            currHit = Hit(obj, obj.normVector, t, obj.getIntersectionPoint(ray, t))
            if debug_flag:
                    print "found a hit: ", currHit
 
    return currHit
            
def shade(hit, ray, counter = 0, max_depth = 10):
    if debug_flag:
        print "in shade, hit is", hit
    global fov, uvw
    r = 0
    g = 0
    b = 0
    offset = PVector.mult(hit.normVector, 0.00001)
    kRefl = hit.tShape.surface.kRefl
    if max_depth > 0 and kRefl > 0:
        reflectOrigin = PVector.add(hit.intersectPoint, offset)
        D = ray.direction.normalize()
        N = hit.normVector
        scalar = PVector.dot(N, PVector.mult(D, -1)) * 2
        reflectDirection = PVector.add(D, PVector.mult(N, scalar)).normalize()
        reflectRay = Ray(reflectOrigin, reflectDirection)
        reflectHit = checkRayIntersect(reflectRay)
        if reflectHit == None:
            reflectColor = PVector.mult(PVector(backgroundColor.x, backgroundColor.y, backgroundColor.z), kRefl)
        else:
            reflectColor = PVector.mult(shade(reflectHit, reflectRay, counter + 1, max_depth - 1), kRefl)
        r += reflectColor.x
        g += reflectColor.y
        b += reflectColor.z
        # if debug_flag:
        #     print "current hit is: ", hit
        #     print "reflection ray origin (should be the hit position slightly offset away from the surface): ", reflectRay.origin 
        #     print "R (reflection ray direction): ", reflectRay.direction
        #     print "reflection hit:", reflectHit
        #     print "reflected color:", reflectColor
        #     print "num recursive calls: ", counter
            # print "reflection contribution (k_refl * reflect_color):", reflect_contribution

    for light in lightSources:
        shadowTerm = 1
        shadowOrigin = PVector.add(hit.intersectPoint, offset)
        shadowDirection = PVector.mult(PVector.sub(hit.intersectPoint, light.position).normalize(), -1)
        shadowRay = Ray(shadowOrigin, shadowDirection)
        shadowHit = checkRayIntersect(shadowRay)
        distance = PVector.dist(light.position, hit.intersectPoint)
        if shadowHit != None and shadowHit.tVal < distance:
            shadowTerm = 0
        L = PVector.mult(PVector.sub(hit.intersectPoint, light.position), -1).normalize()
        nl = PVector.dot(L.normalize(), hit.normVector)
        D = ray.direction.normalize()
        H = (PVector.sub(L, D)).normalize()
        specularCoefficient = pow(max(0, PVector.dot(H, hit.normVector)), hit.tShape.surface.specularPower)
        # L = 
        # nl = PVector.dot(L.normalize(), hit.normVector)
        r += ((hit.tShape.surface.diffusergb.x * light.col.x * max(0, nl)) + (hit.tShape.surface.specularrgb.x * light.col.x * specularCoefficient)) * shadowTerm
        g += ((hit.tShape.surface.diffusergb.y * light.col.y * max(0, nl)) + (hit.tShape.surface.specularrgb.y * light.col.y * specularCoefficient)) * shadowTerm
        b += ((hit.tShape.surface.diffusergb.z * light.col.z * max(0, nl)) + (hit.tShape.surface.specularrgb.z * light.col.z * specularCoefficient)) * shadowTerm
    r += hit.tShape.surface.ambientrgb.x
    g += hit.tShape.surface.ambientrgb.y
    b += hit.tShape.surface.ambientrgb.z

     
    return PVector(r, g, b)



# prints mouse location clicks, for help debugging
def mousePressed():
    print ("You pressed the mouse at " + str(mouseX) + " " + str(mouseY))

# this function should remain empty for this assignment
def draw():
    pass

        # if debug_flag:
        #     print ""
        #     print "adding contribution from the light with position ", light.position
        #     # print "diffuse contribution: ", diffuse_contribution # from P3A
        #     print "L: ", L
        #     print "H: ", H
        #     print "specular coefficient: ", specularCoefficient
        #     # print "specular contribution: ", specular_contribution # light_color * surface_specular_color * specular_coefficient
        #     # print "total contribution from this light: ", PVector.add(diffuse_contribution, specular_contribution)
         #   print ""
        # if debug_flag:
        #     print "checking shadow for light with position: ", light.position
        #     print "hit position: ", hit.intersectPoint
        #     print "shadow ray origin (should be the hit position slightly offset away from the surface): ", shadowRay.origin 
        #     print "shadow ray direction: ", shadowRay.direction
        #     if shadowHit != None:
        #         print "tVal: ", shadowHit.tVal
        #     print "shadow hit: ", shadowHit
        #     print "distance from light to original hit:", distance
        #     print ""


    
        






         
