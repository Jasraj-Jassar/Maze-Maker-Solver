# Maze Maker Solver

A Python project that generates mazes and finds paths through them.

## Features

- Random maze generation
- Simple pathfinding algorithm
- Visual representation using basic libraries

## How It Works

This script generates a maze grid with a guaranteed path from the top-left (`A`) to the bottom-right (`Y`).

Following is the way i think about this:

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

## Getting Started

Clone the repo and run the script:

```bash
git clone https://github.com/yourusername/maze-maker-solver.git
cd maze-maker-solver
python main.py
