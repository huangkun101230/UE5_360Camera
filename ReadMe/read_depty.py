import OpenEXR
import cv2
import numpy as np
from PIL import Image
import Imath
import matplotlib.pyplot as plt
import os

def read_exr(s, width, height):
    mat = np.fromstring(s, dtype=np.float32)
    mat = mat.reshape(height, width)
    return mat

def exr_to_png(exr_path):
    # exr_path = 'Frame_00017_SceneDepth.exr'
    exr_img = OpenEXR.InputFile(exr_path)
    # print('exr_img shape: ', exr_img.shape)
    depth_path = exr_path.replace('.exr', '.png')
    dw = exr_img.header()['dataWindow']
    (width, height) = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)
    # print((width, height))

    dmap, _, _ = [read_exr(s, width, height) for s in exr_img.channels('BGR', Imath.PixelType(Imath.PixelType.FLOAT))]
    # print(dmap.shape)
    plt.imshow(dmap)
    plt.imsave(depth_path, dmap)
    # plt.show()

    # dmap = Image.fromarray((dmap != 1).astype(np.uint8))
    # dmap.save(depth_path)
    # exr_img.close()

if __name__ == '__main__':
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if os.path.splitext(f)[1] == ".exr":
            exr_to_png(f)
            print(f, 'transformed to PNG')