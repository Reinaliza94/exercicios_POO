class Robot:
    def __init__(self, posiX=0, posiY=0):
        self.posiX = posiX
        self.posiY = posiY
    
    def left(self):
        self.posiX -= 1

    def right(self):
        self.posiX += 1

    def up(self):
        self.posiY += 1

    def down(self):
        self.posiY -= 1

    def position(self):
        print(f"Posição atual: X = {self.posiX}, Y = {self.posiY}")
        return (self.posiX, self.posiY)

robo1 = Robot()
robo1.position()
robo2 = Robot(5,10)
robo2.position()
robo2.right()
robo2.up()
robo2.position()