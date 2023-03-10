import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# img = cv2.imread('faces2.jpg')
# img = cv2.resize(img, (700, 500))
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = face_cascades.detectMultiScale(img_gray)

# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)




# cv2.imshow('Result', img)
# cv2.waitKey(0)


cap = cv2.VideoCapture('testvideo.mp4')

while True:
    success, frame = cap.read()
    # cv2.imshow('video', frame)
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascades.detectMultiScale(img_gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow('Result', frame)

    if cv2.waitKey(30) & 0xff == ord('q'):
        break