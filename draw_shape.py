import cv2
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    image = cv2.line(frame,(0,0),(width,width),(255,0,0),4)
    cv2.rectangle(image,(0,0),(width,width),(0,255,0),10)
    cv2.circle(image,(200,200),50,(0,0,255),-1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image,'video_cap',(0,400),font,4,(0,0,255),cv2.LINE_AA)
    cv2.imshow('frame',image)
    if cv2.waitKey(1) == ord('k'):
        break
cap.release()
cv2.destroyAllWindows()