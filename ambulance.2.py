import cv2
import numpy as np
from time import sleep
import serial
width=80
height=80

offset1=8
offset2=1
offset3=3
offset4=3

position_line1=600
position_line2=300
position_line3=300
position_line4=550
delay= 60

detec = []
carno1 = 0
carno2 = 0
carno3 = 0
carno4 = 0
def photon(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx,cy

cap1 = cv2.VideoCapture('traffic.MP4')
cap2 = cv2.VideoCapture('video2.Mp4')
cap3 = cv2.VideoCapture('video3.Mp4')
cap4 = cv2.VideoCapture('video4.Mp4')
diff= cv2.createBackgroundSubtractorMOG2()
try:
    while True:
        ret1 , frame1 = cap1.read()
        ret2 , frame2 = cap2.read()
        ret3 , frame3 = cap3.read()
        ret4 , frame4 = cap4.read()
        temp = float(1/delay)
        sleep(temp)
        grey1 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
        grey2 = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
        grey3 = cv2.cvtColor(frame3,cv2.COLOR_BGR2GRAY)
        grey4 = cv2.cvtColor(frame4,cv2.COLOR_BGR2GRAY)
        blur1 = cv2.GaussianBlur(grey1,(3,3),5)
        blur2 = cv2.GaussianBlur(grey2,(3,3),5)
        blur3 = cv2.GaussianBlur(grey3,(3,3),5)
        blur4 = cv2.GaussianBlur(grey4,(3,3),5)
        img_sub1 = diff.apply(blur1)
        img_sub2 = diff.apply(blur2)
        img_sub3 = diff.apply(blur3)
        img_sub4 = diff.apply(blur4)
        dilat1 = cv2.dilate(img_sub1,np.ones((5,5)))
        dilat2 = cv2.dilate(img_sub2,np.ones((5,5)))
        dilat3 = cv2.dilate(img_sub3,np.ones((5,5)))
        dilat4 = cv2.dilate(img_sub4,np.ones((5,5)))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        dilution1 = cv2.morphologyEx (dilat1, cv2. MORPH_CLOSE , kernel)
        dilution2 = cv2.morphologyEx (dilat2, cv2. MORPH_CLOSE , kernel)
        dilution3 = cv2.morphologyEx (dilat3, cv2. MORPH_CLOSE , kernel)
        dilution4 = cv2.morphologyEx (dilat4, cv2. MORPH_CLOSE , kernel)
        dilution1 = cv2.morphologyEx (dilution1, cv2. MORPH_CLOSE , kernel)
        dilution2 = cv2.morphologyEx (dilution2, cv2. MORPH_CLOSE , kernel)
        dilution3 = cv2.morphologyEx (dilution3, cv2. MORPH_CLOSE , kernel)
        dilution4 = cv2.morphologyEx (dilution4, cv2. MORPH_CLOSE , kernel)
        box1,h1=cv2.findContours(dilution1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        box2,h2=cv2.findContours(dilution2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        box3,h3=cv2.findContours(dilution3,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        box4,h4=cv2.findContours(dilution4,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        
        cv2.line(frame1, (25, position_line1), (1200, position_line1), (255,127,0), 3) 
        for(i,c) in enumerate(box1):
            (x,y,w,h1) = cv2.boundingRect(c)
            valid_box = (w >= width) and (h1 >= height)
            if not valid_box:
                continue

            cv2.rectangle(frame1,(x,y),(x+w,y+h1),(0,255,0),2)        
            center = photon(x, y, w, h1)
            detec.append(center)
            cv2.circle(frame1, center, 4, (0, 0,255), -1)

            for (x,y) in detec:
                if y<(position_line1+offset1) and y>(position_line1-offset1):
                    carno1+=1
                    cv2.line(frame1, (25, position_line1), (1200, position_line1), (0,127,255), 3)  
                    detec.remove((x,y))
                    print("car is detected1 : "+str(carno1))        
           
        cv2.putText(frame1, "VEHICLE COUNT : "+str(carno1), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
        cv2.imshow("Original Video 1" , frame1)
        cv2.imshow("Pixelated1",dilution1)

        cv2.line(frame2, (25, position_line2), (1200, position_line2), (255,127,0), 3) 
        for(i,c) in enumerate(box2):
            (x,y,w,h2) = cv2.boundingRect(c)
            valid_box = (w >= width) and (h2 >= height)
            if not valid_box:
                continue

            cv2.rectangle(frame2,(x,y),(x+w,y+h2),(0,255,0),2)        
            center = photon(x, y, w, h2)
            detec.append(center)
            cv2.circle(frame2, center, 4, (0, 0,255), -1)

            for (x,y) in detec:
                if y<(position_line2+offset2) and y>(position_line2-offset2):
                    carno2+=1
                    cv2.line(frame2, (25, position_line2), (1200, position_line2), (0,127,255), 3)  
                    detec.remove((x,y))
                    print("car is detected2 : "+str(carno2))        
           
        cv2.putText(frame2, "VEHICLE COUNT : "+str(carno2), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
        cv2.imshow("Original Video 2" , frame2)
        cv2.imshow("Pixelated2",dilution2)

        cv2.line(frame3, (25, position_line3), (1200, position_line3), (255,127,0), 3) 
        for(i,c) in enumerate(box3):
            (x,y,w,h3) = cv2.boundingRect(c)
            valid_box = (w >= width) and (h3 >= height)
            if not valid_box:
                continue

            cv2.rectangle(frame3,(x,y),(x+w,y+h3),(0,255,0),2)        
            center = photon(x, y, w, h3)
            detec.append(center)
            cv2.circle(frame3, center, 4, (0, 0,255), -1)

            for (x,y) in detec:
                if y<(position_line3+offset3) and y>(position_line3-offset3):
                    carno3+=1
                    cv2.line(frame3, (25, position_line3), (1200, position_line3), (0,127,255), 3)  
                    detec.remove((x,y))
                    print("car is detected3 : "+str(carno3))        
           
        cv2.putText(frame3, "VEHICLE COUNT : "+str(carno3), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
        cv2.imshow("Original Video 3" , frame3)
        cv2.imshow("Pixelated3",dilution3)

        cv2.line(frame4, (25, position_line4), (1200, position_line4), (255,127,0), 3) 
        for(i,c) in enumerate(box4):
            (x,y,w,h4) = cv2.boundingRect(c)
            valid_box = (w >= width) and (h4 >= height)
            if not valid_box:
                continue

            cv2.rectangle(frame4,(x,y),(x+w,y+h4),(0,255,0),2)        
            center = photon(x, y, w, h4)
            detec.append(center)
            cv2.circle(frame4, center, 4, (0, 0,255), -1)

            for (x,y) in detec:
                if y<(position_line4+offset4) and y>(position_line4-offset4):
                    carno4+=1
                    cv2.line(frame4, (25, position_line4), (1200, position_line4), (0,127,255), 3)  
                    detec.remove((x,y))
                    print("car is detected4 : "+str(carno4))        
           
        cv2.putText(frame4, "VEHICLE COUNT : "+str(carno4), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),5)
        cv2.imshow("Original Video 4" , frame4)
        cv2.imshow("Pixelated4",dilution4)




        if cv2.waitKey(1) == 27:
            break

except:    
   cv2.destroyAllWindows()
   cap1.release()
   cap2.release()
   cap3.release()
   cap4.release()
