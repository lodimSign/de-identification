import os
from glob import glob

# 폴더 경로 패턴
folder_path = r"Z:\de-identification\Kakaomobility\round*\*\*\*"

# faces, plates, personIDs 폴더에서 json 파일 갯수 세는 함수
def count_json_files(folder):
    json_files = glob(os.path.join(folder, '*.json'))
    return len(json_files)

# 모든 폴더에서 json 파일 갯수를 세기 위한 변수 초기화
total_faces = 0
total_plates = 0
total_personIDs = 0

# 결과를 저장할 파일
output_file_path = r"Z:\backup\de-identification\Kakaomobility\count_file_all_and_sum_231218.txt"


# 폴더 경로에 대한 루프
with open(output_file_path, 'w') as output_file:
    for subfolder in glob(folder_path):
        # backup 폴더인 경우 건너뛰기
        if "backup" in subfolder:
            continue

        json_count = count_json_files(subfolder)

        if "faces" in subfolder:
            total_faces += json_count
        elif "plates" in subfolder:
            total_plates += json_count
        elif "personIDs" in subfolder:
            total_personIDs += json_count

        # 결과를 파일과 화면에 출력
        output_file.write(f"folder path: {subfolder}\n")
        output_file.write(f"json file num: {json_count}\n")
        output_file.write("==========================================================================================\n")

        # 결과를 화면에 출력
        print(f"folder path: {subfolder}")
        print(f"json file num: {json_count}")
        print("==========================================================================================")

    # 결과를 파일과 화면에 출력
    output_file.write(f"Total faces: {total_faces}\n")
    output_file.write(f"Total plates: {total_plates}\n")
    output_file.write(f"Total personIDs: {total_personIDs}\n")
    output_file.write(f"Grand Total: {total_faces + total_plates + total_personIDs}\n")

    # 결과를 화면에 출력
    print(f"Total faces: {total_faces}")
    print(f"Total plates: {total_plates}")
    print(f"Total personIDs: {total_personIDs}")
    print(f"Grand Total: {total_faces + total_plates + total_personIDs}")

print(f"Results saved to {output_file_path}")