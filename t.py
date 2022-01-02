import cv2
cap = cv2.VideoCapture('http://192.168.1.42:80/snapshot.cgi?user=admin&pwd=lali197&next_url=tempsnapshot.jpg&count=16951')

while True:
    ret, frame = cap.read()
    img = cap.read()

    cv2.imshow('Image', img)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()