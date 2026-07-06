# 🔑 Secure Password Manager Vault

> A lightweight local credential manager engineered using Object-Oriented Programming (OOP) architectures, high-performance hash dictionary mappings, and flat-file serialization workflows.

---

## 🛠️ System Architecture & Engineering Principles

This implementation leverages advanced dictionary lookups and input data filters to secure credential records:

* **Hash Map Lookups:** Utilizes Python dictionary structures to map website strings directly to nested data values, providing constant $O(1)$ search runtime speeds.
* **Key Normalization Filters:** Implements string conditioning methods (`.strip().lower()`) during initializations to prevent lookup errors caused by accidental spaces or case mismatches.
* **Encapsulated Data Models:** Isolates core credential mutations inside dedicated `Credential` object models, shielding credentials from arbitrary external global overwrites.
* **Dynamic Masking Views:** Employs precise text string padding constraints and character duplication maps to generate uniform asterisks (`*`) alongside clear-text strings for secure terminal views.

---

## 📁 Repository Blueprint

```text
Password_Manager/
│
├── data/
│   └── vault.json             # Serialized local database credential vault
│
├── src/
│   ├── main.py                # Vault user interface loop & input processing shell
│   ├── credential.py          # Credential object boundaries & text formatting
│   └── vault.py               # Central storage dictionary conductor & JSON I/O
│
├── .gitignore                 # Excludes local artifacts & sensitive data from GitHub
├── README.md                  
└── requirements.txt           # Package tracking catalog