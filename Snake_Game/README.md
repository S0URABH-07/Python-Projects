# 🐍 Real-Time 2D Snake Game Engine

> A high-performance desktop graphical application engineered using Object-Oriented Programming (OOP) principles, asynchronous rendering update loops, and coordinate-grid geometry collision mechanics.

---

## 🛠️ System Architecture & Engineering Principles

This implementation shifts from static blocking console interfaces into real-time interactive game design:

* **Asynchronous Frame Updates:** Implements an unblocked timer update loop using Tkinter execution hooks (`.after()`), achieving uniform frame delivery without execution freezes.
* **Coordinate Grid Geometry Mapping:** Operates on a structured $X$/$Y$ raster coordinate system grid ($20 \times 20$ pixel block bounds) to handle unified mathematical locomotion steps.
* **Optimized Locomotion Arrays:** Manipulates nested coordinate list nodes dynamically via high-efficiency head injections (`insert()`) and tail removals (`pop()`) to deliver slithering graphics.
* **Slicing-Based Collision Models:** Deploys strict sub-array list-slicing indicators (`[1:]`) to monitor overlapping head matches against trailing segments instantly.

---

## 📁 Repository Blueprint

```text
Snake_Game/
│
├── data/
│   └── high_score.dat         # Persistent flat-file local database tracking benchmark scores
│
├── src/
│   ├── main.py                # Bootstrapper entry-point initializing the GUI workspace loop
│   ├── snake.py               # Vector velocity configurations and tracking matrices
│   ├── food.py                # Random mathematical coordinate spawn generators
│   └── game.py                # Primary Tkinter window canvas coordinator and event listener
│
├── .gitignore                 
└── README.md                 