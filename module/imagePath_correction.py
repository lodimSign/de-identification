import json
import os
import re
import sys

# JSON 파일들이 저장된 디렉토리 경로
source_folder = r'Z:\de-identification\Kakaomobility\round(20230320124231_autocardata_100)_time(1679288227_1679288270)\sensor\camera(04)\personIDs'

def find_json_files(folder):
    json_files = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))

    return json_files

# "images" 폴더를 추가한 새로운 경로 생성 함수
def imagePath_correction(old_path):
    filename = os.path.basename(old_path.split('.')[0])
    new_path = '..\images\\' + filename + '.png'

    return new_path

json_files = find_json_files(source_folder)


# 모든 JSON 파일을 반복 처리
for json_path in json_files:
    # JSON 파일 읽어오기
    with open(json_path, 'r') as json_file:
        json_data = json.load(json_file)

    # "imagePath" 수정
    new_imagePath = imagePath_correction(json_path)

    # 수정된 JSON 데이터를 다시 파일에 쓰기 (덮어쓰기)
    print("---new_imagePath: "+new_imagePath)
    json_data["imagePath"] = new_imagePath
    with open(json_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)
        print(json_data)

    print(f"---Updated {json_path}")