# Design Decisions and Implementation Details

## Design Decisions

### 1. Menu-Based Interface
A menu-based interface was selected because it is simple to use and suitable for a Python console application.

### 2. Modular Structure
The program is divided into separate Python files so that different tasks can be managed independently.

### 3. JSON for Storage
JSON was selected for storing item records because it is simple, lightweight, and easy to read and write using Python.

### 4. Matching Method
Possible matches are identified by comparing the category and location of lost and found items.

### 5. Item Status
Each item has a status such as Active or Resolved so that completed records can be identified.

## Implementation Details

The main program is controlled by `main.py`, which displays the menu and connects the different modules.

`item_manager.py` handles entering and displaying item information.

`matching.py` contains the matching logic for comparing lost and found items.

`storage.py` handles adding, loading, updating, and saving item records using JSON.

`constants.py` stores fixed item types and categories.

The item records are stored as dictionaries inside a list. The list is saved to `data/items.json`.

The project uses Python concepts including functions, lists, dictionaries, tuples, sets, loops, conditional statements, modules, file handling, and exception handling.