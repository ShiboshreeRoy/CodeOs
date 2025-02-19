# Code OS - Advanced Text Editor

## Overview
**Code OS** is a lightweight yet powerful text editor built using Python and Tkinter. It provides essential features for code editing, including a built-in terminal, syntax highlighting, and the ability to execute Python and web files.

## Features
- **File Operations:** Create, Open, Save, and Save As files.
- **Edit Menu:** Undo, Redo, Cut, Copy, Paste, and Find.
- **Terminal Integration:** Run Python and web files directly from the editor.
- **Customizable UI:** Toggle terminal visibility, Zoom In, Zoom Out.
- **Cross-Platform:** Works on Linux, Termux (with X server), and Windows.

## Installation

### Linux (Ubuntu/Debian)
1. Update the system:
   ```sh
   sudo apt update && sudo apt upgrade -y
   ```
2. Install Python and Tkinter:
   ```sh
   sudo apt install python3 python3-tk -y
   ```
3. Clone the repository:
   ```sh
   git clone https://github.com/ShiboshreeRoy/CodeOs.git
   cd CodeOs
   ```
4. Run the editor:
   ```sh
   python3 CodeOs.py
   ```

### Termux (Android CLI)
1. Update Termux:
   ```sh
   apt update && apt upgrade -y
   ```
2. Install Python and Tkinter:
   ```sh
   apt install python3 python-tk -y
   ```
3. Clone and run:
   ```sh
   git clone https://github.com/shiboshreeroy/CodeOs.git
   cd CodeOs
   python3 CodeOs.py
   ```
**Note:** Tkinter requires an X server on Termux (e.g., VNC Viewer).

### Windows
1. Install [Python 3](https://www.python.org/downloads/).
2. Clone the repository using Git Bash or download the ZIP.
3. Run:
   ```sh
   python CodeOs.py
   ```

## Usage
- **File Menu:** Create, Open, Save, and Exit.
- **Edit Menu:** Undo, Redo, Copy, Paste, Find.
- **View Menu:** Toggle Terminal, Zoom In/Out.
- **Run Menu:** Execute Python or Web files.
- **Terminal Menu:** Open system terminal.

## Contributing
Feel free to fork this repository, create issues, and submit pull requests!

## License
This project is licensed under the MIT License.

## Author
**Shiboshree Roy**

---
Enjoy coding with **Code OS**! 🚀

