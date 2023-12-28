import os
import json
import tkinter as tk
from tkinter import filedialog

def id_delete(input_folder, output_folder, find_label, find_id):
    assigned_ids = {}

    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            input_file_path = os.path.join(input_folder, filename)

            with open(input_file_path, 'r') as json_file:
                data = json.load(json_file)

                for shape in data['shapes']:
                    group_id = shape['group_id']
                    label = shape['label']

                    if label == find_label and group_id == find_id:
                        data['shapes'].remove(shape)
                        print(f"Deleted shape: {shape}")

            output_file_path = os.path.join(output_folder, filename)
            with open(output_file_path, 'w') as output_file:
                json.dump(data, output_file, indent=2)

    return assigned_ids

def browse_input_folder():
    folder_selected = filedialog.askdirectory()
    entry_input.delete(0, tk.END)
    entry_input.insert(0, folder_selected)

def browse_output_folder():
    folder_selected = filedialog.askdirectory()
    entry_output.delete(0, tk.END)
    entry_output.insert(0, folder_selected)

def process_folders():
    input_folder_path = entry_input.get()
    output_folder_path = entry_output.get()

    find_label = entry_find_label.get()
    find_id = entry_find_id.get()
    find_id = int(find_id)
    print("find_label: "+find_label)
    print("type: " + str(type(find_label)))
    print("find_id: "+str(find_id))
    print("type: " + str(type(find_id)))

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    result = id_delete(input_folder_path, output_folder_path, find_label, find_id)

    # Print the assigned IDs for each group_id and label combination
    print(result)

# Create the main window
root = tk.Tk()
root.title("JSON Data Modifier")

# Input Folder Section
tk.Label(root, text="Input Folder:").grid(row=0, column=0, padx=10, pady=5)
entry_input = tk.Entry(root, width=50)
entry_input.grid(row=0, column=1, padx=10, pady=5)
btn_browse_input = tk.Button(root, text="Browse", command=browse_input_folder)
btn_browse_input.grid(row=0, column=2, padx=10, pady=5)

# Output Folder Section
tk.Label(root, text="Output Folder:").grid(row=1, column=0, padx=10, pady=5)
entry_output = tk.Entry(root, width=50)
entry_output.grid(row=1, column=1, padx=10, pady=5)
btn_browse_output = tk.Button(root, text="Browse", command=browse_output_folder)
btn_browse_output.grid(row=1, column=2, padx=10, pady=5)

# Find and Replace Values Section
tk.Label(root, text="Find Label:").grid(row=2, column=0, padx=10, pady=5)
entry_find_label = tk.Entry(root)
entry_find_label.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Find ID:").grid(row=3, column=0, padx=10, pady=5)
entry_find_id = tk.Entry(root)
entry_find_id.grid(row=3, column=1, padx=10, pady=5)

# Process Button
btn_process = tk.Button(root, text="Process Folders", command=process_folders)
btn_process.grid(row=6, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
