# ⚔️ Advanced Text-Based RPG Engine

> A dynamic, terminal-driven role-playing battle simulation built using advanced Object-Oriented Programming (OOP) architectures, object-to-object interaction patterns, and JSON game state serialization.

---

## 🛠️ System Architecture & Engineering Principles

This project implements advanced game state tracking and real-time object attribute manipulation:

* **Object-to-Object Interaction:** Interconnects completely distinct class instances at runtime—allowing the `player` object to target an `enemy` object and alter its internal variables directly.
* **Algorithmic Damage Variance:** Implements dynamic numeric deviation ranges using random choice modules to introduce random damage hits, tracking combat outcomes on every turn.
* **Progress Scaling Logic:** Monitors accumulated metrics against dynamic equations ($Level \times 50$) to trigger character attribute stat expansions during leveling transitions.
* **Bounded List Slicing:** Limits array index scanning windows (`[:2]`) based on active state criteria to balance combat encounters for low-level entities.

---

## 📁 Repository Blueprint

```text
Text_Role_Playing_Game/
│
├── data/
│   └── save_data.json         # Serialized player profile progress state data
│
├── src/
│   ├── main.py                # Dashboard visualization loop & user commands
│   ├── character.py           # Character entity properties & attribute modifiers
│   └── game.py                # Battle arena state loop & database I/O core
│
├── .gitignore                 # Excludes system junk & cache binaries from GitHub
├── README.md                  
└── requirements.txt           # Standard library catalog listing schema