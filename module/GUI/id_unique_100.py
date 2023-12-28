import os
import json
import tkinter as tk
from tkinter import filedialog

def process_json_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            json_file_path = os.path.join(folder_path, filename)

            with open(json_file_path, 'r') as file:
                json_data = json.load(file)

            for shape in json_data.get("shapes", []):
                shape["group_id"] = int(shape.get("group_id", 0)) * 100
                print(shape)

            with open(json_file_path, 'w') as file:
                json.dump(json_data, file, indent=2)

    print("Processing completed.")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path_var.set(folder_selected)

def process_folder():
    folder_path = folder_path_var.get()
    process_json_files(folder_path)

# GUI setup
root = tk.Tk()
root.title("JSON Processor")

# Folder path entry
folder_path_var = tk.StringVar()
folder_path_entry = tk.Entry(root, textvariable=folder_path_var, width=50)
folder_path_entry.grid(row=0, column=0, padx=10, pady=10)

# Browse button
browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.grid(row=0, column=1, padx=10, pady=10)

# Process button
process_button = tk.Button(root, text="Process", command=process_folder)
process_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
