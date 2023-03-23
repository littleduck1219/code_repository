# 날짜 순서 정보를 담기 위해 데이터가 섞이지 않도록, train val test 3가지로 data split 하는 코드
# - 라벨 개수를 균등하게 맞추기 위해 가장 적은 라벨 기준으로 개수 counting

import os
import glob
import shutil

folder_list =['images_filtering_10T', 'images_filtering_30T', 'images_filtering_H']

for folder in folder_list:
    # 0. 폴더 별 경로 설정
    root_path = f'./{folder}/'
    labels = os.listdir(root_path)

    label_data_list = []

    # 1. 라벨마다 개수 세고 가장 적은 라벨을 기준으로 두기
    min_label_count = None
    min_label = None
    for label in labels :
        data = glob.glob(os.path.join(root_path, label, '*.png'))
        if min_label_count is None :
            min_label_count = len(data)
            min_label = label

        if min_label_count > len(data) :
            min_label_count = len(data)
            min_label = label
    print('가장 개수가 적은 라벨 :', min_label, min_label_count)

    # 2. min_label_count 만큼만 데이터스플릿 8:1:1 (train, val, test)
    train_cnt_idx = int(min_label_count * 0.8)
    val_cnt_idx = train_cnt_idx + int(min_label_count * 0.1)
    test_cnt_idx = min_label_count
    save_root_path = f'./sorted_dataset_{folder}/'
    for label in labels :
        cnt = 0
        paths = glob.glob(os.path.join(root_path, label, '*.png'))
        for path in paths :
            if cnt >= 0 and cnt < train_cnt_idx :
                save_path = save_root_path + 'train/' + label +'/'
                os.makedirs(save_path, exist_ok=True)
                shutil.copy(path, save_path + path.split('\\')[-1])
            elif cnt >= train_cnt_idx and cnt < val_cnt_idx :
                save_path = save_root_path + 'val/' + label +'/'
                os.makedirs(save_path, exist_ok=True)
                shutil.copy(path, save_path + path.split('\\')[-1])
            elif cnt >= val_cnt_idx and cnt < test_cnt_idx :
                save_path = save_root_path + 'test/' + label +'/'
                os.makedirs(save_path, exist_ok=True)
                shutil.copy(path, save_path + path.split('\\')[-1])
            else :
                break
            cnt += 1