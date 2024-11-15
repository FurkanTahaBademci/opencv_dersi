import cv2

image = cv2.imread("images/klon.jpg")

dimension = image.shape

print("Boyut: ", dimension)

image[420,500] = [255,0,0]
image[420,501] = [255,0,0]



cv2.imshow("Klon", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

