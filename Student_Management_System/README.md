# 🎓 Student Management System (SMS)

> A production-grade terminal application demonstrating core software engineering principles, robust error handling, and structured data persistence.

---

## 🏗️ Technical Stack & Concepts Applied

This project transitions beyond isolated scripts into a cohesive system architecture, utilizing:

* **Object-Oriented Programming (OOP):** Domain-driven design isolating the core entity blueprint (`Student`) from the system orchestrator (`StudentManagementSystem`).
* **Encapsulation:** Protecting data integrity by enforcing mutations (e.g., handling course configurations) through explicit object methods rather than random access.
* **Data Layouts:** Leveraging fast $O(1)$ lookups via high-efficiency Python dictionary tracking structures combined with safe mutable container lists.
* **Data Persistence:** I/O handling that reads/writes application states into serialized, well-formatted JSON database structures.
* **Defensive Programming:** Active runtime exception monitoring using targeted `try-except` blocks preventing input crashes.

---

## 📁 Repository Layout

```text
student_management_system/
│
├── data/
│   └── students.json          # Persistent flat-file JSON storage
│
├── src/
│   ├── __init__.py            # Explicit package architecture initialization
│   ├── main.py                # Console-based event loop & interaction handling
│   ├── student.py             # Core entity modeling & encapsulation methods
│   └── system.py              # Management layer & CRUD operation engine
│
├── README.md                  # Comprehensive developer reference guide
└── requirements.txt           # Dependency catalog (Standard Library Only)