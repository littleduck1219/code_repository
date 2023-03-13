import os
import glob

import cv2
from PIL import Image
from tqdm import tqdm

image_path = "../07.image"
image = glob.glob(os.path.join(image_path, "*.png"))

for i in tqdm(image):
    folder_name = i.split("/")[2]

    with Image.open(i) as img:
        # 원본 이미지 크기
        width, height = img.size

        # 원하는 이미지 크기
        desired_width, desired_height = 800, 600

        # 비율 계산
        width_ratio = desired_width / width
        height_ratio = desired_height / height

        # 크기 조절
        if width_ratio < height_ratio:
            new_size = (int(width * width_ratio), int(height * width_ratio))
        else:
            new_size = (int(width * height_ratio), int(height * height_ratio))

        # 이미지 리사이즈
        img = img.resize(new_size)

        # 리사이즈된 이미지 저장
        img.save(f"../08.resize_composit_image/{folder_name}")
