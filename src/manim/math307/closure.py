import numpy as np
import itertools as it
from copy import deepcopy
import sys
import operator as op
from random import sample

from big_ol_pile_of_manim_imports import *


class Closure(Scene):

    def buildGraph(self):
        print("(base directory is at ~/manim/")
        inFile = open(input("Name a graph to read: "),"r")
        
        self.vertLbls = []  # labels of each vertex; for building edges
        self.verts = []     # verticies, stored as 2D array of ints
        self.edges = []     # edges, stored as 2D array of vert labels
        vertStr = "" # stores vertices from file
        edgeStr = "" #stores edges from file
        #vertices and edges must all be on same line
        #vertices line must be labeled with 'v-'
        #edge line must be labeled with 'e-'

        for ln in inFile:
#            print(ln)
            if len(ln) > 0:
                if ln[0] == 'v' or ln[0] == 'V':
                    vertStr = ln
                if ln[0] == 'e' or ln[0] == 'E':
                    edgeStr = ln

#        vertLbls = []       
#        verts = []          
        vertStr = vertStr[2:len(vertStr)-1].split(";")
#        print(vertStr) #debug
        for i in range(len(vertStr)):
            self.vertLbls.append(vertStr[i][0])
#            print(vert) #debug
            for j in range(0,44):
                char = chr(j)
                vertStr[i] = vertStr[i].replace(char,"")
            for j in range (58,127):
                char = chr(j)
                vertStr[i] = vertStr[i].replace(char,"")
            vertStr[i] = vertStr[i].split(",")
#            print(vert) #debug
            for j in range(len(vertStr[i])):
                vertStr[i][j] = eval(vertStr[i][j])
            self.verts.append(vertStr[i])

            #loop: build edges[]
        edgeStr = edgeStr[2:len(edgeStr)-1].split(";")
#        print(edgeStr) #debug
        for i in range((len(edgeStr))):
#            print(edgeStr[i]) #debug
            edgeStr[i] = edgeStr[i].replace("(","")
            edgeStr[i] = edgeStr[i].replace(")","")
            edgeStr[i] = edgeStr[i].split(",")
#            print(edgeStr[i]) #debug
            self.edges.append(edgeStr[i])



    def construct(self):
            print("\nNote: FromInput.mp4 will be overwritten upon execution.")
            print("Please backup any needed animations before continuing.")
            self.buildGraph()

            ##Creation of the initial conditions
            circles = []
            adjacency = []
            
            for i in range(len(self.verts)):
                subAdjacency = []
                circle = Circle(radius=.05)
                circle.move_to(self.verts[i][0] * RIGHT + self.verts[i][1] * UP)
                circles.append(circle)
                for j in range(len(self.verts)):
                    subAdjacency.append(0)
                self.add(circle)
                adjacency.append(subAdjacency)

            
            for i in range(len(self.edges)):
                index1 = self.vertLbls.index(self.edges[i][0])
                index2 = self.vertLbls.index(self.edges[i][1])
                adjacency[index1][index2] = 1
                adjacency[index2][index1] = 1
            #####EVERYTHING ABOVE THIS POINT CAN BE CHANGED IF YOU WISH.  JUST MAKE SURE TO PROVIDE A LIST OF CIRCLES
            #####CALLED 'circles' AND AN ADJACENCY MATRIX CALLED 'adjacency' THAT DESCRIBES WHICH CIRCLES
            #####SHOULD BE CONNECTED BY A CIRCLE.
            #####EVERYTHING PAST THIS POINT SHOULD BE LEFT IN  

            #Connects all of the circles are are visually next to each other
            for i in range(len(adjacency)):
                for j in range(i+1,len(adjacency[i])):
                    if adjacency[i][j] == 1:
                        line = Line(circles[i],circles[j])
                        self.add(line)

            self.wait(.25)

            #Creates an array that will store all of the adjacency matrices up to the power of n
            adjacencies = [adjacency]
            adjacencyN = np.matmul(adjacency,adjacency)
            for i in range(len(adjacency)):
                adjacencies.append(adjacencyN)
                adjacencyN = np.matmul(adjacency, adjacencyN)
            
            #Changes every element of every matrix that is nonzero to just be 1
            for i in range(len(adjacencies)):
                for j in range(len(adjacencies[i])):
                    for k in range(len(adjacencies[i][j])):
                        if adjacencies[i][j][k] != 0:
                            adjacencies[i][j][k] = 1
            
            #Takes the ith adjacency matrix and subtracts the value in the (j,k) component of every preceding adjacency matrix
            #So that later when lines are drawn, there will not be unnecesarry repeats.
            for i in range(len(adjacencies) - 1, -1, -1):
                for j in range(len(adjacencies[i])):
                    for k in range(len(adjacencies[i][k])):
                        for l in range(0,i):
                            if (adjacencies[i][j][k] == adjacencies[l][j][k]):
                                adjacencies[i][j][k] = 0
            
            #Creates lists to keep track of the lines so that the colors can be changed
            oldestLines = []
            olderLines = []
            oldLines = []
            newLines = []
            for i in range(1, len(adjacencies)):
                
                for j in range(len(adjacencies[i])):
                    for k in range(j+1,len(adjacencies[i][j])):
                        if adjacencies[i][j][k] == 1:
                            line = Line(circles[j],circles[k], color = GREEN, DEFAULT_PIXEL_WIDTH=.05)
                            newLines.append(line)
                            
                print(i/(len(adjacencies) - 1))

                for l in range(len(newLines)):
                    self.add(newLines[l])

                for l in range(len(oldLines)):
                    oldLines[l].set_color(YELLOW)

                for l in range(len(olderLines)):
                    olderLines[l].set_color(RED)

                for l in range(len(oldestLines)):
                    oldestLines[l].set_color(WHITE)

                for l in range(len(circles)):
                    self.add(circles[l])
                oldestLines = olderLines
                olderLines = oldLines
                oldLines = newLines
                newLines = []

                
                self.wait(.25)

            
            closure = adjacencies[0]
            for i in range(1,len(adjacencies)):
                closure = np.add(closure,adjacencies[i])
            print(closure)


            print("Labels: " + str(self.vertLbls))
            print("Vertices: " + str(self.verts))
            print("Edges: " + str(self.edges))

            self.wait(3)
