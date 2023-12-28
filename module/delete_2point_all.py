import glob
import os
import json

def delet_2point_all(folder_path):
    # 모든 폴더 내부의 모든 json 파일을 저장할 리스트
    json_files = []
    file_counter = 0  # Counter for processed files

    for folder_path in glob.glob(folder_path):
        if 'faces' in folder_path or 'plates' in folder_path or 'personIDs' in folder_path:
            # 폴더 내의 모든 json 파일 찾기
            json_files.extend(glob.glob(os.path.join(folder_path, '*.json')))
            print(str(json_files) + '\n')
        else:
            continue

        # 찾은 모든 json 파일을 읽어오기
        for json_file in json_files:
            try:
                with open(json_file, 'r') as file:
                    data = json.load(file)
                    print("---file path:" + str(json_file))
                    print("before: " + str(data))

                    new_shapes = [shape for shape in data["shapes"] if len(shape["points"]) == 2]
                    data["shapes"] = new_shapes
                    print("after: " + str(data))
                    # print("---file name: " + json_file + "------------------------------------------------------------\n")

                # Save the modified data to the output folder
                output_file_path = os.path.join(folder_path, json_file)
                with open(output_file_path, 'w') as output_file:
                    json.dump(data, output_file, indent=2)

                file_counter += 1  # Increment the counter for each processed file
                print(f"{file_counter} / 30000\n")

            except FileNotFoundError:
                print(f"File not found: {json_file}")
            except Exception as e:
                print(f"An error occurred: {e}")

        json_files = []

# folder_path = r"Z:\de-identification\Kakaomobility_test\round*\*\*\*"
folder_path = r"Z:\de-identification\Kakaomobility\round*\*\*\*"
# Z:\de-identification\Kakaomobility\round()\sensor\camera(00)

delet_2point_all(folder_path)