import cv2

def filtroRGB(src,r,g,b):
    if r == 0:
        src[:,:,2] = 0   
    if g == 0:
        src[:,:,1] = 0    
    if b == 0:
        src[:,:,0] = 0   

beach = cv2.imread('buildings05.jpg')
filtroRGB(beach,0,255,0) 
cv2.imshow('Ta verde',beach)


cv2.imshow('buildings05', beach)
cv2.waitKey(0)
cv2.destroyAllWindows()
