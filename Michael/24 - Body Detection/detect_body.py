import numpy as np
import cv2
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
upper_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
lower_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')
img = cv2.imread('spiderman.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bodies = body_cascade.detectMultiScale(gray, 1.3, 5)
upper = upper_cascade.detectMultiScale(gray, 1.3, 5)
lower = lower_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

for (x,y,w,h) in upper:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

for (x,y,w,h) in lower:
    cv2.rectangle(img,(x,y),(x+w,y+h),(150,0,150),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()