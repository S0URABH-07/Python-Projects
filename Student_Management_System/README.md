# Student Management System

A lightweight, terminal-based Student Management System built using core Python concepts and Object-Oriented Programming (OOP). This system allows users to perform CRUD (Create, Read, Update, Delete) operations on student profiles while ensuring permanent data storage using JSON formatting.

## 🚀 Features
- **Add Student Record:** Creates unique student entries with validation.
- **View All Records:** Displays all stored student information cleanly in the terminal.
- **Search Profile:** Instantly look up a specific student using their unique ID.
- **Course Enrollment:** Dynamically append new courses to specific student accounts.
- **Data Persistence:** Automatically saves and loads data using standard JSON file storage (`data/students.json`).
- **Input Error Handling:** Protects application execution using `try-except` blocks to prevent input crashes.

## 🛠️ Tech Stack & Concepts Applied
- **Language:** Python
- **Object-Oriented Programming (OOP):** Custom class structures, object constructors (`__init__`), methods, and encapsulation.
- **Data Collections:** Dictionaries (for fast lookup) and Lists (for course registration).
- **File Handling:** Read/Write operations with JSON integration via the `json` module.
- **Error Handling:** Graceful exception recovery using `try-except` blocks.

## 📁 Project Structure
```text
student_management_system/
│
├── data/
│   └── students.json          # Persistent JSON storage
│
└── src/
    ├── __init__.py            # Python package initializer
    ├── student.py             # Student entity class definition
    ├── system.py              # Main system engine & logic
    └── main.py                # Command-line menu UI loop