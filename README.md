# Personal Finance Tracker

A beginner-friendly, console-based personal finance tracker built with Python.

## Features currently included

- Add income or expense transactions
- View all transactions
- Search transactions by transaction type (Income or Expense)
- Update a transaction amount by transaction ID
- Delete a transaction by transaction ID
- Display a basic financial summary

## Python concepts practiced

- Functions and modules
- Lists and dictionaries
- Loops and conditional statements
- User input and basic calculations

## How to run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python main.py
   ```

## Project structure

```text
personal-finance-tracker/
├── main.py
├── add.py
├── search.py
├── view_all.py
├── update.py
├── delete.py
├── financial_report.py
└── README.md
```

## Current limitations

- Transactions are held in a Python list and are not saved permanently after the program exits.
- Search currently implements transaction-type filtering; the other displayed search choices are not implemented yet.
- The financial report and transaction-management functions are a work in progress and may need additional validation and edge-case handling.
