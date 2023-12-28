import os
import json
import sys


def delet_2point(folder_path):
    # Iterate through each file in the input folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            input_file_path = os.path.join(folder_path, filename)

            # Load the data from the input file
            with open(input_file_path, 'r') as json_file:
                data = json.load(json_file)
                print("\nbefore: " + str(data))

                # for shape in data['shapes']:
                #     print(shape['points'])
                #     print("len: " + str(len(shape['points'])))
                # sys.exit()

                new_shapes = [shape for shape in data["shapes"] if len(shape["points"]) == 2]
                data["shapes"] = new_shapes
                print("\nafter: " + str(data))
                print("------file name: " + filename + "------------\n")

            # Save the modified data to the output folder
            output_file_path = os.path.join(folder_path, filename)
            with open(output_file_path, 'w') as output_file:
                json.dump(data, output_file, indent=2)

# Example usage
folder_path = r"Z:\de-identification\Kakaomobility\round(20220906111759_autocardata_100)_time(1662435830_1662435858)\sensor\camera(00)\faces"

delet_2point(folder_path)