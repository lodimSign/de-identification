import glob
import os
import json

# 디렉토리 경로 설정
# directory_path = "C:\\workspace\\datasets\\ID_duplicate"
directory_path = r"Z:\de-identification\Kakaomobility\round*\*\camera*\*"

# 모든 파일 검사
for duplicate_check_folder_path in glob.glob(directory_path):
    if 'personIDs' in duplicate_check_folder_path:
        duplicate_check_file_paths = os.listdir(duplicate_check_folder_path)
    else:
        continue

    for duplicate_check_file_path in duplicate_check_file_paths:
        duplicate_check_file_path = os.path.join(duplicate_check_folder_path, duplicate_check_file_path)

        # JSON 파일 읽기
        with open(duplicate_check_file_path, "r") as file:
            data = json.load(file)

        # shapes 리스트에서 label과 group_id가 같은 경우 확인
        for i in range(len(data["shapes"])):
            for j in range(i + 1, len(data["shapes"])):
                shape1 = data["shapes"][i]
                shape2 = data["shapes"][j]

                if shape1["label"] == shape2["label"] and shape1["group_id"] == shape2["group_id"]:
                    print(f"File: {duplicate_check_file_path}, Label: {shape1['label']}, Group ID: {shape1['group_id']}")
                    break