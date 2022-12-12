"""

"""

#packages
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time #for use of sleep



def openCamera():
    #camera channel
    if (cv2.VideoCapture(0).isOpened()):
        camera = cv2.VideoCapture(0)

    #video file
    video_file = ""

    while (True):
        ret, frame = camera.read()

        print('in loop')

        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        #display video frame
        cv2.imshow('frame', frame)
        
        # 'q' to quit loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        #TODO : enable 'X' window functino to quit

        time.sleep(.5) #for video processing time


    #releasing camera obj
    camera.release()
    #destroy windows
    cv2.destroyAllWindows()




if __name__ == '__main__':
    openCamera()
