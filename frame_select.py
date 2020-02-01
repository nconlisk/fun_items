import sys
import argparse

import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    framesTotal = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    selector = 20
    print(framesTotal)
    count = 0
   
                   
    success = True
    while success:
        frameID = int(round(vidcap.get(1)))
        print(frameID)
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        if frameID%selector==0:
            print ('Writing frame_%d.jpg' % frameID)
            cv2.imwrite( pathOut + "\\frame%d.jpg" % frameID, image)     # save frame as JPEG file
            count += 1
    print('Number of images generated: %d'%count)
        


if __name__=="__main__":
    
    pathIn = "C:\\path\\to\\file\video.mp4"
    pathOut = "C:\\path\\to\\file"
    extractImages(pathIn, pathOut)

# TODO:
# Add section to write out camera/lens metadata.
# Create interactive GUI.

