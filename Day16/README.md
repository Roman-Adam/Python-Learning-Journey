# Day 16 – Coffee Machine using OOP

## Overview

Day 16 of my Python learning journey focused on **Object-Oriented Programming (OOP)**.

For the final project, I rebuilt the Coffee Machine program using classes and objects. This project helped me understand how OOP can make a program more organized and easier to manage.

## Topics Learned

* Object-Oriented Programming (OOP)
* Classes
* Objects
* Attributes
* Methods
* Creating objects
* Dot notation
* Python packages
* Using modules
* Working with multiple Python files
* Basic OOP project structure

## Final Project: Coffee Machine

The Coffee Machine allows the user to:

* Choose a coffee
* Check available resources
* Insert coins
* Calculate payment
* Return change
* Make coffee
* View machine reports
* Turn the machine off

## Project Structure

```text
Day16/
│
├── main.py
├── menu.py
├── coffee_maker.py
└── money_machine.py
```

### Files

**main.py**
Controls the main Coffee Machine program.

**menu.py**
Contains the coffee menu and menu items.

**coffee_maker.py**
Manages resources and makes the selected coffee.

**money_machine.py**
Handles coins, payments, change, and profit.

## How the Program Works

```text
User selects coffee
        ↓
Find coffee
        ↓
Check resources
        ↓
Resources available?
   ↓             ↓
  No            Yes
   ↓             ↓
Show error    Take payment
                 ↓
           Payment successful?
             ↓           ↓
            No          Yes
             ↓           ↓
           Refund    Make coffee
                         ↓
                   Serve coffee
```

## Example Commands

```text
espresso
latte
cappuccino
report
off
```

## What I Practiced

Through this project, I practiced:

* Creating classes
* Creating objects
* Using attributes
* Creating methods
* Importing classes from other files
* Using objects with dot notation
* Organizing a Python project into multiple modules
* Applying OOP concepts to a real project

## What I Learned

The most important lesson from Day 16 was understanding how **classes and objects can be used to organize a program**.

Instead of keeping everything in one large program, different responsibilities can be separated into different classes.

## Technologies Used

* Python 3
* Object-Oriented Programming
* Python Modules

## Author

**Roman Bibi**

This project is part of my **100 Days of Python Learning Journey**.
