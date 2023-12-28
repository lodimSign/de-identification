import glob
import os
import json
import shutil
import sys
from datetime import datetime


def backup_jsonfiles(folder_path):
    for folder_path in glob.glob(folder_path):
        if 'images' in folder_path:
            print('\n---folder_path: '+folder_path)
        else:
            # images 폴더가 아닌 폴더(ex: faces, plates, personIDS, backup, ...) 백업하기
            print('folder_path: ' + folder_path)

            # Create a backup folder with today's date as a subfolder
            today_date = datetime.today().strftime('%y%m%d')
            backup_folder_name = folder_path.split('\\')[-1]
            print('### backup_folder_name: ', backup_folder_name)
            backup_folder = os.path.dirname(folder_path)
            print('### backup_folder: ', backup_folder)
            sys.exit()

            backup_folder = os.path.join(backup_folder, 'backup', today_date, backup_folder_name)
            print('backup_folder: ' + backup_folder)
            os.makedirs(backup_folder, exist_ok=True)

            # folder_path의 파일들을 backup_folder에 복사
            for file_path in glob.glob(os.path.join(folder_path, '*.json')):
                file_name = os.path.basename(file_path)
                print("###"+file_name)
                destination_path = os.path.join(backup_folder, file_name)

                try:
                    shutil.copy(file_path, destination_path)
                    print(f'Copied: {file_path} to {destination_path}')
                except shutil.SameFileError:
                    print(f'Skipping: {file_path} (Same file as in backup)')


folder_path = r"Z:\de-identification\Kakaomobility\round*\*\*\*"

backup_jsonfiles(folder_path)
