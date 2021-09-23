import cv2
import numpy as np
def getcontours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(imgcontour,cnt,-1,(255,0,0),2)
        if area>500:
            cv2.drawContours(imgcontour,cnt,-1,(255,0,0),2)
        peri=cv2.arcLength(cnt,True)
        print(peri)
        approx=cv2.approxPolyDP(cnt,0.02*peri,True)
        print(len(approx))
        objcor=len(approx)
        x,y,w,h=cv2.boundingRect(approx)
        if objcor==3:objtype="TRi"
        elif objcor==4:
            aspratio=w/float(h)
            if aspratio>0.95 and aspratio<1.05: objtype="square"
            else:objtype="Reactangle"
        elif objcor>4: objtype="circle"
        else:objtype="none"
        cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(imgcontour,objtype,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,0),2)


        
path="C:/Users/KIIT/Desktop/opencv/shapes.png"
img=cv2.imread(path)
imgcontour=img.copy()


imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur=cv2.GaussianBlur(imggray,(7,7),1)
imgcanny=cv2.Canny(imgblur,50,50)
imgstack=np.hstack((imggray,imgblur))
getcontours(imgcanny)



#cv2.imshow("shapes",img)
#cv2.imshow("grays",imggray)
#cv2.imshow("blur",imgblur)
#cv2.imshow("full",imgstack)
#cv2.imshow("newimage",imgcanny)
cv2.imshow("naya",imgcontour)
cv2.waitKey(0)