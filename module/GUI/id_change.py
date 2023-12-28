import os
import json
import tkinter as tk
from tkinter import filedialog

def id_change(input_folder, output_folder, find_label, find_id, new_label, new_id):
    # Dictionary to store assigned IDs for each group_id and label combination
    assigned_ids = {}

    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            input_file_path = os.path.join(input_folder, filename)

            # Load the data from the input file
            with open(input_file_path, 'r') as json_file:
                data = json.load(json_file)

                # Iterate through each shape in the JSON data
                for shape in data['shapes']:
                    group_id = shape['group_id']
                    label = shape['label']

                    if label==find_label and str(group_id)==find_id:
                        shape['label'] = new_label
                        shape['group_id'] = int(new_id)
                        print(shape)

            # Save the modified data to the output folder
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
    new_label = entry_new_label.get()
    new_id = entry_new_id.get()

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # result = unique_ids(input_folder_path, output_folder_path, str(find_label), find_id, str(new_label), new_id)
    result = id_change(input_folder_path, output_folder_path, str(find_label), str(find_id), str(new_label), str(new_id))

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

tk.Label(root, text="New Label:").grid(row=4, column=0, padx=10, pady=5)
entry_new_label = tk.Entry(root)
entry_new_label.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="New ID:").grid(row=5, column=0, padx=10, pady=5)
entry_new_id = tk.Entry(root)
entry_new_id.grid(row=5, column=1, padx=10, pady=5)

# Process Button
btn_process = tk.Button(root, text="Process Folders", command=process_folders)
btn_process.grid(row=6, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
