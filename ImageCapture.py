import cv2


capture = cv2.VideoCapture(0)
ret,frame = capture.read()

while(True):
    cv2.imwrite('image.png',frame)
    cv2.destroyAllWindows()
    break

capture.release()    