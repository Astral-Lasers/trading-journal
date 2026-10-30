import tkinter as tk

def on_click(event=None):
    symbol = entry.get().strip()
    if symbol:
        result_label.config(text=f"Logged: {symbol.upper()}")
        entry.delete(0, tk.END)
    else:
        result_label.config(text="Type a symbol first.")

root = tk.Tk()
root.title("Warm-up 1")
root.geometry("300x150")

tk.Label(root, text="Symbol:").pack(pady=(12, 0))
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Submit", command=on_click).pack(pady=8)
entry.bind("<Return>", on_click)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()