import numpy as np
import itertools as it
from copy import deepcopy
import sys
import operator as op
from random import sample

from big_ol_pile_of_manim_imports import *


class LetterC(Scene):
        def construct(self):
            

            ##Creation of the initial conditions
            circles = []
            adjacency = []
            for i in range(10,71):
                
                #Creates all of the circles
                circle = Circle(radius=.05)

                #Moves all of the circle to make them into a C shape
                circle.move_to(2.8 * np.cos(np.pi * (1/4) * .1 * i) * RIGHT + 3.5 * np.sin(np.pi * (1/4) * .1 *  i) * UP)

                #Adds the circle to an array to be accessed later and onto the scene
                circles.append(circle)
                self.add(circle)
                subAdjacency = []
                for j in range(61):
                    subAdjacency.append(0)
                if i != 10:
                    subAdjacency[i-11] = 1
                if i != 70:
                    subAdjacency[i-9] = 1
                adjacency.append(subAdjacency)
            
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


            self.wait()

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
                            adjacencies[i][j][k] -= adjacencies[l][j][k]
            
            #Creates lists to keep track of the lines so that the colors can be changed
            oldestLines = []
            olderLines = []
            oldLines = []
            newLines = []
            for i in range(2, len(adjacencies)):
                
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

                self.wait(0.5)

            

            
            
