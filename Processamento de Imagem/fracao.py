import cv2
import numpy as np
 
if __name__ == '__main__' :
 
    
    im = cv2.imread("buildings05.jpg")
    showCrosshair = False 
    fromCenter    = False
   
    myroi = cv2.selectROI("buildings05", im, fromCenter, showCrosshair)
    imCrop = im[int(myroi[1]):int(myroi[1]+myroi[3]), int(myroi[0]):int(myroi[0]+myroi[2])]
 
    cv2.imshow("buildings05", imCrop)
    cv2.waitKey(0)
    cv2.imwrite("buildings05.jpg", imCrop)
