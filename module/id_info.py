import json
import os

input_folder_path = r"C:\workspace\datasets\personIDs"
# Dictionary to store assigned IDs for each group_id and label combination
assigned_ids = {}

# Iterate through each file in the input folder
for filename in os.listdir(input_folder_path):
    if filename.endswith(".json"):
        input_file_path = os.path.join(input_folder_path, filename)

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
                print('NO.' + str(len(assigned_ids)) + ' / ' + 'label: ' + str(label) + ', ID: ' + str(group_id))