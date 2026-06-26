# OOPs Concepts Demonstrations

This repository contains Python scripts demonstrating Object-Oriented Programming (OOP) concepts such as inheritance, encapsulation, abstraction, and polymorphism. 

## Projects

### 1. Hospital Management System (`hospital mangement system.py`)
A basic hospital management system demonstrating the use of Abstract Base Classes (ABC) and inheritance.
- **Classes:** 
  - `Person` (Abstract base class for `Patient` and `Doctor`)
  - `Patient` (Inherits from `Person`, includes encapsulation for appointment history)
  - `Doctor` (Inherits from `Person`)
  - `Appointment` 
  - `Hospital` (Manages doctors, patients, and appointments)
- **Features:** 
  - Add doctors and patients.
  - Book, accept, and complete appointments.
  - View all registered doctors, patients, and upcoming appointments.

### 2. Library Management System (`librarymangement.py`)
An interactive, CLI-based library management system showcasing different library items and member interactions.
- **Classes:** 
  - `LibraryItem` (Abstract base class)
  - `Book`, `Magazine`, `DVD` (Inherit from `LibraryItem`)
  - `Member` (Manages borrowed items using encapsulation)
  - `Library` (Manages adding, removing, and borrowing items)
- **Features:**
  - Add/Remove different types of items to the library.
  - Search for items by title.
  - Interactive menu to borrow, return, and view borrowed items.

## How to run
Make sure you have Python installed on your system. Run the scripts using:
```bash
python "hospital mangement system.py"
# or
python librarymangement.py
```
