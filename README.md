# Tac-Toe-with-Minimax-and-Graph-Coloring
Tic-Tac-Toe game where a human player competes against a computer using the **Minimax algorithm** with **Alpha-Beta pruning** to make the best possible moves.



## Overview
This project contains two main functionalities:

1. **Graph Coloring using Arc Consistency and DFS with Backtracking**:
   - The goal is to assign colors to nodes of a graph such that no two adjacent nodes share the same color.
   - Two algorithms are implemented for solving the problem:
     - **Arc Consistency Algorithm**
       This algorithm uses a forward checking technique to prune the domains of variables based on constraints. It ensures that no two adjacent nodes share the same color by               iteratively revising the graph’s variable domains.
       
     - **DFS with Backtracking Algorithm**
      This algorithm attempts to assign a color to each node by using a depth-first search (DFS) approach. If a node cannot be assigned a valid color (due to conflicts with its           neighbors), the algorithm backtracks and tries a different color until a solution is found.


    - **Graph Drawing and Solution Visualization**
    Once the graph coloring solution is determined, the results are visualized using NetworkX and Matplotlib. The nodes of the graph are displayed with different colors to                represent the solution, and the edges connecting them indicate the relationships between nodes.
    
    Running the graph coloring solution will show a visual representation of the graph with the assigned colors, helping to confirm the correctness of the coloring.

2. **Tic-Tac-Toe Game with Minimax Algorithm**:
   - A simple command-line Tic-Tac-Toe game where a human player competes against a computer using the **Minimax algorithm** with **Alpha-Beta pruning** to make the best possible moves.

---

## Technologies Used

The project uses the following technologies:

- **Python**: The primary programming language used for both the graph coloring algorithms and the Tic-Tac-Toe game.
- **NetworkX**: A Python library used for the graph data structure and algorithms, particularly for representing the graph in the graph coloring problem.
- **Matplotlib**: A Python library used for visualizing the graph with colored nodes.
- **Time** and **Random**: Python standard libraries used for managing the game flow in Tic-Tac-Toe and adding suspense for the computer's turn.
  

