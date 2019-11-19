##############################################################
#   Libraries
##############################################################
import cv2 as cv
import numpy as np
import time
import os

##############################################################
#   Variable Definition
##############################################################
# Write down conf, nms thresholds,inp width/height
confThreshold = 0.25
nmsThreshold = 0.40
inpWidth = 416
inpHeight = 416
PHYSICAL_WIDTH = 22
PHYSICAL_HEIGHT = 16.5
# Load names of classes and turn that into a list
classesFile = "thisisonyou_obj.names"  # "coco.names"  #
classes = None
# Model configuration
modelConf = 'cfg_tiny.cfg'  # "yolov3.cfg"  #
modelWeights = 'peters-5.2.6.weights'  # "yolov3.weights"  #


##############################################################
#   Function Prototype
##############################################################
# Operation Post Porcess
# Process the frame is taken from picture
# Input: frame, outs
# Output: None
def postprocess(frame, outs):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]
    classIDs = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:

            scores = detection[5:]
            classID = np.argmax(scores)
            confidence = scores[classID]

            if confidence > confThreshold:
                centerX = int(detection[0] * frameWidth)
                centerY = int(detection[1] * frameHeight)

                width = int(detection[2] * frameWidth)
                height = int(detection[3] * frameHeight)

                left = int(centerX - width / 2)
                top = int(centerY - height / 2)

                classIDs.append(classID)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

    indices = cv.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)

    indices = cv.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
    for i in indices:
        i = i[0]
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]

        drawPred(classIDs[i], confidences[i], frame, left, top, left + width, top + height)


# Operation DrawPred - draw_prediction
# Draw the imaginary box for the detection result
def drawPred(classId, conf, frame, left, top, right, bottom):
    # Draw a bounding box.
    cv.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)
    mushroom_location_pixel = [(left + right) / 2, (top + bottom) / 2]
    print("Mushroom Detected at location (pixel): (", (left + right) / 2, ",", (top + bottom) / 2, ")")

    # Calculate the Physical Height
    frame_height = frame.shape[0]
    frame_width = frame.shape[1]
    physical_x = (left + right) / 2 / frame_width * PHYSICAL_WIDTH
    physical_y = (top + bottom) / 2 / frame_height * PHYSICAL_HEIGHT
    print("Mushroom Detecte at location (physical): (", physical_x, ",", physical_y, ")")
    file = open("location.txt", "a")
    write_string = str(physical_x) + " " + str(physical_y) + "\n"
    file.write("%s %s\n" % (physical_x, physical_y))
    file.close()

    label = '%.2f' % conf
    # Get the label for the class name and its confidence
    if classes:
        assert (classId < len(classes))
        label = '%s:%s' % (classes[classId], label)


# Operation getOutputNames
# Obtain output names from network
def getOutputsNames(net):
    # Get the names of all the layers in the network
    layersNames = net.getLayerNames()
    # Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]


##############################################################
#   Main Function
##############################################################
def camera_module():
    # Open File that contains all class information
    with open(classesFile, 'rt') as f:
        classes = f.read().rstrip('\n').split('\n')
    # Set up the net
    net = cv.dnn.readNetFromDarknet(modelConf, modelWeights)
    net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)
    # Take a picture via camera
    cap = cv.VideoCapture(0)
    # While loop for continuous taking picture
    # while cv.waitKey(1) < 0:  # While for video purposes
    # get frame from video
    hasFrame, frame = cap.read()
    # Remove file
    if os.path.exists("location.txt"):
        os.remove("location.txt")
    # Create a 4D blob from a frame
    blob = cv.dnn.blobFromImage(frame, 1 / 255, (inpWidth, inpHeight), [0, 0, 0], 1, crop=False)

    # Set the input the the net
    net.setInput(blob)
    outs = net.forward(getOutputsNames(net))
    postprocess(frame, outs)

    # Sleep to reduce frame - Video Purposes
    # time.sleep(1)
    # break


##############################################################
#    Main Function Runner
##############################################################
if __name__ == "__main__":
    camera_module()
