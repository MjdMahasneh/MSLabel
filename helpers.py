import os
import sys
import cv2
import numpy as np
import glob as glist
import getImageList as glist


def check_dir_setup():
    if not os.path.exists('./cache'):
        os.makedirs('./cache')

    if not os.path.exists('./annotation_files'):
        os.makedirs('./annotation_files')

    if not os.path.exists('./cache'):
        os.makedirs('./cache')

    if not os.path.exists('./images/band_1'):
        os.makedirs('./images/band_1')

    if not os.path.exists('./images/band_2'):
        os.makedirs('./images/band_2')

    if not os.path.exists('./cache/temp.txt'):
        file = open('./cache/temp.txt', 'w')
        file.write('')
        file.close()

    if not os.path.exists('./cache/no_image_available.jpg'):
        img = np.zeros((800, 800, 3), np.uint8)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'No Image', (10, 500), font, 5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imwrite('./cache/no_image_available.jpg', img)
    else:
        pass

    if len(glist.get_imlist('images/band_1')) == 0 or len(glist.get_imlist('images/band_2')) == 0:
        print('images/band_1 or images/band_2 is empty')
        sys.exit()

    return()