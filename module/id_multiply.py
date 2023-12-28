import os
import json

# 폴더 경로 지정
folder_path = r"Z:\de-identification\Kakaomobility\round(20220906111759_autocardata_100)_time(1662436882_1662436931)\sensor\camera(05)\personIDs"

# Create the output folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 폴더 내의 모든 파일에 대해 처리
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        # JSON 파일 경로 생성
        json_file_path = os.path.join(folder_path, filename)

        # JSON 파일 읽어오기
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)

        # group_id에 100 곱하기
        for shape in json_data.get("shapes", []):
            shape["group_id"] = int(shape.get("group_id", 0)) * 100
            print(shape)

        # # group_id가 100보다 큰 경우: group_id에 100 나누기
        # for shape in json_data.get("shapes", []):
        #     if shape.get("group_id", 0) >= 100:
        #         shape["group_id"] = int(shape.get("group_id", 0) / 100)
        #         print(shape)

        # for shape in json_data.get("shapes", []):
        #     shape["group_id"] = int(shape.get("group_id", 0))
        #     print(shape)

        # 수정된 JSON 파일 저장
        with open(json_file_path, 'w') as file:
            json.dump(json_data, file, indent=2)

print("Processing completed.")