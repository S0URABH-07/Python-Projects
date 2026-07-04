# 📚 Library Management System (LMS)

> A modular terminal application engineered with domain-isolated entities, state-driven tracking logic, and persistent flat-file storage layouts.

---

## 🛠️ System Architecture & Engineering Principles

This implementation scales core programming fundamentals into an organized backend architecture:

* **State Machine Management:** Books manage their own internal states (`Available` vs `Borrowed`) via atomic boolean flags, ensuring data corruption is impossible.
* **Separation of Concerns (SoC):** Distinct boundaries separate the individual data layer (`Book`), the central ledger database manager (`Library`), and the user interactive shell interface (`main.py`).
* **High-Efficiency Mappings:** Lookups are bound to unique string identifiers (Asset IDs / ISBN numbers) stored inside Python dictionary hash tables, achieving immediate $O(1)$ search speeds.
* **Serialized Data Pipeline:** Reconstructs volatile operational runtime object instances to and from standard persistent JSON flat-file storage configurations dynamically.

---

## 📁 Repository Blueprint

```text
library_management_system/
│
├── data/
│   └── library.json          # Serialized persistent state ledger
│
├── src/
│   ├── main.py                # Command event loop & interactive terminal shell
│   ├── book.py                # Domain entity mapping & individual state flags
│   └── library.py             # System orchestrator, I/O handling, & CRUD engine
│
├── README.md                  # Comprehensive developer documentation
└── requirements.txt           # Dependency tracking (Standard Library Only)