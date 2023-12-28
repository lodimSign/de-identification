import os
import json
import tkinter as tk
from tkinter import filedialog

def unique_ids(input_folder, output_folder):
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

                    # Check if the combination of group_id and label has been assigned an ID
                    if (group_id, label) not in assigned_ids:
                        # Assign a new ID for the combination
                        assigned_ids[(group_id, label)] = len(assigned_ids) + 1

                    # Update the shape with the assigned ID
                    shape['group_id'] = assigned_ids[(group_id, label)]

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

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    result = unique_ids(input_folder_path, output_folder_path)

    # Print the assigned IDs for each group_id and label combination
    print(result)

# Create the main window
root = tk.Tk()
root.title("Unique IDs Processor")

# Create and place the entry widget for the input folder path
entry_input = tk.Entry(root, width=50)
entry_input.grid(row=0, column=0, padx=10, pady=10)

# Create and place the "Browse" button for the input folder
btn_browse_input = tk.Button(root, text="Browse Input", command=browse_input_folder)
btn_browse_input.grid(row=0, column=1, padx=10, pady=10)

# Create and place the entry widget for the output folder path
entry_output = tk.Entry(root, width=50)
entry_output.grid(row=1, column=0, padx=10, pady=10)

# Create and place the "Browse" button for the output folder
btn_browse_output = tk.Button(root, text="Browse Output", command=browse_output_folder)
btn_browse_output.grid(row=1, column=1, padx=10, pady=10)

# Create and place the "Process" button
btn_process = tk.Button(root, text="Process Folders", command=process_folders)
btn_process.grid(row=2, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()