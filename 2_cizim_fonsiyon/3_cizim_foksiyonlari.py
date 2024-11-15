import numpy as np
import cv2

canvas = np.zeros((500,500,3),dtype="uint8")  + 255

cv2.line(canvas,(0,0),(500,500),(255,0,0),2)
cv2.rectangle(canvas,(140,120),(300,300),(0,255,0),2)
cv2.circle(canvas,(250,250),100,(0,0,255),2)


#üçgen çizme
p1=(100,200)
p2=(50,50)
p3=(300,100)

cv2.line(canvas,p1,p2,(0,0,0),2)
cv2.line(canvas,p2,p3,(0,0,0),2)
cv2.line(canvas,p3,p1,(0,0,0),2)

#yazı fontları
font1 = cv2.FONT_HERSHEY_SIMPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX


cv2.putText(canvas,'OpenCV',(30,100),font1,2,(0,0,0),cv2.LINE_4) #(çizilicek yer adı,yazılacak yazı,metnin konumu,FONT)


cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()