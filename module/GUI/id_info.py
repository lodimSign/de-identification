import json
import os
import tkinter as tk
from tkinter import filedialog

# Function to handle button click and set the folder path
def browse_folder():
    folder_selected = filedialog.askdirectory()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, folder_selected)

# Function to process the files in the selected folder
def process_folder():
    input_folder_path = entry_path.get()

    # Rest of your code for processing the folder
    assigned_ids = {}
    for filename in os.listdir(input_folder_path):
        if filename.endswith(".json"):
            input_file_path = os.path.join(input_folder_path, filename)

            with open(input_file_path, 'r') as json_file:
                data = json.load(json_file)

                for shape in data['shapes']:
                    group_id = shape['group_id']
                    label = shape['label']

                    # Check if the combination of group_id and label has been assigned an ID
                    if (group_id, label) not in assigned_ids:
                        # Assign a new ID for the combination
                        assigned_ids[(group_id, label)] = len(assigned_ids) + 1
                        print('NO.' + str(len(assigned_ids)) + ' / ' + 'label: ' + str(label) + ', ID: ' + str(group_id))

    print("---------------end---------------")

# Create the main window
root = tk.Tk()
root.title("Folder Path Input")

# Create and place the entry widget for the folder path
entry_path = tk.Entry(root, width=50)
entry_path.grid(row=0, column=0, padx=10, pady=10)

# Create and place the "Browse" button
btn_browse = tk.Button(root, text="Browse", command=browse_folder)
btn_browse.grid(row=0, column=1, padx=10, pady=10)

# Create and place the "Process" button
btn_process = tk.Button(root, text="Process Folder", command=process_folder)
btn_process.grid(row=1, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
