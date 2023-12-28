import os
import json

def id_delete(input_folder, output_folder, find_label, find_id):
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

                    if label == find_label and group_id == find_id:
                        data['shapes'].remove(shape)
                        print(f"Deleted shape: {shape}")

            # Save the modified data to the output folder
            output_file_path = os.path.join(output_folder, filename)
            with open(output_file_path, 'w') as output_file:
                json.dump(data, output_file, indent=2)

    return assigned_ids

# Example usage
input_folder_path = r"C:\workspace\datasets\personIDs"
output_folder_path = input_folder_path
# output_folder_path = r"Z:\de-identification\Kakaomobility\round(20220906111759_autocardata_100)_time(1662435830_1662435858)\sensor\camera(01)\personIDs"

find_label = 0
find_id = 2

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

result = id_delete(input_folder_path, output_folder_path, str(find_label), find_id)