import cv2

face_cascade=cv2.CascadeClassifier('C:/Users/KIIT/Desktop/opencv/haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
while True:
    file,img=cap.read()



    
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.1,4)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+w),(255,0,0),2)
    
    cv2.imshow('img',img)


    if cv2.waitKey(1) & 0xFF ==ord('q'): 
        break
cap.release()


