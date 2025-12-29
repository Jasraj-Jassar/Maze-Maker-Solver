# Maze Maker Solver

A Python project that generates mazes and finds paths through them.

Love Problem Solving So... Created my own challenge  
Maze generation and solvers operate directly on the grid data.

## Features

- Random maze generation
- Simple pathfinding algorithm
- Visual representation using basic libraries
- Dijkstra shortest-path solver

## How It generates a maze

This script generates a maze grid with a guaranteed path from the top-left (`A`) to the bottom-right (`Y`).

Following is the way i think about maze generation and what my code is doing:

    A B C D E 
    F G H I J
    K L M N O
    P Q R S T
    U V W X Y

- Movement allowed: only **right** or **down**
- `0` = path, `1` = wall
- The rest of the grid is filled with random walls and paths

**Example Random Path generated at random should look like:**  
A → B → G → H → I → N → S → X → Y

## How It Solves the Maze

**1st Solution – Random Maze Solving Algorithm**  
This is the most time-consuming and inefficient method, but it works.

- The solver reads the maze grid and randomly chooses a valid direction (up, down, left, right).
- It avoids walls by checking neighboring cells before moving.
- This process continues until the end point is reached.

**2nd Solution – Smarter Random Maze Solving Algorithm**  
The smarter solver still moves randomly, but it biases moves toward the goal by preferring steps that reduce the Manhattan distance.

**3rd Solution – Dijkstra Shortest-Path Algorithm**  
The Dijkstra solver reads the generated maze grid directly, computes the shortest path from the current position to the bottom-right goal, and then simulates the moves step-by-step on the Tkinter board (`dijkstra_algorithm_mode_actions/dijkstra_solver.py` and `dijkstra_algorithm_mode_actions/dijkstra_mode.py`).

## Getting Started

Clone the repository and run the script:

```bash
git clone https://github.com/yourusername/maze-maker-solver.git
cd maze-maker-solver
python -m venv venv

# Activate the virtual environment if not already activated.
# On Linux/macOS:
source venv/bin/activate

# On Windows (uncomment the line below if you are on Windows):
# .\venv\Scripts\activate

pip install -r requirements.txt
python main.py
```

## System dependencies

- `Tkinter` is required for the GUI (`_tkinter` is part of the Python standard library but ships separately on some systems). Install it with `sudo apt install python3-tk` (Debian/Ubuntu) or your OS-equivalent package manager before running the project.
- On Arch Linux, install the `tk` package with `sudo pacman -S tk`.

## Acknowledgements

This project is powered by:

- [Tkinter](https://docs.python.org/3/library/tkinter.html) – For GUI window rendering  
