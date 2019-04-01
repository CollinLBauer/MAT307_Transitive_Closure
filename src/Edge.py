class Edge:

    def __init__(self, v1, v2):
        self.v1: Vertex = v1
        self.v2: Vertex = v2

    def __str__(self):
        return "Edge: {} -- {}".format(self.v1,self.v2)
