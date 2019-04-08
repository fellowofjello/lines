grow = 0
shrink = 600

def setup():
    size(1000, 1000)
    stroke(45, 15, 75)
    frameRate(60)
    strokeWeight(4)
    background(180,0,75)
    noLoop()

def draw():
    grow = 0
    shrink = 600
    #background(180,0,75)
    fill(255,20)
    rect(width/2, width/2, -grow, -grow)
    rect(grow, width/2,shrink, grow)
    rect(width/2,shrink,shrink, grow)
    rect(width/2, width/2, shrink, grow)
    grow += 3
    shrink -= 3
  
    if (grow == 600):
        grow = 0
        
    if (shrink == 0):
        shrink = 600
        
    loop()
