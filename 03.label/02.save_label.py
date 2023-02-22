import glob
import os

label_data_path = r"./struct_labeltrain/obj_train_data"
label_data = glob.glob(os.path.join(label_data_path, "*.txt"))
person_label_path = r"./runs/detect/exp6/labels"
person_label = glob.glob(os.path.join(person_label_path, "*.txt"))
count = 0
for text in label_data:
    print(f"read text file:", text)
    file_name = text.split("\\")[1]

    with open(text) as f:
        f.readlines()
        line = line.strip()
        line_one = line.startswith("1")

        if not line_one:
            fix_line = line
            print(fix_line)
            # fix_line = "1" + fix_line[1:] + "\n"
            # # with open(fr"{label_data_path}/{file_name}", "a") as t:
            # f.write(fix_line)

