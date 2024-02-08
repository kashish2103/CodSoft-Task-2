import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length should be a positive integer.")
        
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Password Generator")
root.configure(bg="pink")


length_label = tk.Label(root, text="Password Length:",bg="pink",fg="black")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)


generate_button = tk.Button(root, text="Generate Password", command=generate_password,)
generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


password_entry = tk.Entry(root)
password_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
