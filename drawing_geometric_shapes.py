import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2

def main():
    # array of all zeroes takes 2 arg shappe(W x H x no. of channel) and datatype 
    # to make a black convas of size 512 x 512
    img = np.zeros((512, 512, 3), np.uint8)

    #draw line takes 5 args imgcanvas, point1 , point2 , colorin (BGR), line_intensity
    cv2.line(img, (0,99), (99,0), (255,0,0), 2)
    
    #draw rectangle takes 5 args imgcanvas, top-left point, bottom-right point, color, intensity
    cv2.rectangle(img, (350,280), (280,50), (0,255,0), 2)
    
    #draw circle takes arg img, center-pt, radius, color, intensity
    cv2.circle(img,(190,190), 50, (0,0,255),2)
    
    # make intensity -1 to fill the closed shape
    cv2.circle(img,(390,190), 50, (0,255,255),-1)
    
    #draw elipse  takes arg frame, center,axes( major-axis, minor-axis) , start axist of rotation , end axis of rotation, color, intensity 
    cx,cy = 201,113
    frame= img
    ax1,ax2 =  57,27
    angle = -108
    center = (cx,cy)
    axes = (ax1,ax2)
    start_axis_of_rotation = 0
    end_axis_of_rotation = 360
    cv2.ellipse(frame, center, axes, angle, start_axis_of_rotation , end_axis_of_rotation, (255,0,0), 2)
    
    cv2.ellipse(frame, (100,200), axes, angle, start_axis_of_rotation , end_axis_of_rotation, (255,0,0), -1)
    
    #draw polylines
    points = np.array([[200, 400] , [250,400],[400,480],[400,300],[300,500]], np.int32)
    points = points.reshape((-1,1,2))
    cv2.polylines(img, [points], True, (255,65,200))
    
    # write text
    text1 = 'Testing hello'
    cv2.putText(frame, text1, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 2,(55,165,200))
    
    
    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')

   
if __name__ == "__main__":
    main()