import glob
import os


def main():
    data_root = "../data1/val/"
    count = 0

    for use in ["images", "labels"]:
        label_root = os.path.join(data_root, use)
        image_root = os.path.join(data_root, use)
        # print(label_data)

        for image_path in get_image_paths(label_root):
            dirs = image_path.split("\\")
            paths = dirs[0].split("/")

            data_path = os.path.join(data_root, "labels")
            label_name = os.path.basename(image_path)[:-4] + ".txt"

            label_path = os.path.join(data_path, label_name)

            if not os.path.isfile(label_path):
                print('File does not exist:', label_path)
                count += 1
            else:
                pass

    print(count)


def get_image_paths(root_path):
    # root_path 경로 하위에 있는 모든 파일 경로 탐색
    paths = []
    for (path, dir, files) in os.walk(root_path):
        for file in files:
            if file.split('.')[-1] != 'jpg':
                continue

            image_path = os.path.join(path, file)
            paths.append(image_path)
    return paths


# if __name__ == "__main__":
#     main()
