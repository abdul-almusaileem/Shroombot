import numpy as np
import cv2 as cv
#img = cv.imread('4.3-Aplin.jpeg')
img = cv.imread('grey_scaled_dummy.jpeg')

#Convert to HSV color to more easily filter for magenta
#
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lower_magenta = np.array([240,0,0])
upper_magenta = np.array([300,100,255])

# Here we are defining range of magentacolor in HSV
# This creates a mask of magenta coloured
# objects found in the frame.
mask = cv.inRange(img, lower_magenta, upper_magenta)


# The bitwise and of the frame and mask is done so
# that only the magenta coloured objects are highlighted
# and stored in res
res = cv.bitwise_and(img,img, mask= mask)

#convert back to use with opencv modules
new_img = cv.cvtColor(res, cv.COLOR_BGR2GRAY)

#find contours to find rectangles
contours, hierarchy = cv.findContours(new_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#create place to store contours found under conditionals
contour_list = []

#loop through all contours to find rectangles and right sized rectangles
for contour in contours:
   approx = cv.approxPolyDP(contour,0.01*cv.arcLength(contour,True),True)
   area = cv.contourArea(contour)

   #conditional for sides of shape
   if len(approx) == 4:
		# compute the bounding box of the contour and use the
		# bounding box to compute the aspect ratio
        (x, y, w, h) = cv.boundingRect(approx)
        ar = w / float(h)
        # if ar = 1 then is square
        shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
        if shape == "square" or "rectangle":
            #filtering for size so little tiny ones don't show
            if ( ((area >= 900) & (area <= 9000000)) ):
                contour_list.append(contour)


#draw contours onto image
mask2 = cv.drawContours(new_img,contour_list,-1,(255,0,0),10)

#find center of rectangles (pixels)
#try:
for c in contour_list:
    # compute the center of the contour
    M = cv.moments(c)
    #these are the pixel location of center of rectangle
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    print str(cX) + " " + str(cY)
    # draw the contour and center of the shape on the image
    cv.putText(mask2, "center", (cX - 20, cY - 20),
    cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv.LINE_AA)
#except:
#    print("error:no object detected")

cv.imwrite("Image.jpg", mask2)
