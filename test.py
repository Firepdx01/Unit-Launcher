import tkinter as tk

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Timer")

        self.time = 0
        self.running = False

        self.label = tk.Label(root, text="0", font=("Arial", 40))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(side="left", padx=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer)
        self.stop_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side="left", padx=10)

    def update_timer(self):
        if self.running:
            self.time += 1
            self.label.config(text=str(self.time))
            self.root.after(1000, self.update_timer)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.update_timer()

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time = 0
        self.label.config(text="0")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
