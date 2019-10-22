## Codigo da Amostragem##
import numpy as np
import cv2

img = cv2.imread('buildings05.jpg', 0)

n = 2
img_red = img[::n, ::n]

## Codigo da Quantização##
r = 31
img = np.uint8(img / r) * r

cv2.imshow('buildings05', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
