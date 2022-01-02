import numpy as np 
import imageio
import scipy.ndimage
import cv2

#Name of the picture file that we want to make it a scketch {it has to be on this folder, in order to make the process correctly}
img = "NAME OF THE FILE"

def grayscale(rgb):
    return np.dot(rgb[..., :3],[0.299,0.587,0.114])


def dodge(front,back):
    result = front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

j = imageio.imread(img)
g = grayscale(j)
i = 255-g 

b = scipy.ndimage.filters.gaussian_filter(i, sigma=10)
r = dodge(b,g)

cv2.imwrite('output.png', r)