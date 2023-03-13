
import os
import glob
import zipfile
from tqdm import tqdm

# 현재 작업 디렉토리
base_dir = "../08.resize_composit_image"

# 압축 파일 이름
zip_name = "images.zip"

# 한 파일당 포함될 이미지 개수
n_images_per_file = 250

# 현재 작업 디렉토리에 있는 파일 리스트
file_list = glob.glob(os.path.join(base_dir, "*.png"))

# 이미지 파일 리스트
image_list = [f for f in file_list if f.endswith(".png")]

# 이미지 파일 개수
n_images = len(image_list)

# 압축 파일 개수
n_zip_files = n_images // n_images_per_file + (n_images % n_images_per_file > 0)

for i in tqdm(range(n_zip_files)):
    # 압축 파일 이름
    zip_file_name = f"{zip_name.split('.')[0]}_{i+1}.zip"

    # 압축 파일 생성
    with zipfile.ZipFile(zip_file_name, "w") as zip_file:
        # 파일에 추가할 이미지 범위 계산
        start_idx = i * n_images_per_file
        end_idx = min(start_idx + n_images_per_file, n_images)

        # 이미지 파일 압축
        for j in range(start_idx, end_idx):
            zip_file.write(image_list[j])

print("압축 완료")
