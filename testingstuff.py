##A lot of what is written here probably shouldn't be used for the final project
##I'm just planning on using it as a rough draft of sorts


import numpy as np
import itertools as it
from copy import deepcopy
import sys
import operator as op
from random import sample

from big_ol_pile_of_manim_imports import *

class Testing(Scene):
    def construct(self):

        #Creates all of the circles
        circle0 = Circle(radius=.25)
        circle1= Circle(radius=.25)
        circle2 = Circle(radius=.25)
        circle3 = Circle(radius=.25)
        circle4 = Circle(radius=.25)
        circle5 = Circle(radius=.25)
        circle6= Circle(radius=.25)
        circle7 = Circle(radius=.25)
        circle8 = Circle(radius=.25)

        #Moves them to where I want them, take note that you can either multiply a direction like UP by a scalar or 
        #add it to itself to achieve the desired effect
        circle0.move_to(UP*3+LEFT)
        circle1.move_to(UP+UP+UP+RIGHT)
        circle4.move_to(DOWN+DOWN+DOWN+RIGHT)
        circle5.move_to(DOWN+DOWN+DOWN+LEFT)
        circle7.move_to(UP+LEFT+LEFT+LEFT)
        circle2.move_to(UP+RIGHT+RIGHT+RIGHT)
        circle3.move_to(DOWN+RIGHT+RIGHT+RIGHT)
        circle6.move_to(DOWN+LEFT+LEFT+LEFT)

        #Puts all of the circles into a list so they'll be easier to handle
        circles = [circle0,circle1,circle2,circle3,circle4,circle5,circle6,circle7,circle8]

        #Connects all of the circles to the two circles that are closest to them visually
        for i in range(len(circles)-1):
            if (i != 7):
                line = Line(circles[i],circles[i+1])
            else:
                line = Line(circle0,circle7)
            self.add(line)

        #Adds all of the circles to the scene to be drawn in next time the program is told to draw something
        self.add(circle0)
        self.add(circle1)
        self.add(circle2)
        self.add(circle3)
        self.add(circle4)
        self.add(circle5)
        self.add(circle6)
        self.add(circle7)

        #From what I can tell this tells the program to update the current scene
        self.wait()

        #adjacency is the original adjacency matrix
        adjacency = np.array([[0,1,0,0,0,0,0,1],[1,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,0],[0,0,1,0,1,0,0,0],[0,0,0,1,0,1,0,0],
        [0,0,0,0,1,0,1,0],[0,0,0,0,0,1,0,1],[1,0,0,0,0,0,1,0]])
        
        #Adjacency2 represents the original adjacency matrix squared
        adjacency2 = np.matmul(adjacency,adjacency)

        #bruhmoment represents the adjacency2 matrix multiplied by the original matrix
        #trust me, it was a bruhmoment when I was writing this
        bruhmoment = np.matmul(adjacency2,adjacency)

        #bruh represents the original adjacency matrix to the fourth power
        #To actually guarantee that the current graph is a transitive closure of the original, it would be required to find adjacency to the eighth
        #Also, don't worry about which side you are multiplying the matrices on, as matrix multiplication is associative.
        bruh = np.matmul(bruhmoment,adjacency)

        #Adds lines in based on if the corresponding vertices are connected to the same vertex
        #These loops are specifically for the adjacency squared
        #Note that the second loop starts at index i instead of 0, this is because the adjacency matrix will be equal to its transpose
        #So we can completely ignore the bottom left half of the matrix when drawing new lines and the diagonal is all 0's, so it can be 
        #ignored as well
        for i in range(len(adjacency2)):
            for j in range(i+1,len(adjacency2[i])):
                if adjacency2[i][j] != 0:
                    line = Line(circles[i],circles[j])
                    self.add(line)

        self.wait()

        for i in range(len(bruhmoment)):
            for j in range(i+1,len(bruhmoment[i])):
                if bruhmoment[i][j] != 0:
                    line = Line(circles[i],circles[j])
                    self.add(line)  
        
        self.wait()

        for i in range(len(bruh)):
            for j in range(i+1,len(bruh[i])):
                if bruh[i][j] != 0:
                    line = Line(circles[i],circles[j])
                    self.add(line)

        self.wait()
