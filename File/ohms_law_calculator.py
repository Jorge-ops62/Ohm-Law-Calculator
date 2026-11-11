"""
Ohm's Law and Power Calculator (window version)
-----------------------------------------------
Same program as the terminal version, but it runs in a small window
built with tkinter (which comes with Python, nothing to install).

The user picks what to find, types the two known values and clicks
Calculate. The window stays open so the user can keep calculating
until they click Quit.

My twist:
  1. Power can be found from ANY two known values (V and I, I and R, V and R).
  2. A HISTORY box lists every calculation made in the session.
"""

import tkinter as tk

history = []   # list that stores a text line for every calculation done


# ---------- Calculation functions (no window code in here) ----------
def find_voltage(current, resistance):
    """V = I x R"""
    voltage = current * resistance
    return f"Voltage = {current} A x {resistance} ohms = {voltage:.2f} V"


def find_current(voltage, resistance):
    """I = V / R"""
    if resistance == 0:                           # avoid dividing by zero
        raise ValueError("Resistance cannot be 0 (that would be a short circuit).")
    return f"Current = {voltage} V / {resistance} ohms = {voltage / resistance:.2f} A"


def find_resistance(voltage, current):
    """R = V / I"""
    if current == 0:                              # avoid dividing by zero
        raise ValueError("Current cannot be 0 when finding resistance.")
    return f"Resistance = {voltage} V / {current} A = {voltage / current:.2f} ohms"


def power_from_vi(voltage, current):
    """P = V x I"""
    return f"Power = {voltage} V x {current} A = {voltage * current:.2f} W"


def power_from_ir(current, resistance):
    """P = I squared x R"""
    power = current ** 2 * resistance
    return f"Power = {current} A squared x {resistance} ohms = {power:.2f} W"


def power_from_vr(voltage, resistance):
    """P = V squared / R"""
    if resistance == 0:                           # avoid dividing by zero
        raise ValueError("Resistance cannot be 0.")
    power = voltage ** 2 / resistance
    return f"Power = {voltage} V squared / {resistance} ohms = {power:.2f} W"


# Each mode: (text on the radio button, label 1, label 2, function to call)
MODES = [
    ("Voltage (from current and resistance)", "Current (A)", "Resistance (ohms)", find_voltage),
    ("Current (from voltage and resistance)", "Voltage (V)", "Resistance (ohms)", find_current),
    ("Resistance (from voltage and current)", "Voltage (V)", "Current (A)", find_resistance),
    ("Power (from voltage and current)", "Voltage (V)", "Current (A)", power_from_vi),
    ("Power (from current and resistance)", "Current (A)", "Resistance (ohms)", power_from_ir),
    ("Power (from voltage and resistance)", "Voltage (V)", "Resistance (ohms)", power_from_vr),
]


def read_number(entry, name):
    """Convert the text in an entry box to a non-negative float, or raise a clear error."""
    text = entry.get().strip()
    if text == "":
        raise ValueError(f"{name} is empty. Please type a number.")
    try:
        value = float(text)                       # convert text to a decimal number
    except ValueError:
        raise ValueError(f"{name} must be a number, you typed '{text}'.")
    if value < 0:
        raise ValueError(f"{name} cannot be negative.")
    return value


def main():
    window = tk.Tk()
    window.title("Ohm's Law and Power Calculator")
    window.resizable(False, False)

    mode = tk.IntVar(value=0)                     # which radio button is chosen

    def update_labels():
        """Change the two input labels to match the chosen calculation."""
        label1.config(text=MODES[mode.get()][1] + ":")
        label2.config(text=MODES[mode.get()][2] + ":")
        message.config(text="")

    def calculate():
        """Called when Calculate is clicked: read, calculate, show and store."""
        try:
            first = read_number(entry1, MODES[mode.get()][1])
            second = read_number(entry2, MODES[mode.get()][2])
            result = MODES[mode.get()][3](first, second)
        except ValueError as error:
            # Show a friendly message instead of crashing
            message.config(text=error, fg="red")
            return
        message.config(text=result, fg="green")
        history.append(result)
        history_box.insert(tk.END, f"{len(history)}. {result}")   # add to history list

    def clear_boxes():
        """Empty the two input boxes."""
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        message.config(text="")

    # Choice of calculation
    choice_frame = tk.LabelFrame(window, text="What do you want to find?", padx=10, pady=5)
    choice_frame.pack(padx=15, pady=10, fill="x")
    for index, mode_info in enumerate(MODES):
        tk.Radiobutton(choice_frame, text=mode_info[0], variable=mode,
                       value=index, command=update_labels).pack(anchor="w")

    # Input boxes
    input_frame = tk.Frame(window)
    input_frame.pack(pady=5)
    label1 = tk.Label(input_frame, text=MODES[0][1] + ":")
    label1.grid(row=0, column=0, sticky="e", pady=3)
    entry1 = tk.Entry(input_frame, width=12)
    entry1.grid(row=0, column=1, padx=5)
    label2 = tk.Label(input_frame, text=MODES[0][2] + ":")
    label2.grid(row=1, column=0, sticky="e", pady=3)
    entry2 = tk.Entry(input_frame, width=12)
    entry2.grid(row=1, column=1, padx=5)

    # Buttons
    button_frame = tk.Frame(window)
    button_frame.pack(pady=5)
    tk.Button(button_frame, text="Calculate", width=10, command=calculate).pack(side="left", padx=4)
    tk.Button(button_frame, text="Clear", width=10, command=clear_boxes).pack(side="left", padx=4)
    tk.Button(button_frame, text="Quit", width=10, command=window.destroy).pack(side="left", padx=4)

    # Answer / error message line
    message = tk.Label(window, text="", font=("Arial", 10, "bold"), wraplength=380)
    message.pack(pady=5)

    # History list
    history_frame = tk.LabelFrame(window, text="History", padx=5, pady=5)
    history_frame.pack(padx=15, pady=(0, 15), fill="x")
    history_box = tk.Listbox(history_frame, width=58, height=6)
    history_box.pack()

    window.mainloop()                             # keep the window open until Quit


# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()
