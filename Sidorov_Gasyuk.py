import os
import tkinter as tk
from tkinter import messagebox, simpledialog

def create_directory():
    dirname = simpledialog.askstring("Create Directory", "Enter directory name:")
    if dirname:
        try:
            os.mkdir(dirname)
            messagebox.showinfo("Success", "Directory created successfully!")
        except FileExistsError:
            messagebox.showerror("Error", "Directory already exists!")

def delete_file_or_directory():
    path = simpledialog.askstring("Delete File/Directory", "Enter path:")
    if path:
        try:
            if os.path.isdir(path):
                os.rmdir(path)
                messagebox.showinfo("Success", "Directory deleted successfully!")
            else:
                os.remove(path)
                messagebox.showinfo("Success", "File deleted successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "File/Directory not found!")
        except OSError:
            messagebox.showerror("Error", "Unable to delete directory. Directory is not empty!")

def rename_file_or_directory():
    old_path = simpledialog.askstring("Rename File/Directory", "Enter old path:")
    if old_path:
        new_path = simpledialog.askstring("Rename File/Directory", "Enter new path:")
    if new_path:
        try:
            os.rename(old_path, new_path)
            messagebox.showinfo("Success", "File/Directory renamed successfully!")
        except FileNotFoundError:
            messagebox.showerror("Error", "File/Directory not found!")
        except FileExistsError:
            messagebox.showerror("Error", "New path already exists!")

root = tk.Tk()
root.title("File Manager")

create_button = tk.Button(root, text="Create Directory", command=create_directory)
create_button.pack()

delete_button = tk.Button(root, text="Delete File/Directory", command=delete_file_or_directory)
delete_button.pack()

rename_button = tk.Button(root, text="Rename File/Directory", command=rename_file_or_directory)
rename_button.pack()
root.geometry("150x100")
root.mainloop()
