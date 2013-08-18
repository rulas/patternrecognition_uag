'''
Created on Jun 15, 2013

@author: lrvillan
'''

from PyQt4.QtGui import QImage, QImageWriter
import sys
import os
from PIL import Image
import numpy as np


def rgb_to_monochrome(image):
    # receives a QImage in rgb and convert to 1 bit monochrome
    return image.convertToFormat(QImage.Format_Mono)


def convert_gif_to_monochrome(fpath):
    name, _ = os.path.splitext(fpath)
    outpath = "%s_new.png" % name
    print "output = %s" % (outpath)
    img = QImage(fpath).convertToFormat(QImage.Format_Mono)
    r = img.save(outpath, "png")
    if r:
        print


def convert_image_to_array(image):
    """
        converts a PIL image to an numpy matrix with same dimension as image

        @param image: PIL image to be converted
        @return: numpy array with W x H dimension
    """
    w, h = image.size

    # we support black and white images only.
    if "P" in image.getbands():
        #a = image.split()
        #a = image.tostring()
        img_array = np.fromstring(image.tostring(), dtype=np.uint8)
        return img_array.reshape((w, h))
    else:
        raise TypeError("Wrong Image type. Only B&W images are supported")


