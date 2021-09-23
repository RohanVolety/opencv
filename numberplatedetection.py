import cv2
numberplateCascade=cv2.CascadeClassifier("C:/Users/KIIT/Desktop/opencv/haarcascade_russian_number_plate.xml")
frameWidth=640
frameheight=480
cap=cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameheight)
cap.set(10,150)
minarea=500
while True:
    success, img = cap.read()

    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberplates=numberplateCascade.detectMultiScale(imgGray,1.1,4)

    for (x,y,w,h) in numberplates:
        area=w*h
        if area>minarea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(img,"Number plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),2)

            imgroi=img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgroi)


    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): 
        break