class Vertex:

    def __init__(self, x, y, color = "black"):
        self.x: int = x
        self.y: int = y
        self.color: String = color

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def move(self, dX, dY):
        self.x += dX
        self.y += dY

    def setColor(self, color):
        self.color = color

    def __str__(self):
        return "({},{})".format(self.x,self.y)
