import os
import shutil
import requests
import json

def delete_specific_file(parent_folder, target_name):
    for folder, subfolders, files in os.walk(parent_folder):
        for index, current_folder in enumerate(subfolders):
            if current_folder == target_name:
                folder_path = os.path.join(folder, target_name)
                shutil.rmtree(folder_path)
                print(f"Folder '{target_name}' deleted at {folder_path}.")
def rename_folders_recursively(parent_folder, old_name, new_name):
    for folder, subfolders, files in os.walk(parent_folder):
        for index, current_folder in enumerate(subfolders):
            if current_folder == old_name:
                subfolders[index] = new_name
                old_folder_path = os.path.join(folder, old_name)
                new_folder_path = os.path.join(folder, new_name)
                os.rename(old_folder_path, new_folder_path)
                print(f"Folder '{old_name}' => '{new_name}' at {new_folder_path}.")
def noti_slack():
    # Slack Incoming Webhook URL
    webhook_url = "https://hooks.slack.com/services/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"

    # Get the name of the executed Python file
    file_name = os.path.basename(__file__)

    # 보낼 메시지
    message = {
        "text": f"파이썬 파일 '{file_name}'이(가) 실행 완료.",
        "username": "PythonBot",
        "icon_emoji": ":snake:",  # 이모지는 원하는 것으로 변경 가능
    }

    # 메시지를 JSON 형식으로 변환하여 전송
    response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})

    # 응답 확인
    if response.status_code == 200:
        print("메시지 전송 성공")
    else:
        print(f"오류 발생: {response.status_code}")
        print(response.text)


# 삭제하려는 상위 폴더 및 폴더 이름 지정
parent_folder = r"Z:\de-identification\Kakaomobility"
target_name = "personIDs"  # Change this to the name of the folder you want to delete
delete_specific_file(parent_folder, target_name)

# 변경하려는 폴더 이름, 새로운 폴더 이름 지정
old_name = "personIDs_id_sort"
new_name = "personIDs"
rename_folders_recursively(parent_folder, old_name, new_name)

# 파일 실행 완료 알림
noti_slack()



