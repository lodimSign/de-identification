import json
import os
import re
import sys

# JSON 파일들이 저장된 디렉토리 경로
source_folder = r'C:\workspace\datasets\Kakaomobility'
# source_folder = r'C:\workspace\datasets\Kakaomobility_6'

def find_json_files(folder):
    json_files = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".json"):
                json_files.append(os.path.join(root, file))

    return json_files

# "images" 폴더를 추가한 새로운 경로 생성 함수
def update_json_contents(old_path):
    if "faces" in old_path:
        new_path = old_path.replace("faces", "images")
    elif "plates" in old_path:
        new_path = old_path.replace("plates", "images")

    new_path = new_path.split('.')[0] + '.png'
    return new_path

json_files = find_json_files(source_folder)

# 모든 JSON 파일을 반복 처리
for json_path in json_files:
    # JSON 파일 읽어오기
    with open(json_path, 'r') as json_file:
        json_data = json.load(json_file)

    # "imagePath" 수정
    new_imagePath = update_json_contents(json_path)
    parent_path = os.path.dirname(new_imagePath)
    parent_path = os.path.dirname(parent_path)
    print("parent_path: "+parent_path)

    new_imagePath = os.path.relpath(new_imagePath, parent_path)
    new_imagePath = '..\\' + new_imagePath
    print("new_imagePath: "+new_imagePath)

    # 수정된 JSON 데이터를 다시 파일에 쓰기 (덮어쓰기)
    json_data["imagePath"] = new_imagePath
    with open(json_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"Updated {json_path}")