# Python Game of Life (CLI)

A lightweight Terminal/Command Line implementation of **Conway's Game of Life** written in Python. This project features interactive cell toggling, board resetting, and step-by-step state updates using a wrapped-grid boundary system.

---

## Features

- **Interactive CLI Interface:** Controlled via terminal commands.
- **Torus Topology (Wrapped Edges):** Cells wrap around the screen borders horizontally and vertically.
- **Customizable Grid:** Adjust grid size on initialization (default: 20x20).
- **Cell Editing:** Toggle cells between alive (`#`) and dead (`.`) at any specified coordinate.

---

## Rules of Conway's Game of Life

1. **Underpopulation:** Any live cell with fewer than 2 live neighbors dies.
2. **Survival:** Any live cell with 2 or 3 live neighbors lives on to the next generation.
3. **Overpopulation:** Any live cell with more than 3 live neighbors dies.
4. **Reproduction:** Any dead cell with exactly 3 live neighbors becomes a live cell.

---

## How to Run

### Prerequisites
- **Python 3.x** installed on your system.

### Running the Game
Run the main script directly using Python:

```bash
python game_of_life.py