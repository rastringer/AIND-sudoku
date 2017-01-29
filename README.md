# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: We find constraints by seeking out twin boxes, themselves constrained by their peer cells and beyond, to include rows, columns and diagonals. 
If we identify two boxes with two digits (eg, 2, 5), we check to see if both share the same digits. This affords us the useful limitation that each of the two squares has to make use of one of those two numbers. We can then remove the numbers from consideration from other boxes (eg if a box had 2, 3, 5, 7, we could remove 2, 5). This further constrains the board and makes further solving easier.


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: The diagonals add further constraints we can use to solve the puzzle, since they are added to the peer cells (in 3 x 3 square groupings), rows and columns that are duty bound to contain the numbers 1 -- 9 only once. 

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.