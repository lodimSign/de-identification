import os
import glob
import json


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
                        print(
                            'NO.' + str(len(assigned_ids)) + ' / ' + 'label: ' + str(label) + ', ID: ' + str(group_id))

    return assigned_ids


def get_ids(input_folder_paths):
    ids = []
    input_folder_paths = glob.glob(input_folder_paths)
    for input_folder in input_folder_paths:
        print(input_folder)
        ids.append(id_info(input_folder))

    # Flatten the list of dictionaries into a single dictionary
    merged_ids = {key: value for id_dict in ids for key, value in id_dict.items()}

    # Sort the merged dictionary by group_id and label
    sorted_ids = sorted(merged_ids.items(), key=lambda x: (str(x[0][0]), str(x[0][1])))

    # Print the sorted result
    print("---------------ID LIST---------------")
    for idx, ((group_id, label), assigned_id) in enumerate(sorted_ids, start=1):
        print(f'Sorted NO.{idx} / label: {label}, ID: {group_id}')

    return sorted_ids


def consecutively_from_1(ids):
    # Create a mapping of old IDs to new consecutive IDs
    id_mapping = {key: idx + 1 for idx, (key, _) in enumerate(ids)}

    # Print the mapping
    print("--------consecutively_from_1---------")
    for (group_id, label), new_id in id_mapping.items():
        print(f'Label: {label}, ID: {group_id} => {new_id}')

    return id_mapping


def old_id_to_new_id(id_mapping, input_folder_paths, output_folder_name):
    input_folder_paths = glob.glob(input_folder_paths)

    for input_folder_path in input_folder_paths:
        output_folder_path = input_folder_path.replace('personIDs', output_folder_name)

        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        # Iterate through each file in the input folder
        for filename in glob.glob(os.path.join(input_folder_path, '*.json')):
            input_file_path = filename

            # Load the data from the input file
            with open(input_file_path, 'r') as json_file:
                data = json.load(json_file)

                # Iterate through each shape in the JSON data
                for shape in data['shapes']:
                    group_id = shape['group_id']
                    label = shape['label']

                    # Update group_id with the new_id
                    new_id = id_mapping.get((group_id, label))
                    if new_id is not None:
                        shape['group_id'] = new_id
                        print(f'changed / Label: {label}, ID: {group_id} => {new_id}')

            # Save the modified data to the output folder
            output_file_path = os.path.join(output_folder_path, os.path.basename(filename))
            print("output_file_path: ", output_file_path)
            with open(output_file_path, 'w') as output_file:
                json.dump(data, output_file, indent=2)

    print("---------------change end---------------")


# input_folder_paths = r"Z:\de-identification\Kakaomobility\round(20230417095611_autocardata_100)_time(1681703130_1681703230)\sensor\camera*\personIDs"
output_folder_name = "personIDs_id_sort"
# output_folder_name = "Kakaomobility_id_sort"

round_folder_list = r"Z:\de-identification\Kakaomobility\round*"
round_folder_list = glob.glob(round_folder_list)

for round_folder in round_folder_list:
    input_folder_paths = os.path.join(round_folder, 'sensor\camera*\personIDs')

    ids = get_ids(input_folder_paths)
    id_mapping = consecutively_from_1(ids)
    old_id_to_new_id(id_mapping, input_folder_paths, output_folder_name)