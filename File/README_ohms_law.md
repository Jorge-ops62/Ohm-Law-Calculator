# project Title
Ohm's Law and Power Calculator


## What it does
1. Shows a menu: find voltage, current, resistance or power.
2. Asks for the known values and gives the answer with units (V, A, ohms, W).
3. Returns to the menu so the user can do another calculation, until they choose Quit.

Formulas used: `V = I x R`, `I = V / R`, `R = V / I`, `P = V x I`.

## My twist
- **Power from any two values:** power can be found from voltage and current, current and resistance (`P = I² x R`), or voltage and resistance (`P = V² / R`).
- **Calculation history:** every answer is stored in a list. The user can view it at any time (option 5), and it is printed again as a session summary when the program quits.


## How to run
```
python ohms_law_calculator.py
```

## Sample output
```
=== Ohm's Law and Power Calculator ===

What do you want to find?
  1. Voltage (V)
  2. Current (A)
  3. Resistance (ohms)
  4. Power (W)
  5. Show history
  6. Quit
Choose 1-6: 1
  Enter current in amps (A): 2
  Enter resistance in ohms: 5

  ANSWER: Voltage = 2.0 A x 5.0 ohms = 10.00 V

Choose 1-6: 2
  Enter voltage in volts (V): 12
  Enter resistance in ohms: 0
  Error: resistance cannot be 0 (that would be a short circuit).

Choose 1-6: abc
  Invalid choice. Please type a number from 1 to 6.

Choose 1-6: 4
  Which two values do you know?
    1. Voltage and current   (P = V x I)
    2. Current and resistance (P = I squared x R)
    3. Voltage and resistance (P = V squared / R)
  Choose 1, 2 or 3: 2
  Enter current in amps (A): 2
  Enter resistance in ohms: 10

  ANSWER: Power = 2.0 A squared x 10.0 ohms = 40.00 W

Choose 1-6: 6

You did 2 calculation(s) this session:
  1. Voltage = 2.0 A x 5.0 ohms = 10.00 V
  2. Power = 2.0 A squared x 10.0 ohms = 40.00 W
Goodbye!
```

## What I Learned
Functions keep code organised. Separate functions for each formula made the program easy to read, test and reuse in both versions.
Never trust user input. try/except inside a while loop stopped crashes when I typed letters, and I also rejected negative numbers.
Division by zero is a real risk. Formulas like I = V / R break when R is 0, so I added checks with clear messages.
Menus need loops. A while True loop with break lets the program repeat until the user quits.
Lists can remember things. Storing each answer in a list gave me the history feature.
Windows are event-driven. In tkinter, the program waits for a button click instead of running top to bottom.
Next step: convert units like mA and kΩ automatically.

## Author
Adjarho Jorge, ND1 Mechatronics Engineering Engineering, YabaTech.

