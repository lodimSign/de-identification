import json
import os
import sys

input_folder_path = r"Z:\de-identification\Kakaomobility\round(20220906111759_autocardata_100)_time(1662436938_1662436983)\sensor\camera(05)\personIDs"

count_box_total = 0

# Iterate through each file in the input folder
for filename in os.listdir(input_folder_path):
    if filename.endswith(".json"):
        input_file_path = os.path.join(input_folder_path, filename)

    # Load the data from the input file
    try:
        with open(input_file_path, 'r') as json_file:
            data = json.load(json_file)
            print("json_file: ", input_file_path)

            # "shapes" 배열의 길이 출력
            count = len(data["shapes"])
            print("Number of shapes:", count)
            count_box_total += count
            print("---count_box_total: ", count_box_total)
    except:
        print("ERROR!")
