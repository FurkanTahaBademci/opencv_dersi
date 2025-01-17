import cv2
import numpy as np
import requests

url = "http://192.168.1.78:8080/shot.jpg"


while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)

    cv2.imshow("IP Camera", img)
    cv2.waitKey(1)
    

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()