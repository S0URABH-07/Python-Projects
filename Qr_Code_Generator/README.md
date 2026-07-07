# 🎨 Custom Pixel QR Code Generator

> An advanced graphic compiler engineered to encode raw string payloads into high-resolution, fault-tolerant binary QR matrix grids using external rendering pipelines, custom color mappings, and historical audit streams.

---

## 🛠️ System Architecture & Engineering Principles

This system marks a transition into external asset handling and image generation logic:

* **Matrix Transformation Mapping:** Converts plain text payloads into structured binary matrix rows ($1$ representing dark foreground modules and $0$ representing light background canvas pixels).
* **Fault-Tolerant Redundancy:** Employs high-tier error correction configurations (`ERROR_CORRECT_H`) to generate redundant tracking data blocks, ensuring scannability even with 30% image surface loss.
* **Pixel Density Scaling:** Multiplies layout grid models dynamically using fixed block constraints (`box_size=10`) to scale tiny vector arrays into high-definition bitmaps.
* **Audit Trail Architecture:** Implements a structured append-only file logging pipeline (`src/logger.py`) to systematically track generation timestamps and encoded text histories.

---

## 📁 Repository Blueprint

```text
Qr_Code_Generator/
│
├── data/
│   └── generation_history.log # Append-only chronological system audit log file
│
├── outputs/                   # Hard-drive destination directory for generated .png assets
│
├── src/
│   ├── main.py                # Command user interface, input validation, and safety gates
│   ├── generator.py           # Core third-party image compiler and canvas writer
│   └── logger.py              # Clock-synchronized operational history stream
│
├── .gitignore                 
├── README.md                  # Comprehensive technical developer manual reference
└── requirements.txt           # Explicit tracking file mapping third-party libraries