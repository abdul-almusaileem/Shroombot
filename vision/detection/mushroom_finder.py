import cv2
import numpy as np
import time
import math


def detect_mushroom():
  #print("THE THING IS LOOKING FOR MUSHROOMS")


  
  PHYSICAL_X = 22  # inches
  PHYSICAL_Y = 22

  MAX_REACH = 14
  
#  SHITTY_POINTS  = [[9, 8], [11, 7], [11, 8], [8, 9], [12, 7], [8, 8], [13, 7], [12, 8], [14, 8], [15, 8], [15, 7], [16, 8]]

#  SHITTY_POINTS =[[6, 6],	[7, 3],	[7, 6],	[8, 4],	[8, 7],	[8, 6],	[9, 6],	[10, 5], [27, 3], [27, 14], [6, 5], [6, 7], [6, 3], [7, 7], [8, 3], [11, 5], [7, 5], [7, 4], [9, 7]]

  SHITTY_POINTS = [[3, 3], [9, 3]]

  X_SHIFT = 9.2
  Y_SHIFT = 7.5


  capture_duration = 5
  cv2.namedWindow("preview")
  vc = cv2.VideoCapture(0)

  rval, frame = vc.read()

  coord_list = []
  coords_list_np = np.array([0, 0])
  start_time = time.time()
  while (int(time.time() - start_time) < capture_duration):
      #print("WHILE LOOP START")
      if frame is not None:   
  
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
      # define range of white color in HSV
      # change it according to your need !
        lower_white = np.array([0,0,0], dtype=np.uint8)
        upper_white = np.array([0,0,255], dtype=np.uint8)

      # Threshold the HSV image to get only white colors
        mask = cv2.inRange(hsv, lower_white, upper_white)
      # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame,frame, mask= mask)
      # Blur using 3 * 3 kernel. 
        gray_blurred = cv2.blur(gray, (3, 3)) 

        # flip image
        #
        #gray_blurred = cv2.flip(gray, 0)
        
      # Apply Hough transform on the blurred image. 
        detected_circles = cv2.HoughCircles(gray_blurred,  
                                          cv2.HOUGH_GRADIENT,
                                          1,
                                          minDist=500,
                                          param1 = 50, 
                                          param2 = 30,
                                          minRadius = 10,
                                          maxRadius = 60) 
      #param 1 50
      #param 2 30  
      # Draw circles that are detected. 
      if detected_circles is not None: 
  
      # Convert the circle parameters a, b and r to integers. 
        detected_circles = np.uint16(np.around(detected_circles)) 
  
      for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2]

        physical_x = a / frame.shape[0] * PHYSICAL_X
        physical_y = b / frame.shape[1] * PHYSICAL_Y
        coords_list_np = np.row_stack((coords_list_np, [physical_x, physical_y]))
 
        # coords = str(a) + " " + str(b) + "\n"
        # coord_list.append(coords)

        # print("X: " +  str(a)  + " Y: " + str(b))
        # Draw the circumference of the circle. 
      cv2.circle(gray_blurred, (a, b), r, (0, 255, 0), 2) 
  
        # Draw a small circle (of radius 1) to show the center. 
      cv2.circle(gray_blurred, (a, b), 1, (0, 0, 255), 3)    


      cv2.imshow("preview", gray_blurred)
  

      rval, frame = vc.read()

      if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    # (8.3, 8.3) always shows up
    # List Processing #
  unique_coord = np.unique(coords_list_np, axis=0)

  # flip the image
  #
  
  #print("list {}".format(coords_list_np))
  #print("uniq {}".format(unique_coord))

  # initiat list
  #
  final_coord = []

  # filter ghost points 
  #
  for index in range(len(unique_coord)):
    #print("index: {}".format(index))
    
    # filter shitty points 
    #
    if [round(unique_coord[index, 0]), round(unique_coord[index, 1])] in SHITTY_POINTS:
     # print("shitty point {}".format(unique_coord[index]))
      continue

    # store first index
    #
    if index == 0:
     # print("added firts point")
      final_coord = np.array([unique_coord[index]])
    else:
      target_x = unique_coord[index-1, 0]
      target_y = unique_coord[index-1, 1]
      comp_x = unique_coord[index, 0]
      comp_y = unique_coord[index, 1]
      if target_x - 1 < comp_x < target_x + 1  and target_y - 1 < comp_y < target_y + 1:
        # Do Nothing
        pass
      #  print("ghost")
      else:
        final_coord = np.row_stack((final_coord, unique_coord[index, :]))
        #final_coord = final_coord[1:, :]
        #print("uniq {}".format(unique_coord))
        #final_coord.append([unique_coord[index]])
        #print("final {}".format(final_coord))


  shifted_output = []
  #print("")
  #print("Thelength of final_coord is {}".format(len(final_coord)))
  #print(final_coord)

  if final_coord is not None:
    for point in final_coord:
      tmp = []
      #if (point[0] < X_SHIFT):
        #shifted_x = point[0] + X_SHIFT
      
      #else:
        #shifted_x = X_SHIFT - point[0]

      # X: if x < 9.2 the point is gonna be (+) right of the arm
      #    if x >= 9.2 the point ia gonna be (- or 0) left of the arm
      # Y: y is alwayse (+)
      #
      shifted_x = X_SHIFT - point[0]  
      shifted_y = Y_SHIFT + point[1]

      if (shifted_y < MAX_REACH) and (shifted_x < MAX_REACH):
        tmp.append(shifted_x)
        tmp.append(shifted_y)
        shifted_output.append(tmp)


        
  print("original {}".format(final_coord))
  print("shifted {}".format(shifted_output))


  print("----------------------")
  
  vc.release()

  cv2.destroyAllWindows()
  shifted_output.remove(shifted_output[0])
  return(shifted_output)
