import os
import json

# 폴더 경로 지정
input_folder_path = r"C:\workspace\datasets\personIDs"
output_folder_path = input_folder_path

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# 폴더 내의 모든 파일에 대해 처리
for filename in os.listdir(input_folder_path):
    if filename.endswith('.json'):
        # JSON 파일 경로 생성
        json_file_path = os.path.join(output_folder_path, filename)

        # JSON 파일 읽어오기
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)

        for shape in json_data.get("shapes", []):
            # if shape.get("group_id", 0) >= 6:
            shape["group_id"] = int(shape.get("group_id", 0)) - 3
            print(shape)

        # 수정된 JSON 파일 저장
        with open(json_file_path, 'w') as file:
            json.dump(json_data, file, indent=2)

print("Processing completed.")