# Python program to  Edge detection 
# using OpenCV in Python
# using Sobel edge detection 
# and laplacian method
import cv2
import numpy as np
  
#Capture livestream video content from camera 0
cap = cv2.VideoCapture(0)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()


while(1):
  
    # Take each frame
    _, frame = cap.read()
      
    # Convert to HSV for simpler calculations
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
      
    # Calcution of Sobelx
    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    
    fgmask =  fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
      
    # Calculation of Laplacian
    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
      
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('frame',fgmask)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        print(sobelx);  
        break
    
cv2.destroyAllWindows()
  
#release the frame
cap.release()
