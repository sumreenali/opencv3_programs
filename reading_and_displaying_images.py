import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2

def main():
   # print(cv2.__version__)
   
   
   #IMPORT IMAGE PATH  , READ IMAGE & DISPLAY IMAGE  
   imgpath = "E:\\OpenCV\\dataset\\lena_color_256.tif" 
   img = cv2.imread(imgpath) 
   
   #TO CREATE A SEPARATE WINDOW
   cv2.namedWindow('Lena', cv2.WINDOW_AUTOSIZE)
   
   #DISPLAY IMAGE
   cv2.imshow('Lena', img)
   
   #THIS FUNCTOION IS TO DESTROY THE WINDOW ON PRESSING ANY OF THE KEYBOARD 
   # - IN SHORT BINDING THE WINDOW WITH KEYBOARD
   cv2.waitKey(0)
   #FOR DISTROYING ALL WINDOWS
   # cv2.destroyAllWindows()  
   
   #FOR DISTROYING SINGLE WINDOWS
   cv2.destroyWindow('Lena')

   
if __name__ == "__main__":
    main()