import cv2
import numpy as np


img = cv2.imread("buildings05.jpg")
_, width, _ = img.shape


width_cutoff = width / 2
s1 = img[:, width_cutoff]
s2 = img[:, width_cutoff:]

cv2.imsave("face1.jpg", s1)
cv2.imsave("face2.jpg", s2)

i1 = cv2.imread("face1.jpg")
i2 = cv2.imread("face2.jpg")
assert i1.mode == i2.mode
assert i1.size == i2.size

pairs = zip(i1.getdata(), i2.getdata())
if len(i1.getbands()) == 1:

    dif = sum(abs(p1-p2) for p1, p2 in pairs)
else:
    dif = sum(abs(c1-c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

ncomponents = i1.size[0] * i1.size[1] * 3
print("Agora foi():" + str((dif / 255.0 * 100) / ncomponents))
