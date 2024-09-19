import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        
        if length < 6:
            messagebox.showwarning("Warning", "Password length should be at least 6 characters for security.")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        
        password = ''.join(random.choice(characters) for _ in range(length))
        
        password_entry.delete(0, tk.END)  # Clear previous password
        password_entry.insert(0, password)  # Insert new password
        
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)

length_label = tk.Label(root, text="Enter the desired length of the password:")
length_label.pack(pady=10)

length_entry = tk.Entry(root, width=10)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="Generated Password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.pack()


root.mainloop()

