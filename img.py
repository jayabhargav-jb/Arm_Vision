import cv2 
import numpy as np 
import matplotlib.pyplot as plot

image = cv2.imread('img_real.jpg') 
image = cv2.resize(image, (0, 0), fx = 0.8, fy = 0.8)
cv2.waitKey(0) 

h, w, _ = image.shape
h_needed = 720
w_needed = 1280


# cv2.imshow("som1", half)

# Grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
# cv2.imshow("win",gray)

# imFlood = gray.copy()
# h, w = gray.shape[:2]
# mask = np.zeros((h+2, w+2), np.uint8)
# cv2.floodFill(imFlood, mask, (0,0), 0)


# Find Canny edges 
edged = cv2.Canny(gray, 0, 200) 
cv2.waitKey(0) 
  
# Finding Contours 
# Use a copy of the image e.g. edged.copy() 
# since findContours alters the image 
contours, hierarchy = cv2.findContours(edged,  cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE) 
# print(contours[0])
# half = cv2.resize(edged, (0, 0), fx = 0.8, fy = 0.8)
cv2.imwrite("canny.jpg", edged)
# cv2.imshow('Canny Edges After Contouring', half) 
cv2.waitKey(0) 
  
print("Number of Contours found = " + str(len(contours))) 

# Draw all contours 
# -1 signifies drawing all contours 
cv2.drawContours(image, contours, -1, (0, 255, 0), 2) 

for c in contours:
    rect = cv2.boundingRect(c)
    # if rect[2] < 70 or rect[3] < 70: continue
    # if  cv2.contourArea(c) > 1000: continue
    # print (cv2.contourArea(c))
    x,y,w,h = rect
    print(x,y,w,h)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(image,str((x,y,w,h)),(x+w+10,y+h),0,0.3,(0,255,0))


# plot.imshow(image)
# plot.show()
# cv2.imshow('Contours', image)
cv2.imwrite('actual.jpg', image)
cv2.waitKey(0) 
cv2.destroyAllWindows() 