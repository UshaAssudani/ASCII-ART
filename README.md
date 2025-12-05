# ASCII-ART
🎨 ASCII Art Project with Color Selection (Python)

A fully interactive, menu-driven Python console application that generates large ASCII art for characters, words, alphabets, numbers, and alphabet ranges — with user-selected text colors using Colorama.

This project is specially designed for the Windows terminal and uses custom ASCII patterns embedded directly inside the script.

---

📑 Table of Contents

* About the Project
* Features
* How It Works
* Project Files
* Installation
* Usage
* Example Output
* Notes
* Author

---

📝 About the Project

This ASCII Art Project allows users to generate large, stylish ASCII text directly in the terminal.
The unique feature of this project is that users can **select their own color before generating ASCII output**, making it visually attractive and interactive.

All ASCII character patterns are pre-defined in the program and displayed using smart slicing logic.

---

⭐ Features

✔ 1. One Character Mode
Generate large ASCII art for a single character with selected color.

✔ 2. Alphanumeric Word Mode
Generate ASCII art for words up to 15 characters.
Supports:

* A–Z
* 0–9
* Special symbols

✔ 3. Alphabet Range Mode
Generate ASCII art for alphabet ranges such as:
A-D
M-P
X-Z

✔ 4. Only Alphabets Mode
Accepts only A–Z characters (maximum 15).

✔ 5. Only Numbers Mode
Accepts only digits 0–9 (maximum 15).

✔ 6. Color Selection System
User selects a text color before entering input:

* Red
* Green
* Yellow
* Blue
* Magenta
* Cyan
* White

✔ 7. Fully Menu-Driven Interface
Uses `msvcrt.getch()` for instant keypress without pressing Enter.

---

🧠 How It Works

🔤 ASCII Pattern Data
The script contains a list of 5 large strings.
Each row stores patterns for all characters side-by-side.

Each character uses:

* 6 columns width
* Mathematical indexing to extract correct character design

Logic Used:
((ord(text) - 64) - 1) * 6    → For letters A–Z
(ord(x) - 17) * 6            → For digits 0–9

🔁 Printing Mechanism
For each of the 5 ASCII rows:

* The start index is calculated
* 6 characters are sliced
* Output is printed side by side
* Selected color is applied using Colorama

🎨 Color Handling
The user selects a color at runtime.
The selected color is stored in `current_color` and applied to every ASCII print.

---

📂 Project Files

asciiartproject.py
README.md

The Python file contains:

* ASCII pattern database
* Color selection module
* Menu-driven UI
* Input validation
* Character slicing logic
* All five ASCII display modes

---

⚙ Installation

1️⃣ Install Python
Download from:
[https://www.python.org/](https://www.python.org/)

2️⃣ Install Colorama
pip install colorama

3️⃣ Clone the Repository
git clone [https://github.com/your-username/ascii-art-project.git](https://github.com/your-username/ascii-art-project.git)

4️⃣ Navigate to Folder
cd ascii-art-project

5️⃣ Run the Script
python asciiartproject.py

---

▶ Usage

After running the program, you will see:

********** ASCII ART PROJECT **********

OPTIONS --

1. One Character
2. Words
3. Range
4. Only Alphabets
5. Only Numbers
6. Exit

After selecting a mode:

* Choose a color
* Enter your input
* View your colored ASCII output

---

🖼 Example Output

Input:
A

Output (Example):

---

* *

---

* *
* *

(Note: Actual output may vary based on ASCII pattern data.)

---

⚠ Notes

* This project is **Windows-specific** because it uses:

  * `msvcrt.getch()`
  * `os.system("cls")`

* Maximum input length: 15 characters

* Range input must be exactly 3 characters (e.g., A-D)

* Colorama is required for color output

---

👨‍💻 Author

Usha Assudani
