import numpy as np
import cv2

canvas = np.zeros((10,10,3),dtype="uint8")  + 255
#pikselleri tek tek renklendiriyoruz

canvas[0,0]=(255,255,255)
canvas[0,1]=(200,255,200)
canvas[0,2]=(150,255,150)
canvas[0,3]=(15,255,15)

canvas= cv2.resize(canvas,(800,800),interpolation=cv2.INTER_AREA)
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()