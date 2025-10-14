# Copilot Instructions for PythonBasics

## Project Overview
This repository contains beginner-level Python exercises and scripts, each in its own file. There is no complex architecture or inter-file dependencies; each file is a standalone solution to a specific task or exercise.

## File Structure & Patterns
- Each script (e.g., `task_1_1.py`, `task_1_2.py`, ...) is self-contained and typically starts with user input, followed by simple logic and output.
- The file `RandomPass.py` demonstrates a utility script (random password generator) using standard libraries (`random`, `string`).
- No modules, packages, or imports between user scripts; all logic is local to each file.

## Developer Workflow
- Run scripts directly with Python (e.g., `python task_1_1.py`).
- No build system, test framework, or automation is present.
- Debug by running scripts and observing console output.
- All user input is handled via `input()`; type conversion (e.g., `int()`) is common and necessary for numeric operations.

## Conventions
- Variable names are in German or English, depending on the exercise.
- Input prompts and output messages are often in German.
- Scripts are short, focused, and do not use functions unless required by the task.
- If a script requires a function, it is defined locally (see `RandomPass.py`).
- No external dependencies except for standard Python libraries.

## Examples
- **Password Generator**: See `RandomPass.py` for a pattern using functions and standard libraries.
- **Time Conversion**: See `task_1_12.py` for converting hours, minutes, and seconds to decimal hours.
- **Input Validation**: See `task_1_8.py` for basic numeric range checks.

## Recommendations for AI Agents
- Treat each file as an independent script; do not introduce cross-file imports or dependencies.
- Use clear, concise variable names and match the language of the prompt (German/English).
- Prefer simple, direct solutions using built-in Python features.
- When updating or generating new scripts, follow the style and structure of existing files.
- If adding new instructions or exercises, create a new file following the naming pattern (`task_X_Y.py`).

## Key Files
- `RandomPass.py`: Example of a utility script with a function.
- `task_1_12.py`: Example of input handling and calculation.
- `README.md`: Project title only; no further documentation.

---
For questions or unclear conventions, review existing scripts for style and structure. If a new pattern is needed, document it here.
