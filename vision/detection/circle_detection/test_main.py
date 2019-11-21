import os
import sys

# import other files
#
CWD = os.getcwd()
sys.path.append(CWD+'/vision/detection/circle_detection/')

from test_finder import detect_mushroom

if __name__ == "__main__":
    detect_mushroom()
