import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('C:\Users\Sujay\Downloads\opencv extracted\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')   
count=0
frame_no=0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    count=count+1
    # Our operations on the frame come here
    if ret:
	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	    for (x,y,w,h) in faces:
	        cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),0)
	        #cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),0)
	    #if cv2.waitKey(1) & 0xFF == ord('c'):
	    	crop_img = gray[y: y + h, x: x + w]
	    # Display the resulting frame
	    	cv2.imshow('frame',frame)
	    	crop_img = cv2.resize(crop_img, (350, 350)) #Resize face so all images have same size

	    	if count%4 == 0:
	    		cv2.imwrite("test_images\\frame%s.jpg" %(frame_no),crop_img)
	    		frame_no=frame_no+1

	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
os.system('python classifier.py')
