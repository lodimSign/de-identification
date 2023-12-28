import glob
import os

# images_path = r'C:\workspace\datasets\camera(00)\images'
# delete_check_paths = r'C:\workspace\datasets\camera(00)\*'

images_path = r'Z:\de-identification\Kakaomobility\round(20230417095611_autocardata_100)_time(1681703130_1681703230)\sensor\camera(03)\images'
# Z:\de-identification\Kakaomobility\round()\sensor\camera(03)
delete_check_paths = r'Z:\de-identification\Kakaomobility\round(20230417095611_autocardata_100)_time(1681703130_1681703230)\sensor\camera(03)\personIDs'

# images 폴더의 파일 목록 가져오기
files_in_images_path = os.listdir(images_path)
print("-----" + str(files_in_images_path))
print(len(files_in_images_path))

# delete_check 필요한 폴더들의 파일 목록 가져오기
for delete_check_path in glob.glob(delete_check_paths):
    if 'faces' in delete_check_path or 'plates' in delete_check_path or 'personIDs' in delete_check_path:
        # delete_check_path 폴더 내의 모든 파일 찾기
        delete_check_files = os.listdir(delete_check_path)
        print("-----" + str(delete_check_files))
        print("" + str(len(delete_check_files)) + '\n')

        num = 1

        # delete_check 필요한 폴더 파일 중, images 폴더에 없는 파일 삭제
        for delete_check_file_name in delete_check_files:
            delete_check_file_name_with_extension = delete_check_file_name.split('.')[0] + '.png'
            delete_check_file_path = os.path.join(delete_check_path, delete_check_file_name)

            # 파일이 images 폴더에 없으면 삭제
            if delete_check_file_name_with_extension not in files_in_images_path:
                print("##################################################################################")
                print(f"NO.{num}: {delete_check_file_name}")
                num += 1

                # 파일 삭제
                os.remove(delete_check_file_path)
                print(f"Deleted: {delete_check_file_path}")
                print("##################################################################################\n\n")

    else:
        continue