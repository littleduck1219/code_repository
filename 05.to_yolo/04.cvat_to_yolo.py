import os
import glob
from xml.etree.ElementTree import parse

import cv2

xml_dir = "./data/"


class Voc_to_yolo_convter():
    def __init__(self, xml_path):
        self.xml_path_list = glob.glob(os.path.join(xml_path, "*.xml"))
        # print(self.xml_path_list)

    # 이미지 박스 확인
    def cavt_xyxy_show(self, xtl, ytl, xbr, ybr, label, image_name):
        image_path = os.path.join("./data/images", image_name)
        image = cv2.imread(image_path)
        img_rect = cv2.rectangle(image, (int(xtl), int(ytl)), (int(xbr), int(ybr)), (0, 255, 0), 2)
        cv2.imshow("test", img_rect)
        cv2.waitKey()

        return img_rect


    def get_voc_to_yolo(self):
        for xml_path in self.xml_path_list:
            tree = parse(xml_path)
            root = tree.getroot()

            # image_meta
            yolo_format = []
            meta = root.findall("image")
            for image in meta:
                image_name = image.attrib["name"]  # 파일이름
                image_width = int(image.attrib["width"])  # width
                image_height = int(image.attrib["height"])  # height
                # print(image_name, image_width, image_height)

                # object_meta
                object_metas = image.findall("box")
                for bbox in object_metas:
                    label = bbox.attrib["label"]
                    xtl = float(bbox.attrib["xtl"])
                    ytl = float(bbox.attrib["ytl"])
                    xbr = float(bbox.attrib["xbr"])
                    ybr = float(bbox.attrib["ybr"])
                    # print(xtl, ytl, xbr, ybr, label)

                    img_rect = self.cavt_xyxy_show(xtl, ytl, xbr, ybr, label, image_name)

                    # CVAT to yolo
                    yolo_x = round(((xtl + xbr)/2)/image_width, 6)
                    yolo_y = round(((ytl + ybr)/2)/image_height, 6)
                    yolo_w = round((xbr - xtl)/image_width, 6)
                    yolo_h = round((ybr - ytl)/image_height, 6)
                    print(label, yolo_x, yolo_y, yolo_w, yolo_h)
                    yolo_format.append((label, yolo_x, yolo_y, yolo_w, yolo_h))

                    # Save yolo format to file
                    yolo_file = os.path.join("./data/yolo", f"{image_name.split('.')[0]}.txt")
                    with open(yolo_file, "w") as f:
                        for item in yolo_format:
                            f.write(" ".join([str(x) for x in item]) + "\n")


test = Voc_to_yolo_convter(xml_dir)
test.get_voc_to_yolo()