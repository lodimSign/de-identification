import os
import json
import tkinter as tk
from tkinter import ttk, filedialog

def browse_folder(entry_widget):
    folder_selected = filedialog.askdirectory()
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, folder_selected)

def id_info(input_folder_path):
    assigned_ids = {}
    for filename in os.listdir(input_folder_path):
        if filename.endswith(".json"):
            input_file_path = os.path.join(input_folder_path, filename)

            with open(input_file_path, 'r') as json_file:
                data = json.load(json_file)

                for shape in data['shapes']:
                    group_id = shape['group_id']
                    label = shape['label']

                    if (group_id, label) not in assigned_ids:
                        assigned_ids[(group_id, label)] = len(assigned_ids) + 1
                        print('NO.' + str(len(assigned_ids)) + ' / ' + 'label: ' + str(label) + ', ID: ' + str(group_id))

    print("---------------end---------------")

def id_delete(input_folder, output_folder, find_label, find_id):
    assigned_ids = {}

    consecutive_frames = 0
    consecutive_count = 0

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            input_file_path = os.path.join(input_folder, filename)

            with open(input_file_path, 'r') as json_file:
                data = json.load(json_file)

                for shape in data['shapes']:
                    group_id = shape['group_id']
                    label = shape['label']

                    if label == find_label and group_id == int(find_id):
                        data['shapes'].remove(shape)
                        print('deleted / '+ 'label: ' + str(label) + ', ID: ' + str(group_id) +
                              ', ---filename: ' + str(filename))
                        consecutive_count = 1

            output_file_path = os.path.join(output_folder, filename)
            with open(output_file_path, 'w') as output_file:
                json.dump(data, output_file, indent=2)

        if consecutive_count == 1:
            consecutive_frames += 1  # Increment the counter for consecutive frames not satisfying the condition
        if consecutive_frames >= 50:
            break

    print("---------------end---------------")

    return assigned_ids

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
    print(assigned_ids)
    print("---------------end---------------")

    return assigned_ids

def id_change(input_folder, output_folder, find_label, find_id, new_label, new_id):
    # Dictionary to store assigned IDs for each group_id and label combination
    assigned_ids = {}

    consecutive_frames = 0
    consecutive_count = 0

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

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
                        print('changed / '+ 'label: ' + str(label) + '=> ' + str(find_label) +
                              ', ID: ' + str(group_id) +'=> ' + str(new_id) +
                              ', ---filename: ' + str(filename))
                        consecutive_count = 1
        if consecutive_count == 1:
            consecutive_frames += 1  # Increment the counter for consecutive frames not satisfying the condition
        if consecutive_frames >= 50:
            break

            # Save the modified data to the output folder
            output_file_path = os.path.join(output_folder, filename)
            with open(output_file_path, 'w') as output_file:
                json.dump(data, output_file, indent=2)
    print("---------------change end---------------")
    return assigned_ids

def id_plus(input_folder, output_folder, num):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 폴더 내의 모든 파일에 대해 처리
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            # JSON 파일 경로 생성
            json_file_path = os.path.join(input_folder, filename)

            # JSON 파일 읽어오기
            with open(json_file_path, 'r') as file:
                json_data = json.load(file)

            for shape in json_data.get("shapes", []):
                id_before = shape['group_id']
                shape["group_id"] = int(shape.get("group_id", 0)) + int(num)
                print('ID: ' + str(id_before) + '=> ' + str(shape['group_id']) + ', ----- changed filename: ' + str(filename))

        # 수정된 JSON 파일 저장
        with open(json_file_path, 'w') as file:
            json.dump(json_data, file, indent=2)

    print("---------------plus end---------------")

def id_multiply(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 폴더 내의 모든 파일에 대해 처리
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            # JSON 파일 경로 생성
            json_file_path = os.path.join(input_folder, filename)

            # JSON 파일 읽어오기
            with open(json_file_path, 'r') as file:
                json_data = json.load(file)

            # group_id에 100 곱하기
            for shape in json_data.get("shapes", []):
                id_before = shape['group_id']
                shape["group_id"] = int(shape.get("group_id", 0)) * 100
                print('ID: ' + str(id_before) + '=> ' + str(shape['group_id']) + ', ----- changed filename: ' + str(filename))

        # 수정된 JSON 파일 저장
        with open(json_file_path, 'w') as file:
            json.dump(json_data, file, indent=2)

    print("---------------multiply end---------------")

def id_devide(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 폴더 내의 모든 파일에 대해 처리
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            # JSON 파일 경로 생성
            json_file_path = os.path.join(input_folder, filename)

            # JSON 파일 읽어오기
            with open(json_file_path, 'r') as file:
                json_data = json.load(file)

            # group_id가 100보다 큰 경우: group_id에 100 나누기
            for shape in json_data.get("shapes", []):
                id_before = shape['group_id']
                if shape.get("group_id", 0) >= 100:
                    shape["group_id"] = int(shape.get("group_id", 0) / 100)
                    print('ID: ' + str(id_before) + '=> ' + str(shape['group_id'])
                          + ', ----- changed filename: ' + str(filename))

        # 수정된 JSON 파일 저장
        with open(json_file_path, 'w') as file:
            json.dump(json_data, file, indent=2)

    print("---------------devide end---------------")

def create_info_tab(root, tab_title, tab_index):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=tab_title)

    # Entry widget for folder path
    entry_path = tk.Entry(tab, width=50)
    entry_path.grid(row=0, column=0, padx=10, pady=10)

    # "Browse" button
    btn_browse = tk.Button(tab, text="Browse", command=lambda: browse_folder(entry_path))
    btn_browse.grid(row=0, column=1, padx=10, pady=10)

    # "Process" button
    btn_process = tk.Button(tab, text="Process Folder", command=lambda: id_info(entry_path.get()))
    btn_process.grid(row=1, column=0, columnspan=2, pady=10)

    return tab

def create_delete_tab(root, tab_title, tab_index):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=tab_title)

    # Input Folder Section
    tk.Label(tab, text="Input Folder:").grid(row=2, column=0, padx=10, pady=5)
    entry_input = tk.Entry(tab, width=50)
    entry_input.grid(row=2, column=1, padx=10, pady=5)
    btn_browse_input = tk.Button(tab, text="Browse", command=lambda: browse_folder(entry_input))
    btn_browse_input.grid(row=2, column=2, padx=10, pady=5)

    # Output Folder Section
    tk.Label(tab, text="Output Folder:").grid(row=3, column=0, padx=10, pady=5)
    entry_output = tk.Entry(tab, width=50)
    entry_output.grid(row=3, column=1, padx=10, pady=5)
    btn_browse_output = tk.Button(tab, text="Browse", command=lambda: browse_folder(entry_output))
    btn_browse_output.grid(row=3, column=2, padx=10, pady=5)

    # Find and delete Values Section
    tk.Label(tab, text="Find Label:").grid(row=4, column=0, padx=10, pady=5)
    entry_find_label = tk.Entry(tab)
    entry_find_label.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(tab, text="Find ID:").grid(row=5, column=0, padx=10, pady=5)
    entry_find_id = tk.Entry(tab)
    entry_find_id.grid(row=5, column=1, padx=10, pady=5)

    # Process Button
    btn_process_folders = tk.Button(tab, text="Process Folders", command=lambda: id_delete(entry_input.get(), entry_output.get(), entry_find_label.get(), entry_find_id.get()))
    btn_process_folders.grid(row=6, column=0, columnspan=2, pady=10)

    return tab

def create_unique_tab(root, tab_title, tab_index):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=tab_title)

    # Input Folder Section
    tk.Label(tab, text="Input Folder:").grid(row=2, column=0, padx=10, pady=5)
    entry_input = tk.Entry(tab, width=50)
    entry_input.grid(row=2, column=1, padx=10, pady=5)
    btn_browse_input = tk.Button(tab, text="Browse", command=lambda: browse_folder(entry_input))
    btn_browse_input.grid(row=2, column=2, padx=10, pady=5)

    # Output Folder Section
    tk.Label(tab, text="Output Folder:").grid(row=3, column=0, padx=10, pady=5)
    entry_output = tk.Entry(tab, width=50)
    entry_output.grid(row=3, column=1, padx=10, pady=5)
    btn_browse_output = tk.Button(tab, text="Browse", command=lambda: browse_folder(entry_output))
    btn_browse_output.grid(row=3, column=2, padx=10, pady=5)

    # Process Button
    btn_process_folders = tk.Button(tab, text="Process Folders", command=lambda: unique_ids(entry_input.get(), entry_output.get()))
    btn_process_folders.grid(row=6, column=0, columnspan=2, pady=10)

    return tab

def create_change_tab(root, tab_title, tab_index):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=tab_title)

    # Input Folder Section
    tk.Label(tab, text="Input Folder:").grid(row=0, column=0, padx=10, pady=5)
    entry_input = tk.Entry(tab, width=50)
    entry_input.grid(row=0, column=1, padx=10, pady=5)
    btn_browse_input = tk.Button(tab, text="Browse", command=lambda: browse_folder(entry_input))
    btn_browse_input.grid(row=2, column=2, padx=10, pady=5)

    # Output Folder Section
    tk.Label(tab, text="Output Folder:").grid(row=1, column=0, padx=10, pady=5)
    entry_output = tk.Entry(tab, width=50)
    entry_output.grid(row=1, column=1, padx=10, pady=5)
    btn_browse_output = tk.Button(tab, text="Browse", command=lambda: browse_folder(entry_output))
    btn_browse_output.grid(row=3, column=2, padx=10, pady=5)

    # Find and Replace Values Section
    tk.Label(tab, text="Find Label:").grid(row=2, column=0, padx=10, pady=5)
    entry_find_label = tk.Entry(tab)
    entry_find_label.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(tab, text="Find ID:").grid(row=3, column=0, padx=10, pady=5)
    entry_find_id = tk.Entry(tab)
    entry_find_id.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(tab, text="New Label:").grid(row=4, column=0, padx=10, pady=5)
    entry_new_label = tk.Entry(tab)
    entry_new_label.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(tab, text="New ID:").grid(row=5, column=0, padx=10, pady=5)
    entry_new_id = tk.Entry(tab)
    entry_new_id.grid(row=5, column=1, padx=10, pady=5)

    # Process Button
    btn_process_folders = tk.Button(tab, text="Process Folders",
                                    command=lambda: id_change(entry_input.get(), entry_output.get(),
                                                              entry_find_label.get(), entry_find_id.get(),
                                                              entry_new_label.get(), entry_new_id.get()))
    btn_process_folders.grid(row=6, column=0, columnspan=2, pady=10)

    return tab

def create_plus_tab(root, tab_title, tab_index):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=tab_title)

    # Input Folder Section
    tk.Label(tab, text="Input Folder:").grid(row=2, column=0, padx=10, pady=5)
    entry_input = tk.Entry(tab, width=50)
    entry_input.grid(row=2, column=1, padx=10, pady=5)
    btn_browse_input = tk.Button(tab, text="Browse", command=lambda: browse_folder(entry_input))
    btn_browse_input.grid(row=2, column=2, padx=10, pady=5)

    # Output Folder Section
    tk.Label(tab, text="Output Folder:").grid(row=3, column=0, padx=10, pady=5)
    entry_output = tk.Entry(tab, width=50)
    entry_output.grid(row=3, column=1, padx=10, pady=5)
    btn_browse_output = tk.Button(tab, text="Browse", command=lambda: browse_folder(entry_output))
    btn_browse_output.grid(row=3, column=2, padx=10, pady=5)

    # Find and delete Values Section
    tk.Label(tab, text="plus or minus:").grid(row=4, column=0, padx=10, pady=5)
    entry_plus = tk.Entry(tab)
    entry_plus.grid(row=4, column=1, padx=10, pady=5)

    # Process Button
    btn_process_folders = tk.Button(tab, text="Process Folders",
                                    command=lambda: id_plus(entry_input.get(), entry_output.get(),
                                                            entry_plus.get()))
    btn_process_folders.grid(row=6, column=0, columnspan=2, pady=10)

    return tab

def create_multiply_tab(root, tab_title, tab_index):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=tab_title)

    # Input Folder Section
    tk.Label(tab, text="Input Folder:").grid(row=2, column=0, padx=10, pady=5)
    entry_input = tk.Entry(tab, width=50)
    entry_input.grid(row=2, column=1, padx=10, pady=5)
    btn_browse_input = tk.Button(tab, text="Browse", command=lambda: browse_folder(entry_input))
    btn_browse_input.grid(row=2, column=2, padx=10, pady=5)

    # Output Folder Section
    tk.Label(tab, text="Output Folder:").grid(row=3, column=0, padx=10, pady=5)
    entry_output = tk.Entry(tab, width=50)
    entry_output.grid(row=3, column=1, padx=10, pady=5)
    btn_browse_output = tk.Button(tab, text="Browse", command=lambda: browse_folder(entry_output))
    btn_browse_output.grid(row=3, column=2, padx=10, pady=5)

    # Process Button
    btn_process_folders = tk.Button(tab, text="Process Folders", command=lambda: id_multiply(entry_input.get(), entry_output.get()))
    btn_process_folders.grid(row=6, column=0, columnspan=2, pady=10)

    return tab

def create_devide_tab(root, tab_title, tab_index):
    tab = ttk.Frame(notebook)
    notebook.add(tab, text=tab_title)

    # Input Folder Section
    tk.Label(tab, text="Input Folder:").grid(row=2, column=0, padx=10, pady=5)
    entry_input = tk.Entry(tab, width=50)
    entry_input.grid(row=2, column=1, padx=10, pady=5)
    btn_browse_input = tk.Button(tab, text="Browse", command=lambda: browse_folder(entry_input))
    btn_browse_input.grid(row=2, column=2, padx=10, pady=5)

    # Output Folder Section
    tk.Label(tab, text="Output Folder:").grid(row=3, column=0, padx=10, pady=5)
    entry_output = tk.Entry(tab, width=50)
    entry_output.grid(row=3, column=1, padx=10, pady=5)
    btn_browse_output = tk.Button(tab, text="Browse", command=lambda: browse_folder(entry_output))
    btn_browse_output.grid(row=3, column=2, padx=10, pady=5)

    # Process Button
    btn_process_folders = tk.Button(tab, text="Process Folders", command=lambda: id_devide(entry_input.get(), entry_output.get()))
    btn_process_folders.grid(row=6, column=0, columnspan=2, pady=10)

    return tab



# Create the main window
root = tk.Tk()
root.title("Tabbed JSON Data Modifier")

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Create tabs
tab1 = create_info_tab(root, "id_info", 0)
tab2 = create_delete_tab(root, "id_delete", 1)
tab3 = create_unique_tab(root, "unique", 2)
tab4 = create_change_tab(root, "change", 3)
tab5 = create_plus_tab(root, "plus", 4)
tab6 = create_multiply_tab(root, "multiply", 5)
tab7 = create_devide_tab(root, "devide", 6)

# Start the Tkinter event loop
root.mainloop()