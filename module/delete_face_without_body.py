import glob
import json
import os
import sys


def face_inside_check(face, person):
    face_x1, face_x2 = (face[0][0], face[1][0]) if face[0][0] < face[1][0] else (face[1][0], face[0][0])
    face_y1, face_y2 = (face[0][1], face[1][1]) if face[0][1] < face[1][1] else (face[1][1], face[0][1])

    person_x1, person_x2 = (person[0][0], person[1][0]) if person[0][0] < person[1][0] else (person[1][0], person[0][0])
    person_y1, person_y2 = (person[0][1], person[1][1]) if person[0][1] < person[1][1] else (person[1][1], person[0][1])

    print("---face:")
    print(face_x1, face_y1)
    print(face_x2, face_y2)

    print("---person:")
    print(person_x1, person_y1)
    print(person_x2, person_y2)

    return person_x1 <= face_x1 <= person_x2 and person_x1 <= face_x2 <= person_x2 and \
        person_y1 <= face_y1 <= person_y2 and person_y1 <= face_y2 <= person_y2


faces_folder_path = r'Z:\de-identification\Kakaomobility\round(20220906111759_autocardata_100)_time(1662436882_1662436931)\sensor\camera(00)\faces\*'
# faces_folder_path = r'C:\workspace\datasets\delete_face_without_body\faces\*'

# faces json 파일들 가져오기
for faces_json_file_path in glob.glob(faces_folder_path):
    print("-------------------------------------------------------------------------------------------------------")
    print("faces_json_file_path: ", faces_json_file_path)

    # faces json 파일 별 faces points 가져오기
    with open(faces_json_file_path, 'r') as faces_json_file:
        data_face = json.load(faces_json_file)
        for shape_face in data_face['shapes']:
            print("face points: ", shape_face['points'], '\n')

            # faces json 파일과 같은 이름의 personIDs json 파일 가져오기
            personIDs_folder_path = os.path.dirname(faces_json_file_path)
            personIDs_folder_path = os.path.dirname(personIDs_folder_path)
            personIDs_folder_path = os.path.join(personIDs_folder_path, 'personIDs')
            faces_json_file_name = os.path.basename(faces_json_file_path)
            personID_json_file_path = os.path.join(personIDs_folder_path, faces_json_file_name)
            print("personID_json_file_path: ", personID_json_file_path)
            with open(personID_json_file_path, 'r') as personID_json_file_path:
                data_person = json.load(personID_json_file_path)

            face_remove = False
            for shape_person in data_person['shapes']:
                print("person points: ", shape_person['points'])

                # personIDs json 파일 내용 중 faces points를 포함하는 personIDs points가 있는지 확인
                is_face_inside = face_inside_check(shape_face['points'], shape_person['points'])

                print("\nis_face_inside: ", is_face_inside, '////////////////////')

                # 있다면 다음 face로 넘어가기
                if is_face_inside == True:
                    face_remove = False
                    break

                if is_face_inside == False:
                    face_remove = True

            # face_remove가 True 인 경우 face 삭제
            if face_remove == True:
                data_face['shapes'].remove(shape_face)

    with open(faces_json_file_path, 'w') as faces_json_file:
        json.dump(data_face, faces_json_file, indent=2)