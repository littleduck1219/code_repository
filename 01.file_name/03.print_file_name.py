import os
import glob

cloth_path = r"D:\folder\obj_train_data"
cloth_data = glob.glob(os.path.join(cloth_path, "*.jpg"))

for path in cloth_data:
    path = path.split("\\")[3]
    path_new = fr"folder/obj_train_data/{path}"
    print(path_new)
