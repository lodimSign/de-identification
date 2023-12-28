import os
import cv2
import concurrent.futures
import numpy as np

def find_image_files(directory, img_files=[]):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path) and (item.endswith('.png') or item.endswith('.jpg')):
            img_files.append(item_path)
        elif os.path.isdir(item_path):
            img_files = find_image_files(item_path, img_files)
    return img_files

# Directory containing image files
directory_path = 'C:\\workspace\\datasets\\Kakaomobility_people6\\round(20220906111759_autocardata_100)_time(1662435830_1662435858)\\sensor\\camera(00)'

# Find all image files in the directory
img_files = find_image_files(directory_path)

# Create a single instance of the HOG detector for person detection
body_cascade = cv2.HOGDescriptor()
body_cascade.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Function to process an image
def process_image(image_path):
    # Load YOLOv3 model
    net = cv2.dnn.readNet('C:\workspace\de-identification\people_tracker\models\yolov3.weights', 'C:\workspace\de-identification\people_tracker\models\yolov3.cfg')

    # Load COCO class names
    with open('C:\workspace\de-identification\people_tracker\models\coco.names', 'r') as f:
        classes = f.read().strip().split('\n')

    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    # Detect objects in the image using YOLOv3
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layer_names = net.getUnconnectedOutLayersNames()
    detections = net.forward(layer_names)

    # Create a list to store detected people
    detected_people = []

    for detection in detections:
        for obj in detection:
            scores = obj[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and classes[class_id] == 'person':
                center_x, center_y = int(obj[0] * width), int(obj[1] * height)
                w, h = int(obj[2] * width), int(obj[3] * height)
                x, y = int(center_x - w / 2), int(center_y - h / 2)

                detected_people.append((x, y, x + w, y + h))

    # Filter overlapping detections to keep unique people
    unique_people = []
    for person in detected_people:
        (x, y, x2, y2) = person
        overlaps = False
        for (x1, y1, x2_1, y2_1) in unique_people:
            if (x < x2_1 and x2 > x1 and y < y2_1 and y2 > y1):
                overlaps = True
                break
        if not overlaps:
            unique_people.append((x, y, x2, y2))

    # Draw rectangles around detected unique people and display their IDs
    for (x, y, x2, y2) in unique_people:
        cv2.rectangle(image, (x, y), (x2, y2), (0, 0, 255), 3)

    # Save the modified image
    original_image_file_contained_folder_path = os.path.dirname(image_path)
    original_image_file_name = os.path.basename(image_path)
    print("---original_image_file_name: " + original_image_file_name)

    save_path = "result\\" + original_image_file_contained_folder_path.split('C:\\workspace\\datasets\\')[-1] + "\\people_IDs\\"

    # Create the output folder if it doesn't exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    save_path += original_image_file_name
    print("---output path: " + save_path)
    cv2.imwrite(save_path, image)

# Directory containing image files
directory_path = 'C:\\workspace\\datasets\\Kakaomobility_people6\\round(20220906111759_autocardata_100)_time(1662435830_1662435858)\\sensor\\camera(00)'

# Find all image files in the directory
img_files = find_image_files(directory_path)

with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
    executor.map(process_image, img_files)

print("Images with detected people and IDs saved.")
