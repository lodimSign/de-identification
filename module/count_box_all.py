import json
import os
from glob import glob

def count_box_all(folder_path, result_txt_path):
    count_box_dict = {}  # Dictionary to store count_box_total for each folder path

    # Use glob to find all matching JSON files
    json_files = glob(os.path.join(folder_path, '**', '*.json'), recursive=True)

    # Iterate through each file
    for input_file_path in json_files:
        try:
            # Load the data from the input file
            with open(input_file_path, 'r') as json_file:
                data = json.load(json_file)
                print("json_file: ", input_file_path)

                # "shapes" 배열의 길이 출력
                count = len(data["shapes"])
                print("Number of shapes:", count)

                # Get the folder path excluding the filename
                folder_key = os.path.dirname(input_file_path)

                # Update the count_box_total for the folder path in the dictionary
                count_box_dict[folder_key] = count_box_dict.get(folder_key, 0) + count

                print("---count_box_total: ", count_box_dict[folder_key])
        except FileNotFoundError:
            print(f"File not found: {json_file}")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Save the results to the output file
    with open(result_txt_path, 'w') as output_file:
        for folder_key, count_box_total in count_box_dict.items():
            output_file.write(f"{folder_key}\ncount_box_total: {count_box_total}\n\n")

# Example usage
folder_path = r"Z:\de-identification\Kakaomobility\round*\*\*\*"
# result_txt_path = r"Z:\de-identification\Kakaomobility\count_box_all.txt"
result_txt_path = r"Z:\backup\de-identification\Kakaomobility\count_box_all_231218.txt"

count_box_all(folder_path, result_txt_path)