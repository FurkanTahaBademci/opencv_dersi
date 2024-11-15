import numpy as np
import cv2

canvas = np.zeros((500,500,3),dtype="uint8")  + 255

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()