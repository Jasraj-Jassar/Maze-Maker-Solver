# Maze Maker Solver

A Python project that generates mazes and finds paths through them.

Love Problem Solving So... Created my own challenge  
Instead of taking the array and processing it, plan is to use OpenCV and treat it as a vision system challenge.

## Features

- Random maze generation
- Simple pathfinding algorithm
- Visual representation using basic libraries

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

- The script uses OpenCV to capture the current Tkinter window and detect the red maze mouse location.
- It then randomly chooses a direction (up, down, left, right).
- Before moving, it checks if there's a wall in that direction.
- If there's a wall, it retries with a new random direction.
- This process continues until the end point is reached.

**2nd Solution – Smarter Random Maze Solving Algorithm**  
The smarter solver still moves randomly, but it samples the four neighboring cells around the mouse (three directions plus the current goal direction) and inspects the pixel colors (`smarter_random_mode_actions/smarter_random_solver.py:16-39`).

- A green block (`g >= 120`, `r/b <= 20`) is treated as the goal and immediately chosen so the solver can home in on the end point.
- Otherwise any dark block (`r/g/b < 200`) is considered a passable path and added to the valid moves before picking one at random, which keeps the mouse exploring only walkable tiles while still avoiding overly deterministic behavior.

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

- [OpenCV](https://opencv.org/) – For real-time computer vision tasks  
- [Tkinter](https://docs.python.org/3/library/tkinter.html) – For GUI window rendering  
- [NumPy](https://numpy.org/) – For efficient maze mouse detection(circle finding algorithm)
