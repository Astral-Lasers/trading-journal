import queue
import threading
import time
import tkinter as tk
from tkinter import ttk

count = 0
results = queue.Queue()

def tick():
    global count
    count += 1
    counter_label.config(text=f"Ticks: {count}")
    root.after(1000, tick)          # schedule myself again in 1 second

def blocking_task():
    status.config(text="Working (blocking)...")
    time.sleep(5)                   # stand-in for a slow request
    status.config(text="Blocking task done")

def after_task():
    status.config(text="Waiting with after()...")
    root.after(5000, lambda: status.config(text="after() task done"))

def worker():
    time.sleep(5)                   # runs in a separate thread
    results.put("Thread task done") # never touch widgets from here

def thread_task():
    status.config(text="Working in a thread...")
    threading.Thread(target=worker, daemon=True).start()
    root.after(100, check_queue)

def check_queue():
    try:
        msg = results.get_nowait()
    except queue.Empty:
        root.after(100, check_queue)   # nothing yet, check again soon
    else:
        status.config(text=msg)

root = tk.Tk()
root.title("Warm-up 3: Freezing")
root.geometry("320x220")

frame = ttk.Frame(root, padding=12)
frame.pack(fill="both", expand=True)

counter_label = ttk.Label(frame, text="Ticks: 0")
counter_label.pack(pady=4)
status = ttk.Label(frame, text="Idle")
status.pack(pady=4)

ttk.Button(frame, text="Blocking task", command=blocking_task).pack(pady=3)
ttk.Button(frame, text="after() task", command=after_task).pack(pady=3)
ttk.Button(frame, text="Thread task", command=thread_task).pack(pady=3)

tick()
root.mainloop()