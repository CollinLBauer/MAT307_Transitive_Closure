# Transitive Closure Project
Collin Bauer, Terence Carey

MATH 307 - Discrete Structures II

College of Charleston, Spring 2019


## Project details
This project uses manim to simulate the transitive closure of a simple graph. It may read an input file with a list of vertices and edges, generates a graph, and iterates transitive closure on said graph. It then outputs an animation which demonstrates the closure from start to finish.

A detailed report for this project can be found in the Report directory. Premade animations can be found in the Example MP4s directory.


### Running project code
Code specific to this project is stored in `src/manim/math307/`

To animate the project, cd into src/manim and run `python3 -m manim math307/closure.py Closure -pl`. Output files will be sent to a Media subdirectory of manim.

Closure will ask for an input file to select from a subdirectory to `manim/` Example graphs can be found in `math307/g/`


## manim
This project builds on the manim lobrary, and requires manim's dependencies in order to run. The manim library is under the MIT free software license.

For details about manim, including how to install dependencies, go to https://github.com/3b1b/manim
