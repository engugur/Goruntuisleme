import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while (True):
    RED, vid = cam.read()
    hsv = cv2.cvtColor(vid, cv2.COLOR_BGR2HSV)

    low=np.array([155, 0, 0])
    upp=np.array([185, 255, 255])

    mask=cv2.inRange(hsv,low,upp)
    alt=cv2.bitwise_and(vid, vid, mask=mask)
    alt=cv2.cvtColor(alt, cv2.COLOR_BGR2GRAY)
    RED, alt = cv2.threshold(alt,10,255,cv2.THRESH_BINARY)

    cv2.imshow("cam", vid)
    cv2.imshow("alt",alt)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()