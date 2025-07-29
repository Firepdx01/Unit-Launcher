import tkinter as tk

def start_timer():
    try:
        seconds = int(entry.get())
        countdown(seconds)
    except ValueError:
        label.config(text="Please enter a valid number")

def countdown(seconds):
    if seconds >= 0:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=time_format)
        root.after(1000, countdown, seconds - 1)
    else:
        label.config(text="Time's up!")

# Create main window
root = tk.Tk()
root.title("Countdown Timer")

# Inpu
