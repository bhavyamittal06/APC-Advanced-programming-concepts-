
import tkinter as tk
from tkinter import filedialog, messagebox

# Create the main window
root = tk.Tk()
root.title("My Notepad")
root.geometry("700x500")

# Create text area
text_area = tk.Text(root, font=("Arial", 14), wrap="word")
text_area.pack(expand=True, fill="both")

# Create a new file
def new_file():
    text_area.delete("1.0", tk.END)

# Open an existing file
def open_file():
    file = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file:
        with open(file, "r") as f:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, f.read())

# Save the file
def save_file():
    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file:
        with open(file, "w") as f:
            f.write(text_area.get("1.0", tk.END))
        messagebox.showinfo("Success", "File saved successfully!")

# Create menu bar
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Run the application
root.mainloop()
