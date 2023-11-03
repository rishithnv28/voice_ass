import tkinter as tk

# Function to update the label text
def update_label_text():
    if switch_var.get():
        label.config(text="Luna is listening")
    else:
        label.config(text="Luna is sleeping")

# Create the main window
root = tk.Tk()
root.title("Luna")

# Create a variable to store the switch state
switch_var = tk.BooleanVar()

# Create a switch (Checkbutton)
switch = tk.Checkbutton(root, text="Turn on Luna", variable=switch_var, command=update_label_text)
switch.pack()

# Create a label to display the status
label = tk.Label(root, text="")
label.pack()

# Initialize the label text based on the initial state of the switch
update_label_text()

# Run the Tkinter main loop
root.mainloop()
