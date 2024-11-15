import cv2

cap = cv2.VideoCapture(0)

fileName = "videos/kamera.avi"
codec =cv2.VideoWriter_fourcc('W','M','V','2')
frameRate=30
resolution=(640,480)

videoFileOutput =cv2.VideoWriter(fileName,codec,frameRate,resolution)


while True:
    ret, frame = cap.read()

    if not ret:
        break  # Video bittiğinde döngüden çık
    # Videoları göster
    
    videoFileOutput.write(frame)
    cv2.imshow("Video", frame)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

# Kaynakları serbest bırak ve pencereleri kapat
cap.release()
videoFileOutput.release()
cv2.destroyAllWindows()
