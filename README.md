## **Cellular Automata Simulator**

A Python-based Cellular Automata (CA) simulator implemented using NumPy and Pygame. This simulator includes a variety of CA types, from classic Conway’s Game of Life variants to 1D and cyclic automata, with real-time visualizations in a single Pygame window.

---

## **Features**
Choose between 8 cellular automata types via console menu.
Fully visualized in Pygame, supports color-coded states.
Adjustable parameters: grid size, cell size, frames per second, neighborhood radius.
Real-time updates without flickering or reopening windows.

## **Supported Cellular Automata**

1. **HighLife** – Conway’s Game of Life variant (B36/S23)  
    - A variant of Conway’s Game of Life.
    - Rules (B36/S23):
        - A dead cell becomes alive if it has 3 or 6 neighbors (birth).
        - A live cell survives if it has 2 or 3 neighbors.
    - Produces complex patterns like gliders and replicators.
2. **Brian’s Brain** – Three-state CA: off, on, dying  
    - A 3-state automaton.
    - States:
        0 = OFF
        1 = ON
        2 = DYING
    - Rules:
        ON → DYING
        DYING → OFF
        OFF → ON if exactly 2 ON neighbors
    - Creates moving “wave” patterns resembling neural activity.
3. **Seeds** – Simple 2-state CA, all live cells die; dead cells with 2 neighbors become alive  
    - Binary CA with simple explosive growth.
    - Rules:
        OFF → ON if exactly 2 neighbors (birth)
        ON → OFF (no survival)
    - Produces rapidly growing, chaotic patterns.
4. **Wireworld** – Simulates electronic circuits (states: empty, head, tail, conductor)  
    - Simulates electronic circuits.
    - States:
        0 = Empty
        1 = Electron head
        2 = Electron tail
        3 = Conductor
    - Rules:
        Head → Tail
        Tail → Conductor
        Conductor → Head if 1 or 2 neighbors are heads
    - Can simulate logic gates and wires in a grid.
5. **Langton’s Ant** – Ant moves on a grid flipping cells  
    - A Turing-complete 2D CA with a single moving agent (“ant”).
    - Rules:
        On a white cell: turn right, flip the cell to black, move forward.
        On a black cell: turn left, flip the cell to white, move forward.
    - Generates highway and chaotic patterns from simple rules.
6. **Larger-than-Life / Totalistic CA** – Customizable radius and birth/survive rules  
    - Generalization of Life to larger neighborhoods.
    - Example rule (B3/S45678):
        Birth if 3 neighbors
        Survive if ≥4 neighbors
    - Produces dense and complex patterns.
7. **Elementary Cellular Automata (1D)** – Wolfram rules applied row by row  
    - 1D binary CA, evolves row by row.
    - Each cell depends on left, center, right neighbors.
    - Example: Rule 110:
        Binary rule expressed as 8-bit number determining next state.
    - Can generate fractal, chaotic, or repetitive patterns.
8. **Cyclic Cellular Automata** – N-state CA where a cell increments if neighbor has next state  
    - Each cell has N states (e.g., N=8).
    - Rules:
        A cell advances to the next state if a neighbor has that next state.
        States cycle modulo N.
    - Creates colorful rotating wave patterns, useful for modeling excitable media.

---

## **Installation**
python setup.py

### To run manually later, activate the environment:
python -m venv ca_env

# Linux / Mac
source ca_env/bin/activate
# Windows
ca_env\Scripts\activate

# Then run
python main.py

---

## **Configuration**
- Grid size: size in main.py (default 50x50)
- Cell size for display: scale (default 10)
- Frames per second: fps (default 10)
- Cyclic CA states (N): change N in main.py for option 8

## **Notes**
- All CA types use toroidal boundary conditions (edges wrap around).
- Colors are automatically assigned:
    Binary CA → black (dead) / white (alive)
    Langton’s Ant → red ant on black/white grid
    Wireworld → blue (head), yellow (conductor), red (tail), black (empty)
    Cyclic CA → rainbow gradient based on state
- Fully compatible with NumPy 2.x and Pygame.

##**Folder Structure**
cellular_automata/
│
├── main.py                  # Main driver to choose and run CA type
├── findNeighbour.py         # Fixed neighbor-finding function (used by all CA)
├── rules.py                 # Contains all rules functions (HighLife, Brian, Seeds, etc.)
├── updateMatrix.py          # Optional: used by Conway/HighLife/Brian/Seeds
├── utils.py                 # Optional: helper functions for coloring, matrix init
├── run_life_simulation.py   # Optional: help for the initial setup
├── generate_examples.py     # Optional: helps to generate the example for each CA
├── README.md                # Instructions for usage
└── examples/                # Optional: preset patterns / seeds for CA
    ├── wireworld_gates.npy
    ├── langtons_ant_pattern.npy
    └── conway_glider.npy
