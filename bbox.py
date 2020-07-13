#!/usr/bin/env python

import cv2
import os
from os import path
from glob import glob

def add_bbox(raw_img_file, label_file, bbox_img_file):
    if path.exists(raw_img_file):
        img = cv2.imread(raw_img_file)
    else:
        print(f"Couldn't open the raw image file: {raw_img_file}")
        return

    if path.exists(label_file):
        with open(label_file) as fl:
            for line in fl:
                label = line.split()
                if label[0] == 'loop':
                    cv2.rectangle(img, (int(label[4]), int(label[5])), (int(label[6]), int(label[7])), (0, 0, 255), 2)
    else:
        print(f"Couldn't open the label file: {label_file}")
        return
    
    cv2.imwrite(bbox_img_file, img)

if __name__ == "__main__":
    if not path.exists("bboxes"):
        os.makedirs("bboxes")

    for img_file in glob("images/*.jpg"):
        print(img_file)
        basename = path.basename(img_file).split('.')[0]
        label_file = 'labels/' + basename + '.txt'
        bbox_file = 'bboxes/' + basename + '.jpg'
        add_bbox(img_file, label_file, bbox_file)