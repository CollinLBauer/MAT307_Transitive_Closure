from Vertex import Vertex
from Edge import Edge

def main():
    print("I do something.")

    aSet = [Vertex(10,10),Vertex(10,20),Vertex(10,30),
            Vertex(30,20),Vertex(30,30),Vertex(20,30),
            Vertex(10,30),Vertex(10,20)]
    
    aBinRel = [Edge(aSet[0],aSet[1])]

    for s in aBinRel:
        print(s)


main()
