import os
import glob
from sklearn.model_selection import train_test_split
import cv2

data_image_path = "../all_data/data/images"
image_data = glob.glob(os.path.join(data_image_path, "*.jpg"))

train_data, val_list = train_test_split(image_data, train_size=0.8, random_state=7)
val_data, test_data = train_test_split(val_list, test_size=0.1, random_state=7)

def data_save(data, mode):
    for path in data:
        folder_name = path.split("/")[3]
        print(folder_name)

        folder_path = f"../dataset/{mode}"
        os.makedirs(folder_path, exist_ok=True)

        image_name = path.split("/")[4]

        img = cv2.imread(path)
        cv2.imwrite(os.path.join(folder_path, image_name), img)


data_save(train_data, mode="train")