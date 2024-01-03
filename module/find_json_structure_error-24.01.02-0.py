import os
import json
import requests


def find_error_folders(parent_folder, target_name):
    error_folders = []

    for folder, subfolders, files in os.walk(parent_folder):

        for index, current_folder in enumerate(subfolders):
            if current_folder == target_name:
                folder_path = os.path.join(folder, target_name)
                print("checking folder: ", folder_path)

                for filename in os.listdir(folder_path):
                    if filename.endswith(".json"):
                        file_path = os.path.join(folder_path, filename)

                    try:
                        with open(file_path, "r") as f:
                            data = json.load(f)
                    except json.decoder.JSONDecodeError as e:
                        error_folders.append(file_path)

    return error_folders


folder_path = r"Z:\de-identification\Kakaomobility"
target_name = "personIDs"
error_folders = find_error_folders(folder_path, target_name)
print("-------------error folder list-------------")
print(error_folders)