import glob
import os
import shutil

dataset_path = "./struct_dataset"
image_data = glob.glob(os.path.join(dataset_path, "*", "*", "*.jpg"))
label_data = glob.glob(os.path.join(dataset_path, "*", "*", "*.txt"))

cloth_path = "../remove_folder"
cloth_image_data = glob.glob(os.path.join(cloth_path, "*.jpg"))
cloth_label_data = glob.glob(os.path.join(cloth_path, "*", "*", "*.txt"))

remove_path = "./struct_dataset"
all_data = glob.glob(os.path.join(remove_path, "*", "*", "*.jpg"))


def remove_data():
    for path2 in cloth_image_data:
        file_name = path2.split("\\")[1]

        move_path = "../remove_folder2"
        os.makedirs(move_path, exist_ok=True)

        if not os.path.isfile(path2):
            print('File does not exist:', path2)
            pass
        else:
            shutil.move(f"./struct_dataset/test/images/{file_name[:-4]}.jpg", move_path)
            shutil.move(f"./struct_dataset/test/labels/{file_name[:-4]}.txt", move_path)
            shutil.move(f"./struct_dataset/train/images/{file_name[:-4]}.jpg", move_path)
            shutil.move(f"./struct_dataset/train/labels/{file_name[:-4]}.txt", move_path)
            shutil.move(f"./struct_dataset/valid/images/{file_name[:-4]}.jpg", move_path)
            shutil.move(f"./struct_dataset/valid/labels/{file_name[:-4]}.txt", move_path)


remove_data()
