import cv2
import os, glob
import json
import shutil

os.makedirs("./results", exist_ok=True)


im_paths = glob.glob("C:\workspace\datasets\delete_face_without_body\images\*.png")
imgs = {}
for p in im_paths:
    name = p.split("/")[-1].split(".")[0]
    imgs[name] = p

print("Im_path loading done!")
    
face_lab_paths = glob.glob(r"C:\workspace\datasets\delete_face_without_body\faces\*.json")
face_lab = {}

for p in face_lab_paths:
    with open(p, "r") as file:
        data = json.load(file)
        name = p.split("/")[-1].split(".")[0]
        if data['shapes'] != []:
            faces=[]
            for d in data['shapes']:
                faces.append(d['points'])
            face_lab[name] = faces
            
print("Face lab loading done!")
print(f"{len(face_lab.keys())} of images have face bboxes")
            
LP_lab_paths = glob.glob(r"C:\workspace\datasets\delete_face_without_body\plates\*.json")
lp_lab = {}

for p in LP_lab_paths:
    with open(p, "r") as file:
        data = json.load(file)
        name = p.split("/")[-1].split(".")[0]
        if data['shapes'] != []:
            lps=[]
            for d in data['shapes']:
                lps.append(d['points'])
            lp_lab[name] = lps

print("Plates lab loading done!")
print(f"{len(lp_lab.keys())} of images have Plates bboxes")

for k in imgs.keys():
    if k in face_lab.keys() or k in lp_lab.keys():
        im = cv2.imread(imgs[k])
        if k in face_lab.keys() and face_lab[k] !=[]:
            for lab in face_lab[k]:
                im = cv2.rectangle(im, (int(lab[0][0]), int(lab[0][1])),(int(lab[1][0]), int(lab[1][1])), (255, 0, 0), 1)
        if k in lp_lab.keys() and lp_lab[k] !=[]:
            for lab in lp_lab[k]:
                try:
                    im = cv2.rectangle(im, (int(lab[0][0]), int(lab[0][1])),(int(lab[1][0]), int(lab[1][1])), (0, 255, 0), 1)
                except:
                    import ipdb; ipdb.set_trace()
                    
                
        cv2.imwrite(f"C:\workspace\datasets\delete_face_without_body\\results\{k}.png", im)
      
print("done!")