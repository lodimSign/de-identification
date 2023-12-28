import glob
import os
import tkinter as tk
from tkinter import filedialog

def browse_images_path():
    folder_selected = filedialog.askdirectory()
    images_path_var.set(folder_selected)

def browse_delete_check_paths():
    folder_selected = filedialog.askdirectory()
    delete_check_paths_var.set(folder_selected)

# Create the main window
root = tk.Tk()
root.title("Path Configurator")

# Variables to store the paths
images_path_var = tk.StringVar()
delete_check_paths_var = tk.StringVar()

# GUI components
tk.Label(root, text="Images Path:").grid(row=0, column=0)
tk.Entry(root, textvariable=images_path_var, width=50).grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_images_path).grid(row=0, column=2)

tk.Label(root, text="Delete Check Paths:").grid(row=1, column=0)
tk.Entry(root, textvariable=delete_check_paths_var, width=50).grid(row=1, column=1)
tk.Button(root, text="Browse", command=browse_delete_check_paths).grid(row=1, column=2)

def process_paths():
    images_path = images_path_var.get()
    delete_check_paths = delete_check_paths_var.get()

    # images 폴더의 파일 목록 가져오기
    files_in_images_path = os.listdir(images_path)
    print("-----" + str(files_in_images_path))
    print(len(files_in_images_path))

    # delete_check 필요한 폴더들의 파일 목록 가져오기
    for delete_check_path in glob.glob(delete_check_paths):
        if 'faces' in delete_check_path or 'plates' in delete_check_path or 'personIDs' in delete_check_path:
            # delete_check_path 폴더 내의 모든 파일 찾기
            delete_check_files = os.listdir(delete_check_path)
            print("-----" + str(delete_check_files))
            print("" + str(len(delete_check_files)) + '\n')

            num = 1

            # delete_check 필요한 폴더 파일 중, images 폴더에 없는 파일 삭제
            for delete_check_file_name in delete_check_files:
                delete_check_file_name_with_extension = delete_check_file_name.split('.')[0] + '.png'
                delete_check_file_path = os.path.join(delete_check_path, delete_check_file_name)

                # 파일이 images 폴더에 없으면 삭제
                if delete_check_file_name_with_extension not in files_in_images_path:
                    print(f"NO.{num}: {delete_check_file_name}")
                    num += 1

                    # 파일 삭제
                    # os.remove(delete_check_file_path)
                    print(f"Deleted: {delete_check_file_path}")

        else:
            continue


# Button to trigger processing
tk.Button(root, text="Process Paths", command=process_paths).grid(row=2, column=1)

# Run the GUI
root.mainloop()