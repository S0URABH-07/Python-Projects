# 🏢 Corporate Employee Record System (ERS)

> A high-efficiency administrative terminal application engineered to manage corporate rosters using tabular CSV database flat-files, strict input mapping, and left-aligned string formatting views.

---

## 🛠️ System Architecture & Engineering Principles

This system transitions beyond tree-structured JSON storage into tabular data formats, emphasizing disk writing optimization:

* **Tabular Roster Serialization:** Unpacks active Python objects into structured positional index lists (`[id, name, dept, role, salary]`) designed for standard stream row writers.
* **Stream Parsing Engines:** Leverages native `csv` streaming modules to extract, read, and instantiate row data while skipping headers and filtering out bad array splits.
* **Formatted Column Alignments:** Employs precise text string padding constraints (`{var:<width}`) to guarantee perfectly straight tabular spreadsheet layouts directly inside terminal displays.
* **Cached Transaction Processing:** Executes active profile mutations (such as registrations or removals) inside high-speed computer memory before committing changes to disk.

---

## 📁 Repository Blueprint

```text
Employee_Record_System/
│
├── data/
│   └── employees.csv          # Persistent flat-file spreadsheet ledger
│
├── src/
│   ├── main.py                # Admin interactive console loop & exception capture
│   ├── employee.py            # Profile model boundaries & array format filters
│   └── roster.py              # CSV pipeline conductor & operational CRUD engine
│
├── README.md                
└── requirements.txt           # Dependency schema