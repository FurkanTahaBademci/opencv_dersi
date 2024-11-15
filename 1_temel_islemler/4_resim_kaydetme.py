import cv2

image = cv2.imread("images/klon.jpg")

print(image.shape)

roi = image[30:200,200:400]

cv2.imshow("ROI",roi)
cv2.imshow("Image",image)
cv2.imwrite("images/klon_roi.jpg",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()