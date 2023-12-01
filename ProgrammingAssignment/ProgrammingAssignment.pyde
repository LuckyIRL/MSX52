models = []

def setup():
    global models
    fullScreen()
    size(1000, 1000, P3D)
    colorMode(HSB)
    
    car52_model = Model("CarModel52.obj",width/2, height/2, -5000, 10, 250) 
    models.append(car52_model)
    
    car52_model2 = Model2("CarModel52.obj",-500, 1000, 10, 10, 250) 
    models.append(car52_model2)
    
    car52_model3 = Model3("CarModel52.obj",4000, 300, 40, 5, 200)
    models.append(car52_model3)
    
    for i in  range(1):
        msx_model = MSX_Model("msx.obj",width/2,height/2,1700,10,150)
        models.append(msx_model)

def draw():
    global models
    
    pushMatrix()
    colorMode(RGB)
    blendMode(SUBTRACT)
    fill(255, 8)
    rect(0, 0, width*2, height*2)
    blendMode(BLEND)
    colorMode(HSB)
    #background(0)
    lights()
    strokeWeight(4)
    #translate(width/4, height/4, 100 ) #centre of screen
                    
    # Callint the render method on the cube
        
    for car52_model in models:
        car52_model.render()

    for car52_model2 in models:
        car52_model2.render()
        
    for car52_model3 in models:
        car52_model3.render()
    fill(255, 2)
    for msx_model in models:
        msx_model.render()
    popMatrix()
        
# A class consists of fields and methods   
        
class Model:
    def __init__(self, file_name, x, y, z, s, h):
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.sh = loadShape(file_name)
        self.sh.disableStyle()
        self.theta = random(TWO_PI)
        
    def render(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        #rotateY(self.theta)
        rotateZ(PI)
        #rotateX(-HALF_PI)
        scale(50)
        stroke((self.h) % 256, 255, 255)
        noFill()
        shape(self.sh)
        popMatrix()
        #self.theta += 0.01
        self.pos.z += 6
        self.h += 0.2
        #if self.pos.z > 50:
            #anim1_finished = True

class Model2:
    def __init__(self, file_name, x, y, z, s, h):
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.sh = loadShape(file_name)
        self.sh.disableStyle()
        self.theta = random(TWO_PI)
        
    def render(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        rotateY(HALF_PI)
        rotateZ(PI)
        #rotateX(HALF_PI)
        scale(50)
        stroke((self.h) % 256, 255, 255)
        noFill()
        shape(self.sh)
        popMatrix()
        #self.theta += 0.01
        self.pos.x += 2.5
        self.h += 0.3
        if self.pos.x > 4000:
            self.pos.x = -500
            self.pos.z = 100
            self.s += 20
class Model3:
    def __init__(self, file_name, x, y, z, s, h):
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.sh = loadShape(file_name)
        self.sh.disableStyle()
        self.theta = random(TWO_PI)
        
    def render(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        rotateY(-HALF_PI)
        rotateZ(PI)
        #rotateX(HALF_PI)
        scale(50)
        stroke((self.h) % 256, 255, 255)
        noFill()
        shape(self.sh)
        popMatrix()
        #self.theta += 0.01
        self.pos.x -= 10
        #if self.pos.z > 50:
            #anim1_finished = True
        self.h += 0.5
class MSX_Model:
    def __init__(self, file_name, x, y, z, s, h):
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.sh = loadShape(file_name)
        self.sh.disableStyle()
        self.theta = TWO_PI # makes random rotations
        
        
    def render(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        rotateY(self.theta)
        rotateX(-HALF_PI)
        scale(80 + noise(self.theta * 2) * 50)
        stroke((self.h) % 256, 255, 255)
        fill(200 + self.h,0,0)
        shape(self.sh)
        popMatrix()
        if self.pos.z >= 190:
            self.theta += 0.01
            self.pos.z -= 0.8
        else:
            self.theta = 0.01
            self.pos.z -= 0.1
        self.h += 0.5
