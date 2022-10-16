#group 2

import cv2

image = cv2.imread('image.jpg',0)              #load image in gray scale 


(minVal,maxVal,minLoc,maxLoc)=cv2.minMaxLoc(image)
images=cv2.circle(image,maxLoc,30,(255,255,255),5)

cv2.namedWindow("group2",cv2.WINDOW_NORMAL)
cv2.resizeWindow("group2",500,600)
cv2.imshow('group2',images)                     #display image in an window
cv2.waitKey(0)
print("The coordinate of point are:",maxLoc)


'''
The coordinate of point are: (1593, 2322)
'''