from tkinter import *
import customtkinter as ctk
import tkinter as tk



ctk.set_appearance_mode("system")

ctk.set_default_color_theme("blue")



root =ctk.CTk()
root.title("Luna")
root.resizable(False, False)
root.lift()

root.geometry("400x400")

switch_var = ctk.BooleanVar()






def update_label_text():
    if switch_var.get():
        label.config(text="Luna is listening")
    else:
        label.config(text="Luna is sleeping")

label = tk.Label(root, text="Luna is sleeping")
label.pack(padx=10, pady=30)


def switch_event():
    print( switch_var.get())
  

switch_1 = ctk.CTkSwitch(master=root, text="mode", command=update_label_text,
                                   variable=switch_var, onvalue=1, offvalue=0)
switch_1.pack(padx=20, pady=10)











root.mainloop()