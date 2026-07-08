# 🎮 Turn-Based 3x3 Matrix Tic-Tac-Toe Engine

> A modular desktop application engineered using strict Model-View-Controller (MVC) architectural separation, event-driven state validation, and context-safe command closures.

---

## 🛠️ System Architecture & Engineering Principles

This implementation explores state-driven isolation and matrix grid mathematics:

* **Model-View-Controller Decoupling:** Isolates core game rules (`src/logic.py`) completely from visual layout render code (`src/game.py`), passing verification tokens cleanly back up to the frame layer.
* **Chained Vector Evaluation:** Employs optimized chained comparison statements (`b[r][0] == b[r][1] == b[r][2] != ""`) to evaluate 8 independent linear win trajectories inside unified array scans.
* **Context-Safe Closure Traps:** Utilizes default parameter overrides inside lambda expressions (`lambda row=r, col=c:`) to isolate scope variables and map 9 distinct button grid entities correctly.
* **Event-Driven Operational Pipeline:** Leverages OS-level desktop hardware event hooks to process mutations only upon direct user interaction, reducing background processor consumption to zero.

---

## 📁 Repository Blueprint

```text
Tic_Tac_Toe/
│
├── src/
│   ├── main.py                # Bootstrapper entry-point initializing the GUI workspace loop
│   ├── logic.py               # Pure board array mutations and win condition algorithms
│   └── game.py                # Core Tkinter grid rendering and user click tracking
│
├── .gitignore                 # Shields environment system cache files from Git versioning
└── README.md                  # Comprehensive developer operational and technical overview