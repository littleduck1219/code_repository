import glob
import os
import shutil

main_data_path = "../struct_dataset"

train_image_path = "../struct_dataset/train/images"
train_image = glob.glob(os.path.join(train_image_path, "*.jpg"))
train_label_path = "../struct_dataset/train/labels"
train_label = glob.glob(os.path.join(train_label_path, "*.txt"))
valid_image_path = "../struct_dataset/valid/images"
valid_image = glob.glob(os.path.join(valid_image_path, "*.jpg"))
valid_label_path = "../struct_dataset/valid/labels"
valid_label = glob.glob(os.path.join(valid_label_path, "*.txt"))
test_image_path = "../struct_dataset/test/images"
test_image = glob.glob(os.path.join(test_image_path, "*.jpg"))
test_label_path = "../struct_dataset/test/labels"
test_label = glob.glob(os.path.join(test_label_path, "*.txt"))

remove_path_image = "../remove_folder/images"
remove_image_data = glob.glob(os.path.join(remove_path_image, "*.jpg"))
remove_path_label = "../remove_folder/labels"
remove_label_data = glob.glob(os.path.join(remove_path_label, "*.txt"))

belt_path_image = "../remove_folder/images"
belt_image_data = glob.glob(os.path.join(remove_path_image, "*.jpg"))
belt_path_label = "../remove_folder/labels"
belt_label_data = glob.glob(os.path.join(remove_path_label, "*.txt"))


for path in remove_image_data:
    file_name = path.split("\\")[1]
    print(file_name)
    # dirs = path.split("/")
    shutil.move(f"../all_data/images/{file_name}", f"../delete/{file_name}")

