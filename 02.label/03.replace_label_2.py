import os
import glob
import shutil

label_path = "./obj_train_data"
label_data = glob.glob(os.path.join(label_path, "*.txt"))
label_path_2 = "./new_label"
label_data_2 = glob.glob(os.path.join(label_path_2, "*.txt"))
os.makedirs("./new_label", exist_ok=True)
os.makedirs("./new_label_2", exist_ok=True)

# for label in label_data:
#     file_name = label.split("/")[2]
#     with open(label, encoding="utf-8") as f:
#         # for lines in f:
#         #     lines = lines.strip()
#         #     print(lines)
#         lines = f.readlines()

    # with open(f"new_label/{file_name}", "a") as t:
    #     for line in lines:
    #         if line.strip("\n")[0:2] != "10" and line.strip("\n")[0:2] != "11":
    #             t.write(line)
    #
    #         if line.startswith("11"):
    #             new_lines_1 = "15" + line[2:]
    #             t.write(new_lines_1)
    #
    #         elif line.startswith("10"):
    #             new_lines_2 = "11" + line[2:]
    #             t.write(new_lines_2)

for label in label_data_2:
    file_name = label.split("/")[2]
    with open(label, encoding="utf-8") as f:
        # for lines in f:
        #     lines = lines.strip()
        #     print(lines)
        lines = f.readlines()

    with open(f"new_label_2/{file_name}", "a") as t:
        for line in lines:
            if line.strip("\n")[0:2] != "15":
                t.write(line)

            if line.startswith("15"):
                new_lines_1 = "10" + line[2:]
                t.write(new_lines_1)
