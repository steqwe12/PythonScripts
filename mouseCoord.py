import pyautogui
from tkinter import *

def update_coordinates_label():
    x, y = pyautogui.position()
    coordinates_label.config(text=f"X: {x}, Y: {y}")
    coordinates_label.after(100, update_coordinates_label)

# Create GUI window
root = Tk()
root.title("Mouse Coordinates Tracker")
root.geometry("300x100")

# Create label to display coordinates
coordinates_label = Label(root, text="")
coordinates_label.pack()

# Start updating coordinates label
update_coordinates_label()

# Run the GUI
root.mainloop()