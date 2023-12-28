import copy
import glob
import json
import os
import sys
import time


def face_inside_check(face, person):
    face_x1, face_x2 = (face[0][0], face[1][0]) if face[0][0] < face[1][0] else (face[1][0], face[0][0])
    face_y1, face_y2 = (face[0][1], face[1][1]) if face[0][1] < face[1][1] else (face[1][1], face[0][1])

    person_x1, person_x2 = (person[0][0], person[1][0]) if person[0][0] < person[1][0] else (person[1][0], person[0][0])
    person_y1, person_y2 = (person[0][1], person[1][1]) if person[0][1] < person[1][1] else (person[1][1], person[0][1])

    print("------face:")
    print(face_x1, face_y1)
    print(face_x2, face_y2)

    print("------person:")
    print(person_x1, person_y1)
    print(person_x2, person_y2)

    return person_x1 <= face_x1 <= person_x2 and person_x1 <= face_x2 <= person_x2 and \
        person_y1 <= face_y1 <= person_y2 and person_y1 <= face_y2 <= person_y2


folder_path = r'C:\workspace\datasets\delete_person_without_face\*'
# folder_path = r"Z:\de-identification\Kakaomobility\round*\*\*\*"

for check_folder_path in glob.glob(folder_path):
    if 'personIDs' in check_folder_path:
        personIDs_folder_path = check_folder_path + '\*'
        print(personIDs_folder_path)

        # personIDs json 파일들 가져오기
        for personIDs_json_file_path in glob.glob(personIDs_folder_path):
            print("-------------------------------------------------------------------------------------------------------")
            print("personIDs_json_file_path: ", personIDs_json_file_path)

            try:
                # personIDs json 파일 별 personIDs points 가져오기
                with open(personIDs_json_file_path, 'r') as personIDs_json_file:
                    data_person = json.load(personIDs_json_file)
                    result_person = copy.deepcopy(data_person)

                    # Create a list to store shapes to be removed
                    shapes_to_remove = []

                    for shape_person in data_person['shapes']:
                        print("---person points: ", shape_person['points'])

                        # personIDs_json_file과 같은 이름의 faces json 파일 가져오기
                        faces_folder_path = os.path.dirname(personIDs_json_file_path)
                        faces_folder_path = os.path.dirname(faces_folder_path)
                        faces_folder_path = os.path.join(faces_folder_path, 'faces')
                        faces_json_file_name = os.path.basename(personIDs_json_file_path)
                        faces_json_file_path = os.path.join(faces_folder_path, faces_json_file_name)

                        if not os.path.exists(faces_json_file_path):
                            print("NO faces_json_file!")
                            personIDs_json_file.close()

                            if os.path.isfile(personIDs_json_file_path):
                                data_person['shapes'].clear()
                                print("---person removed")
                                with open(personIDs_json_file_path, 'w') as personIDs_json_file:
                                    json.dump(data_person, personIDs_json_file, indent=2)

                            continue

                        with open(faces_json_file_path, 'r') as faces_json_file:
                            data_face = json.load(faces_json_file)

                        person_remove = False
                        for shape_face in data_face['shapes']:
                            is_face_inside = face_inside_check(shape_face['points'], shape_person['points'])
                            print("////////////////////////////////is_face_inside:", is_face_inside, '////////////////////////////////')

                            if is_face_inside:
                                person_remove = False
                                break
                            else:
                                person_remove = True

                        if person_remove:
                            shapes_to_remove.append(shape_person)

                # Remove the shapes from result_person
                for shape_to_remove in shapes_to_remove:
                    result_person['shapes'].remove(shape_to_remove)

                for data in data_person['shapes']:
                    print(data)
                print("======================>")
                for result in result_person['shapes']:
                    print(result)
                print("\n")

                # with open(personIDs_json_file_path, 'w') as personIDs_json_file:
                #     json.dump(result_person, personIDs_json_file, indent=2)
                #     print(f"\n\n{personIDs_json_file_path} changed!")

            except:
                print(f"Skipping : {personIDs_json_file_path} (no exist)")
