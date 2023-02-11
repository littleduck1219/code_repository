import os
import glob
import shutil
import splitfolders

image_path = "ddong/test/images"
image_data = glob.glob(os.path.join(image_path, "*.jpg"))
label_path = "../ys_split_clothes_dataset/dataset_clothes"
label_data = glob.glob((os.path.join(label_path, "*", "*", "*.txt")))


image_move_path = "../ys_split_clothes_dataset/dataset_clothes"
image_move_data = glob.glob(os.path.join(image_move_path, "*", "*", "*.jpg"))
label_move_path = "ddong/label"
label_move_data = glob.glob(os.path.join(label_move_path, "*", "*", "*.txt"))



new_label_path = "../cloth labels"
new_label_data = glob.glob(os.path.join(new_label_path, "*.txt"))


def label_remove():
    for text in label_data:
        file_name = text.split("\\")[3]
        # print(file_name)
        with open(text, encoding="utf-8") as f:
            for lines in f:
                lines = lines.strip()
                # print(lines)
                zero = lines.startswith("0")
                one = lines.startswith("1")
                two = lines.startswith("2")
                three = lines.startswith("3")
                four = lines.startswith("4")
                with open(fr"../cloth labels/{file_name}", "a") as t:
                    if lines.startswith("0"):
                        new_line = "1" + lines[1:] + "\n"
                        t.write(new_line)
                    elif lines.startswith("1"):
                        new_line = "1" + lines[1:] + "\n"
                        t.write(new_line)
                    elif lines.startswith("2"):
                        new_line = "1" + lines[1:] + "\n"
                        t.write(new_line)
                    elif lines.startswith("3"):
                        new_line = "1" + lines[1:] + "\n"
                        t.write(new_line)
                    elif lines.startswith("4"):
                        new_line = "1" + lines[1:] + "\n"
                        t.write(new_line)


def check_label_error():
    for text in new_label_data:
        file_name = text.split("\\")[1]
        # print(file_name)
        with open(text, encoding="utf-8") as f:
            for lines in f:
                lines = lines.strip()
                # print(lines)
                zero = lines.startswith("0")
                one = lines.startswith("1")
                two = lines.startswith("2")
                three = lines.startswith("3")
                four = lines.startswith("4")

                if not one:
                    print(lines)


def image_move():
    for image in image_move_data:

        shutil.move(image, "../cloth_labels/images")


# label_remove()
# check_label_error()
# image_move()


splitfolders.ratio(r"D:\all_data2\data", output=r"D:\data2",
                   seed=77, ratio=(0.8, 0.1, 0.1), group_prefix=1)
