# 🎮 Console Quiz Game Engine

> An interactive, terminal-based interview assessment engine utilizing state-driven index tracking, strict option validation loops, and external JSON data structures.

---

## 🛠️ System Architecture & Engineering Principles

This implementation highlights core logic encapsulation and data parsing strategies:

* **String Normalization pipelines:** Leverages sanitization methods (`.strip().upper()`) to process keyboard inputs safely, preventing evaluation mismatches from case discrepancies or spaces.
* **Bounded Index State Machine:** Manages session transitions dynamically using linear index increment tracking, protecting runtime lookups from out-of-range index crashes.
* **Nested Data Deserialization:** Maps structured arrays of question dictionaries directly from JSON file storage into operational class instances at initialization.
* **Defensive Validation Loop Gates:** Protects runtime data using targeted verification loops (`while True`), isolating and prompting against arbitrary invalid input letters.

---

## 📁 Repository Blueprint

```text
Quiz_Game/
│
├── data/
│   └── quiz_data.json        
│
├── src/
│   ├── main.py                # System interface loop & option verification shell
│   ├── question.py            
│   └── quiz.py                # Game logic orchestrator
│
├── README.md                  
└── Requirements.txt           # Dependency schema