
import tkinter as tk
from tkinter import messagebox
import threading
import subprocess
import time



script_path = "./script.py"

process = None
def run_script():
    global process
    try:
        process = subprocess.Popen(["python", script_path])
        messagebox.showinfo("Started", "Script started successfully!")
        time.sleep(1)  
        process.wait()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run script: {e}")

def stop_script():
    global process
    if process and process.poll() is None:
        process.terminate()
        process = None
        messagebox.showinfo("Stopped", "Script was stopped.")

def close_app():
    stop_script()
    root.destroy()

root = tk.Tk()
root.title("EDGY")

label = tk.Label(root, text="Click the tick to run the script, or the cross to close the app.")
label.pack(pady=10)

tick_button = tk.Button(root, text="✅", font=("Arial", 24), command=lambda: threading.Thread(target=run_script).start())
tick_button.pack(side=tk.LEFT, padx=20, pady=10)

cross_button = tk.Button(root, text="❌", font=("Arial", 24), command=close_app)
cross_button.pack(side=tk.RIGHT, padx=20, pady=10)

root.mainloop()
