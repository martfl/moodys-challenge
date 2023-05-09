# Mars Rover Navigation 🚀🤖


## Overview

This script provides a solution to the Mars Rover Navigation problem. The problem consists of navigating a squad of robotic rovers on a rectangular plateau on Mars. Each rover's position and location are represented by x and y coordinates and a letter representing one of the four cardinal compass points (N, E, S, W). The plateau is divided into a grid to simplify navigation. 

Rovers receive instructions as a string of letters, with the possible letters being 'L', 'R', and 'M'. 'L' and 'R' make the rover spin 90 degrees left or right, respectively, without moving from its current spot. 'M' means move forward one grid point and maintain the same heading. The goal is to find the final coordinates and heading for each rover after executing their respective instructions.

```
       N
       ^
       |
 W <---+---> E
       |
       v
       S

Plateau (5 x 5 grid):
+-----+-----+-----+-----+-----+
|     |     |     |     |     |
|  0,4|  1,4|  2,4|  3,4|  4,4|
+-----+-----+-----+-----+-----+
|     |  ^  |     |     |     |
|  0,3| 1,3 |  2,3|  3,3|  4,3|
+-----+--N--+-----+-----+-----+
|     |     |     |  >  |     |
|  0,2|  1,2|  2,2|  3,2|  4,2|
+-----+-----+-----+--E--+-----+
|     |     |     |     |     |
|  0,1|  1,1|  2,1|  3,1|  4,1|
+-----+-----+-----+-----+-----+
|     |     |     |     |     |
|  0,0|  1,0|  2,0|  3,0|  4,0|
+-----+-----+-----+-----+-----+

Rover 1: Position (1, 2, N)
Rover 2: Position (3, 3, E)

```

## Running the Script

To run the script, you can either use an input file or pass the input data directly through the command line. To use an input file, create a text file with the input data formatted according to the problem description, and then run the script as follows:

`python main.py < input_test.txt`


To pass the input data directly through the command line, run the script and enter the input data when prompted and send the EOF command to end (Ctrl+D):

`python main.py`


## Running the Tests

To run the tests, simply execute the following command in your terminal:

`python -m unittest tests.py`


## Possible optimizations

- The script could be optimized by breaking the instructions processing into two steps: first, calculate the rover's final direction, and then calculate its final position. This way, we can avoid redundant moves in the same direction (e.g., "MMLMMRMM" can be simplified to "MRMM"). However, this optimization might not always lead to significant improvements, as it depends on the input data.

- If the rover instructions and positions were to be processed in parallel, we could use multiprocessing or multithreading to execute the instructions for multiple rovers simultaneously. However, this would only be applicable if the rovers' movements did not depend on each other (i.e., if they could move at the same time).

- Create a Plateau class. Instead of using a tuple to represent the plateau size, create a Plateau class that encapsulates the dimensions and the grid. This will make it easier to handle the grid and any associated operations, such as checking if a position is within bounds.

- Implement a command-line interface to allow users to provide input data via command-line arguments or input files.