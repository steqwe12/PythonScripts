import tkinter as tk
from tkinter import simpledialog

def make_always_on_top(window):
    # Use ctypes to set the window to be always on top
    import ctypes
    user32 = ctypes.windll.user32
    user32.SetWindowPos(window.winfo_id(), -1, 0, 0, 0, 0, 0x0001)

class AlwaysOnTopTextBox(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Always On Top Text Box")
        self.geometry("300x100")
        
        self.text_box = tk.Text(self, wrap='word', height=5)
        self.text_box.pack(expand=True, fill='both')
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Make the window always on top
        self.attributes('-topmost', True)
        self.after(10, lambda: make_always_on_top(self))

    def on_closing(self):
        self.destroy()

if __name__ == "__main__":
    app = AlwaysOnTopTextBox()
    app.mainloop()
