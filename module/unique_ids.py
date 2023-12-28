import os
import json

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

# Example usage
input_folder_path = r"Z:\de-identification\Kakaomobility\round(20220907192457_autocardata_100)_time(1662555077_1662555102)\sensor\camera(01)\personIDs"
output_folder_path = input_folder_path
# output_folder_path = r"Z:\de-identification\Kakaomobility\round(20220906111759_autocardata_100)_time(1662435830_1662435858)\sensor\camera(01)\personIDs_unique"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

result = unique_ids(input_folder_path, output_folder_path)

# Print the assigned IDs for each group_id and label combination
print(result)