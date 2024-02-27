# Travelling Salesman Problem Solver

This project provides a solution to the Travelling Salesman Problem (TSP) using the nearest neighbor heuristic method. The TSP is a classic combinatorial optimization problem where the goal is to find the shortest possible route that visits each city exactly once and returns to the origin city.

## Example Usage

Consider a graph with 6 vertices:
- Run the program.
- Select 6 vertices
- Enter the following weighted edges into the respective field:
(0, 1, 3); (1, 0, 3); (1, 2, 8); (2, 1, 3); (2, 3, 1); (3, 2, 8); (3, 4, 1); (4, 3, 1); (4, 0, 3); (0, 4, 1); (5, 4, 4); (5, 0, 3); (1, 5, 3); (5, 1, 3); (2, 5, 1); (5, 2, 3); (5, 3, 5)
-  Click on "Create Graph" to visualize the input graph.
- Click on "Find Optimal Path" to calculate the approximate shortest path using the nearest neighbor heuristic.
- The length of the found path and the path itself will be displayed.

  ## Requirements

- Python 3.x
- tkinter
- networkx
- matplotlib


