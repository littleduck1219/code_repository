import os
import random
from PIL import Image
from tqdm import tqdm

# 바탕 이미지 크기
background_size = (700, 300)

# 합성될 이미지 크기
image_size = (300, 100)

# 이미지 간격
padding = 20

# 이미지 폴더 경로
image_folder = "../05.resize_crop_images"

# 합성된 이미지 저장 폴더 경로
result_folder = "../08.05.image"

# 이미지 파일 경로 리스트
image_path_list = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith(".jpg")]

# 이미지 합성
for i in tqdm(range(5000)):
    # 바탕 이미지 생성
    background = Image.new(mode="RGB", size=background_size, color=(255, 255, 255))

    # 이미지 개수가 4개 미만인 경우, 중복되지 않도록 이미지 제거
    while len(image_path_list) < 4:
        image_path_list.append(random.choice(image_path_list))

    # 랜덤으로 이미지 4개 선택
    selected_images = random.sample(image_path_list, 4)

    # 선택된 이미지 합성
    for j, image_path in enumerate(selected_images):
        # 이미지 불러오기
        image = Image.open(image_path)

        # 이미지 크기가 같아야 합성이 가능하므로, 모든 이미지를 같은 크기로 조정합니다.
        image = image.resize(image_size)

        # 이미지를 합성할 위치 계산
        row = j // 2
        col = j % 2
        position = ((col * image_size[0] + (col + 1) * padding), (row * image_size[1] + (row + 1) * padding))

        # 이미지 합성
        background.paste(image, position)

    # 합성된 이미지 저장
    result_path = os.path.join(result_folder, f"{i}.png")
    background.save(result_path)
