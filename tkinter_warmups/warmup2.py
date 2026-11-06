import tkinter as tk
from tkinter import ttk

def add_row(row, text, widget):
    ttk.Label(form, text=text).grid(row=row, column=0, sticky="e", padx=4, pady=4)
    widget.grid(row=row, column=1, sticky="ew", padx=4, pady=4)

def parse_float(text, name):
    try:
        return float(text)
    except ValueError:
        raise ValueError(f"{name} must be a number.")
    
def submit(event=None):
    symbol = symbol_entry.get().strip().upper()
    side = side_box.get()
    try:
        if not symbol:
            raise ValueError("Symbol is required.")
        
        entry_price = parse_float(entry_price_entry.get(), "Entry price")
        exit_price = parse_float(exit_price_entry.get(), "Exit price")
        fee_price = parse_float((fees_entry.get() or 0), "Fee price")
        size = parse_float(size_entry.get(), "Size")

        if size <= 0:
            raise ValueError("Size must be greater than zero.")
    except ValueError as e:
        result_label.config(text=str(e), foreground="red")
        return
    
    if side == "Long":
        pnl = ((exit_price - entry_price) * size * 5) - (fee_price * size)
    else:
        pnl = ((entry_price - exit_price) * size * 5) - (fee_price * size)

    if pnl < 0:
        result_label.config(text=f"{symbol} {side}: P&L {pnl:+,.2f}", foreground="red")
    elif pnl > 0:
        result_label.config(text=f"{symbol} {side}: P&L {pnl:+,.2f}", foreground="green")
    else:
        result_label.config(text=f"{symbol} {side}: P&L {pnl:+,.2f}", foreground="black")

def clear(event=None):
    symbol_entry.delete(0, tk.END)
    side_box.current(0)
    entry_price_entry.delete(0, tk.END)
    exit_price_entry.delete(0, tk.END)
    size_entry.delete(0, tk.END)
    fees_entry.delete(0, tk.END)
    result_label.config(text="", foreground="black")
    symbol_entry.focus()

root = tk.Tk()
root.title("Warm-up 2: Trade Form")
root.columnconfigure(0, weight=1)

form = ttk.Frame(root, padding=12)
form.grid(row=0, column=0, sticky="nsew")
form.columnconfigure(1, weight=1)

symbol_entry = ttk.Entry(form)
side_box = ttk.Combobox(form, values=["Long", "Short"], state="readonly")
side_box.current(0)
entry_price_entry = ttk.Entry(form)
exit_price_entry = ttk.Entry(form)
size_entry = ttk.Entry(form)
fees_entry = ttk.Entry(form)

add_row(0, "Symbol:", symbol_entry)
add_row(1, "Side:", side_box)
add_row(2, "Entry price:", entry_price_entry)
add_row(3, "Exit price:", exit_price_entry)
add_row(4, "Size:", size_entry)
add_row(5, "Fees:", fees_entry)

button_frame = ttk.Frame(form)
button_frame.grid(row=6, column=1, pady=10)

ttk.Button(button_frame, text="Submit", command=submit).pack(side="left", padx=2)
ttk.Button(button_frame, text="Clear", command=clear).pack(side="right", padx=2)

result_label = ttk.Label(form, text="")
result_label.grid(row=7, column=0, columnspan=2)

symbol_entry.focus()
root.bind("<Return>", submit)

root.mainloop()