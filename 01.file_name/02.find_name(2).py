import glob
import os


def main():
    count = 0
    data_root = "../dataset/test"

    image_root = os.path.join(data_root, "images")
    label_root = os.path.join(data_root, "labels")

    image_data = glob.glob(os.path.join(image_root, "*.jpg"))

    for image_path in image_data:
        dirs = image_path.split("\\")
        paths = dirs[0].split("/")

        label_name = os.path.basename(image_path)[:-4] + ".txt"

        label_path = os.path.join(label_root, label_name)
        # print(label_path)

        if not os.path.isfile(label_path):
            print('File does not exist:', label_path)
            count += 1
        else:
            pass

    print(count)


if __name__ == "__main__":
    main()
