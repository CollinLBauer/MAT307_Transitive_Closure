import numpy as np
import itertools as it
from copy import deepcopy
import sys
import operator as op
from random import sample

from big_ol_pile_of_manim_imports import *




class FromInput(Scene):
    
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
            for j in range(46,48):
                char = chr(j)
                vertStr[i] = vertStr[i].replace(char,"")
            for j in range (58,127):
                char = chr(j)
                vertStr[i] = vertStr[i].replace(char,"")
            vertStr[i] = vertStr[i].split(",")
#            print(vert) #debug
            for j in range(len(vertStr[i])):
                vertStr[i][j] = int(vertStr[i][j])
            self.verts.append(vertStr[i])

        print(self.vertLbls)
        print(self.verts)
        
        
#        print("vertStr: \"" + vertStr + "\"")
#        print("edgeStr: \"" + edgeStr + "\"")



    def construct(self):
        print("\nNote: FromInput.mp4 will be overwritten upon execution.")
        print("Please backup any needed animations before continuing.")
        self.buildGraph()

        print(self.vertLbls)
        print(self.verts)

        self.wait(3)