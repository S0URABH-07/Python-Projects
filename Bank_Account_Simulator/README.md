# 🏦 Bank Account Simulator

> A secure, terminal-driven financial ledger simulation engineered with strict data validation boundaries, PIN authentication gates, and persistent statement logs.

---

## 🛠️ System Architecture & Engineering Principles

This simulator applies foundational object-oriented logic to execute state transactions with defensive error checking:

* **Transactional Encapsulation:** Account metrics (Balances, Owner Profiles, PINs) are locked inside independent `Account` class entities, preventing arbitrary memory edits.
* **Audit Trail Tracking:** Leverages linear array logs (`Lists`) to capture sequential historical data records, ensuring a completely transparent runtime audit path.
* **Defensive Boundary Validations:** Prevents invalid transactional inputs (e.g., negative value checking or overdraft limit protection) via target validation conditional states.
* **Two-Step Authentication Gates:** Restricts access to sensitive account workflows (such as balance lookups, withdrawals, and ledger listings) through an explicit string-comparison PIN check method.

---

## 📁 Repository Blueprint

```text
bank_account_simulator/
│
├── data/
│   └── bank_data.json         
│
├── src/
│   ├── main.py                
│   ├── account.py             
│   └── bank.py               
│
├── README.md                 
└── requirements.txt           # Dependency schema