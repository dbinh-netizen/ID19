"""

This module creates a tkinter application with multiple pop-up windows.

"""

import tkinter as tk
import random

def create_window():
    """Create a pop-up window with a random position."""
    popup = tk.Toplevel()
    popup.geometry("320x160")
    popup.title("Tràn ngập bộ...")

    frame = tk.Frame(popup, bg='white', padx=2, pady=2)
    frame.pack(expand=True, fill='both', padx=10, pady=10)

    inner_frame = tk.Frame(frame, bg='#FFCDCB')
    inner_frame.pack(expand=True, fill='both', padx=5, pady=5)

    label = tk.Label(inner_frame, text="Nhớ nhớ nhớ em!", bg='#FFCDCB', font=("Noto Sans", 16, "italic"))
    label.pack(expand=True)

    x = random.randint(0, popup.winfo_screenwidth())
    y = random.randint(0, popup.winfo_screenheight())
    popup.geometry(f"320x160+{x}+{y}")

def create_windows_with_delay(count=50, delay=200):
    """Create multiple windows with a delay."""
    if count > 0:
        create_window()
        root.after(delay, create_windows_with_delay, count-1, delay)

def on_click():
    """Handle button click to create windows with delay."""
    create_windows_with_delay()

def main_window():
    """Create the main window."""
    global root
    root = tk.Tk()
    root.geometry("420x210")
    root.title("Tmai needs the remedy.")
    root.configure(bg='#FFCDCB')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 420
    window_height = 210
    position_x = int((screen_width / 2) - (window_width / 2))
    position_y = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    button = tk.Button(root, text="Muốn nói là..", font=("Noto Sans", 24), bg='#FFCDCB', command=on_click)
    button.pack(expand=True)

    root.mainloop()

main_window()