import cv2
import os
import glob

root_path = '../03.split_dataset/test/images'
all_data_path = glob.glob(os.path.join(root_path, '*.jpg'))
for path in all_data_path:
    all_data_name = [os.path.basename(file_path) for file_path in all_data_path]
print(all_data_name)

for image_path in all_data_path:
    label_path = image_path.replace('/images/', '/labels/')[:-4] + '.txt'
    with open(label_path, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')

    for line in lines:
        if line[:2] == '10':
            line = line.split(' ')
            image = cv2.imread(image_path)
            image_h, image_w, _ = image.shape
            x_c, y_c, w, h = image_w * float(line[1]), image_h * float(line[2]), image_w * float(line[3]), image_h * float(line[4])
            x1, y1, x2, y2 = int((x_c) - (w // 2)), int((y_c) - (h // 2)), int((x_c) + (w // 2)), int((y_c) + (h // 2))
            print(image_path)
            print(x1, y1, x2, y2)
            image = image[y1:y2, x1:x2]
            cv2.imshow('test', image)
            cv2.waitKey(0)
            cv2.imwrite("../04.crop_images/{}")

