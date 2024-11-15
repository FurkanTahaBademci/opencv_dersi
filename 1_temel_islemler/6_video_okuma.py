import cv2

cap = cv2.VideoCapture("videos/antalya.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break  # Video bittiğinde döngüden çık

    frame_yeni = cv2.flip(frame, 0)

    # Videoları göster
    cv2.imshow("Video", frame)
    cv2.imshow("Yeni Video", frame_yeni)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

# Kaynakları serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
