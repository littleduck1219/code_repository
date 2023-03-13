import os
import glob
import cv2

path = ".\obj_traindata\"
images = glob.glob(os.path.join(path, "*.jpg"))

for image in images:
    name = image.split("\")[-1]
    name = name[:-4]
    img = cv2.imread(imag e)
    lh, lw,  = img.shape

    with open('.\obj_train_data\' + name + ".txt", 'r') as f:
        strings = f.readlines()
        for i in strings:
            box = i.lstrip()
            class_id, x_center, y_center, w, h = box.strip().split()
            # if class_id == '0':
            #     x_center, y_center, w, h = float(x_center), float(y_center), float(w), float(h)
            #     x_center = round(x_center * lw)
            #     y_center = round(y_center * lh)
            #     w = round(w * lw)
            #     h = round(h * lh)
            #     x = round(x_center - w / 2)
            #     y = round(ycenter  - h / 2)
            #
            #     boxedImage = img[y:y + h, x:x + w]
            #     cv2.imwrite(f"./belt/{name}{x_center}.jpg", boxedImage)
                # cv2.imshow("sample", boxedImage)
                # cv2.waitKey(0)
            if class_id == '1':
                x_center, y_center, w, h = float(x_center), float(y_center), float(w), float(h)
                x_center = round(x_center * lw)
                y_center = round(y_center * lh)
                w = round(w * lw)
                h = round(h * lh)
                x = round(x_center - w / 2)
                y = round(ycenter - h / 2)

                boxedImage = img[y:y + h, x:x + w]
                cv2.imwrite(f"./nobelt/{name}{x_center}.jpg", boxedImage)