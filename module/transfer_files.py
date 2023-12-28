import os
import shutil

def find_target_folders(source_folder, target_folder_name):
    target_folders = []

    # 원본 폴더 내의 모든 폴더와 파일 목록을 얻습니다.
    for root, dirs, files in os.walk(source_folder):
        for dir in dirs:
            # 폴더 이름이 대상 문자열을 포함하면 해당 폴더를 찾습니다.
            if target_folder_name.lower() in dir.lower():
                target_folders.append(os.path.join(root, dir))

    return target_folders

def create_and_move_folders(target_folders, new_folder_name):
    for folder in target_folders:
        # 새로운 폴더 경로 생성
        new_folder_path = os.path.join(folder, new_folder_name)

        # 새로운 폴더 생성
        os.makedirs(new_folder_path, exist_ok=True)

        # 원본 폴더 내의 파일을 새로운 폴더로 이동
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                shutil.move(file_path, os.path.join(new_folder_path, file))
                print("file path: "+file_path)

# 예제 사용법
source_folder = r'C:\workspace\datasets\backup\Kakaomobility'
target_folder_name = 'camera'
new_folder_name = 'images'

target_folders = find_target_folders(source_folder, target_folder_name)

# 새로운 폴더를 만들고 파일을 이동
create_and_move_folders(target_folders, new_folder_name)