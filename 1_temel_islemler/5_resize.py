import cv2

image = cv2.imread("images/klon.jpg")

dimesion = image.shape

resized_image = cv2.resize(image,(dimesion[1]//3,dimesion[0]//3))


cv2.imshow("Resized Image",resized_image)
cv2.imshow("Original Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()